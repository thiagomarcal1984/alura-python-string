class ExtratorURL:
    def __init__(self, url):
        self.__url = self.__sanitiza_url(url)
        self.valida_url()

    def __sanitiza_url(self, url):
        return url.strip()

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial != -1:
            valor = self.get_url_parametros()[indice_valor : indice_e_comercial]
        else:
            valor = self.get_url_parametros()[indice_valor : ]
            
        return valor

    def valida_url(self):
        if self.__url == "":
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.__url.find('?')
        url_base = self.__url[: indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.__url.find('?')
        url_parametros = self.__url[indice_interrogacao + 1 :]
        return url_parametros

extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
