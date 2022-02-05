import re
from decimal import Decimal
class ExtratorURL:

    @property
    def url(self):
        return self.__url

    def __init__(self, url):
        self.__url = self.sanitiza_url(url)
        self.__valida_url()
        self.__valor_dolar_real = Decimal(5.50)

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def __valida_url(self):
        if not self.__url:
            raise ValueError('A URL está vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.__url)
        if not match:
            raise ValueError("A URL não é valida")

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

    def conversao(self):
        quantidade = Decimal(extrator_url.get_valor_parametro("quantidade"))
        destino = extrator_url.get_valor_parametro("moedaDestino")
        origem = extrator_url.get_valor_parametro("moedaOrigem")
       
        if destino == 'dolar' and origem =='real':
            conversao = quantidade / self.__valor_dolar_real
            print(f'Convertendo {quantidade:.2f} {origem} para {destino}: {conversao:.2f}')
        elif destino == 'real' and origem =='dolar':
            conversao = quantidade * self.__valor_dolar_real
            print(f'Convertendo {quantidade:.2f} {origem} para {destino}: {conversao:.2f}')
        else:
            print('Conversão não disponivel')

        

    def __len__(self):
        return len(self.__url)
        

    def __str__(self):
        return f'{self.url} \nParametros: {self.get_url_parametros()}\nURL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
#extrator_url_2 = ExtratorURL(url)
#print(extrator_url_2 == extrator_url)

valor_quantidade = extrator_url.get_valor_parametro("quantidade")

#print(f'O tamanho da URL é : {len(extrator_url)}')
#print(extrator_url)
#rint(valor_quantidade)
extrator_url.conversao()
