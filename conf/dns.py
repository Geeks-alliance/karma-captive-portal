import sys, traceback, socket
# NOTICE: This DNS server works with python 2 and python 3

class DNSQuery:
  def __init__(self, data):
    self.data = data
    self.domain = ''

    queryType = (ord(data[2]) >> 3) & 15

    # Only handle basic requests.
    if queryType != 0:
      print('Ignoring Query: Non-spoofed type.')
      return

    domainStart = 13 # Skip length byte and start at domain.
    domainLength = ord(data[domainStart - 1]) # Evaluate length byte.

    while domainLength != 0:
      self.domain += data[domainStart : domainStart + domainLength] + '.'

      domainStart += domainLength + 1 # Skip the length byte & start at domain.
      domainLength = ord(data[domainStart - 1]) # Evaluate length byte.

  def response(self, ipv4):
    if not self.domain: return ''

    packet = ''

    packet += self.data[ :2] + '\x81\x80'
    packet += self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'
    packet += self.data[12:]
    packet += '\xc0\x0c'
    packet += '\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'

    # Convert string IPv4 quads to binary values (bytes).
    packet += str.join('', map(lambda s: chr(int(s)), ipv4.split('.')))

    return packet

if __name__ == '__main__':
  targetIPv4 = '10.0.0.1'

  print('Mini DNS Spoofer:: dom.query. 60 IN A %s' % targetIPv4)

  link = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  link.bind(('',53))

  try:
    while True:
      clientData, clientIPv4 = link.recvfrom(1024)

      queryData = clientData if sys.version_info < (3, 0) else clientData.decode('unicode_escape')

      query = DNSQuery(queryData)

      response = query.response(targetIPv4)

      if sys.version_info > (3, 0):
        # Someone that knows more about python and how it does byte-handling,
        # please fix the following shitfest and make it a bit more elegant.
        # Do what? A raw conversion of the "response" string to bytes.
        responseHex = ''
        for xx in response:
          responseHex += "%x%x" % ((ord(xx) >> 4) & 0b1111, ord(xx) & 0b1111)

        response = bytearray.fromhex(responseHex)

      link.sendto(response, clientIPv4)

      print('Request: %s -> %s' % (query.domain, targetIPv4))

  except KeyboardInterrupt:
    print('INTERRUPT: Stopping.')
    link.close()

  except Exception as error:
    print('EXCEPTION: Stopping!')
    print(error)
    print(traceback.format_exc())
    link.close()
