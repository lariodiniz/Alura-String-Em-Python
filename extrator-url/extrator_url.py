class ExtratorURL:
    def __init__(self, url):
        self.__url = self.sanitiza_url(url)
        self.__valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def __valida_url(self):
        if not self.__url:
            raise ValueError('A URL está vazia')
        if not self.__url.startswith('http'):
            raise ValueError('A URL não segue o protocolo http') 
        if not self.get_url_base().endswith ('cambio'):
            raise ValueError('A URL base não termina em cambio') 

    def get_url_base(self):
        indice_interrogacao = self.__url.find('?')
        url_base = url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.__url.find('?')
        url_parametro = url[indice_interrogacao+1:]
        return url_parametro

    def get_valor_parametro(self, parametro):
        url_parametro = self.get_url_parametros()
        indice_parametro = url_parametro.find(parametro)
        indice_valor = indice_parametro + len(parametro) +1
        indice_e_comecial = url_parametro.find('&', indice_valor)
        if indice_e_comecial == -1:
            valor = url_parametro[indice_valor:]
        else:
            valor = url_parametro[indice_valor:indice_e_comecial]
        
        return valor

    @property
    def url(self):
        return self.__url
        

url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)