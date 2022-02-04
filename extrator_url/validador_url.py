import re

url = ''
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)
if not match:
    raise ValueError("A URL é valdia")
