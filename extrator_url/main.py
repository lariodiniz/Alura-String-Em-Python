url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
url = ' '


# Sanitização da url
# url = url.replace(" ", "")
url = url.strip()
# url.strip() # tira os espaçoes em branco dos dois lados
# url.rstrip() # tira os espaçoes em branco do lado direito
# url.lstrip() # tira os espaçoes em branco do lado esquerdo


if url == '':
    raise ValueError('A URL está vazia')

indice_interrogacao = url.find('?')

if indice_interrogacao != -1:

    url_base = url[:indice_interrogacao]
    url_parametro = url[indice_interrogacao+1:]
    print(url_parametro)

    parametro_busca = 'quantidade'
    indice_parametro = url_parametro.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) +1
    indice_e_comecial = url_parametro.find('&', indice_valor)
    if indice_e_comecial == -1:
        valor = url_parametro[indice_valor:]
    else:
        valor = url_parametro[indice_valor:indice_e_comecial]

    print(valor)

else:
    print('? não encontrado na url')