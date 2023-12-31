import re

class ExtratorURL:
    def __init__(self, url):
        self.__url = self.__sanitiza_url(url)
        self.valida_url()

    def __sanitiza_url(self, url):
        if type(url) == str: # O método strip() só existe em strings.
            return url.strip()
        else:
            return ""

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
        if not self.__url: # bool("") é igual a False.
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www\.)?bytebank\.com(\.br)?/cambio')
        # O padrão deve casar com o início da string, 
        # daí o match ao invés de search.
        match = padrao_url.match(self.__url) 

        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.__url.find('?')
        url_base = self.__url[: indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.__url.find('?')
        url_parametros = self.__url[indice_interrogacao + 1 :]
        return url_parametros
    
    def __len__(self):
        return len(self.__url)
    
    def __str__(self):
        return "".join([
            "URL: ", 
            self.__url,
            "\nParâmetros: ",
            self.get_url_parametros(),
            "\nURL Base: ", 
            self.get_url_base()
        ])

    def __eq__(self, other):
        return self.__url == other.__url

url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
print('Id1.: ', id(extrator_url), '\n\rId2.: ', id(extrator_url2))
print(extrator_url == extrator_url2) # Retorna True, a URL é igual.
