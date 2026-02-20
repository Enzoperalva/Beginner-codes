import urllib.request

try:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}
    req = urllib.request.Request('https://pudim.com.br/', headers=headers)
    site = urllib.request.urlopen(req, timeout=5)
    print('Tudo ok')
except Exception as erro:
    print(f'Servidor indisponível. ERRO: {erro}')