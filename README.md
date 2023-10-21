# Parâmetros em páginas da Internet
Temos a seguinte URL:
https://www.example.co.uk:443/blog/article/search?docid=720&hl=en#dayone

As 9 partes de uma URL:
1. Esquema/protocolo: `https://`
2. Subdomínio: `www.`
3. Domínio: `example.`
4. TLD (Top Level Domain): `co.uk`
5. Número da porta: `:443`
6. Path (caminho): `/blog/article/search`
7. Separador de query string: `?`
8. Parâmetros da query string (separados por `&`): `docid=720&hl=en`
9. Fragmento: `#dayone`

# Fatiamento de strings
O fatiamento de strings é feito com colchetes. Dentro dos colchetes podemos colocar um único inteiro ou dois números inteiros separados por dois pontos (o primeiro inteiro é incluído, e o segundo inteiro é excluído).

```python
>>> texto = 'abcde'
>>> texto[1] # Fatiamento com um inteiro.
'b'
>>> texto[1:2] 
# Fatiamento com dois inteiros (inclui posição 1 e exclui posição 2)
'b'
>>> texto[1:3] # Inclui a posição 1 e exclui a posição 3. 
'bc'
>>> texto[0:2] # Inclui a posição 0 e exclui a posição 2. 
'ab'
```
O processo de fatiamento não modifica a string original: o fatiamento de strings sempre gera novas strings.

Novo código no arquivo `main.py`:
```python
url = 'bytebank.com/cambio?moedaOrigem=real'
print('URL: ', url)

url_base = url[0:19]
print('URL Base: ', url_base)

url_parametros = url[20:36]
print('URL Parâmetros: ', url_parametros)
```
# O método find()
O método `find('string_procurada')` de objetos string retorna a posição da string procurada.

O fatiamento da string pode:
1. omitir o primeiro parâmetro (ou seja, inclui o primeiro caracter da string: `'aeiou'[:3]` retorna `aei`);
2. omitir o segundo parâmetro (ou seja, inclui o último caracter da string: `'aeiou'[3:]` retorna `ou`);
3. omitir os dois parâmetros de fatiamento, que resulta na string completa (`'aeiou'[:]` retorna `'aeiou'`).

Finalmente, os parâmetros do fatiamento podem conter uma variável.

Código do arquivo `main.py`:
```python
url = 'https://bytebank.com/cambio?moedaOrigem=real'
print('URL: ', url)

indice_interrogacao = url.find('?')

url_base = url[: indice_interrogacao]
print('URL Base: ', url_base)

url_parametros = url[indice_interrogacao+1 : ]
print('URL Parâmetros: ', url_parametros)
```
# Para saber mais: Documentação - método find
O método `find` tem 3 parâmetros posicionais (os dois últimos opcionais):

1. substring: a string procurada (`'abracadabra'.find('b')` retorna `1`);
2. start: o índice a partir do qual a substring será procurada (`'abracadabra'.find('b', 5)` retorna `1`);
3. end: o índice até o qual a substring será procurada (`'abracadabra'.find('b', 2, 7)` retorna `-1`, ou seja, não encontra a string `'b'` depois da posição 2 e antes da posição 7).

> Não use a sintaxe de parâmetros chave/valor:
>```python
>'abracadabra'.find(sub='b', start=2, end=7)
>```
> Essa sintaxe não funciona.

# O método len()
O método `len(string)` retorna o tamanho da string.

Modificações no arquivo `main.py`:
```python
url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

indice_interrogacao = url.find('?')

url_base = url[: indice_interrogacao]

url_parametros = url[indice_interrogacao+1 :]
print('URL Parâmetros: ', url_parametros)

parametro_busca = 'moedaOrigem'
# Achar a posição do nome do parâmetro na string de busca.
indice_parametro = url_parametros.find(parametro_busca)

# Achar a posição do valor a partir da posição do nome do
# parâmetro na string de busca. Isso corresponde à posição
# inicial do parâmetro somado com o tamanho do nome do
# parâmetro, somado a 1.
indice_valor = indice_parametro + len(parametro_busca) + 1

# Se o valor procurado for 'moedaOrigem', retorna 'real'.
# Mas se o valor procurado for 'moedaDestino', retorna a
# querystring quase toda ('dolar&moedaOrigem=real').
valor = url_parametros[indice_valor : ]
print(valor)
```

# URL com múltiplos parâmetros
Veja no código `main.py` a lógica do teste para localização do ampersand:

```python
url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[: indice_interrogacao]
url_parametros = url[indice_interrogacao+1 :]
print('URL Parâmetros: ', url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'

# Achar a posição do nome do parâmetro na string de busca.
indice_parametro = url_parametros.find(parametro_busca)

# Achar a posição do valor a partir da posição do nome do
# parâmetro na string de busca. Isso corresponde à posição
# inicial do parâmetro somado com o tamanho do nome do
# parâmetro, somado a 1.
indice_valor = indice_parametro + len(parametro_busca) + 1


# Procura o ampersand (e_comercial) depois do índice do valor.
indice_e_comercial = url_parametros.find('&', indice_valor)

# Se encontrar o ampersand, recupera a string a partir do 
# índice até o ampersand. Se não encontrar, recupera a 
# string a partir do índice até o fim.
if indice_e_comercial != -1: # Encontrou o ampersand.
    valor = url_parametros[indice_valor : indice_e_comercial]
else: # Não encontrou o ampersand.
    valor = url_parametros[indice_valor : ]
    
print(valor)
```

# Validando a URL
O foco agora é fazer o tratamento de URLs vazias. Duas coisas:

1. Há caracteres invisíveis (tabulação, espaços, quebras de linha, retorno de carro etc.) que precisam ser suprimidos das extremidas da string. Isso é possível graças ao método `strip` (e suas variantes `lstrip` e `rstrip`). Outra alternativa é usando o comando `replace(string_procurada, string_substituta)`.
2. Caso a string esteja vazia, uma exceção/erro precisa ser exibida. Para isso, usamos o comando `raise` seguido do tipo de exceção/erro que exibiremos.

Código do arquivo `main.py`:
```python
url = "\t  \n\r \t"

# Sanitização da URL
url = url.lstrip() # Strip do lado esquerdo.
url = url.rstrip() # Strip do lado direito.
url = url.strip() # Strip dos dois lados.

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")
# Resto do código
```
# Criando nossa classe
O código do arquivo `main.py` foi copiado e adaptado para o arquivo `extrator_url.py`, cujo conteúdo é mostrado a seguir:

```python
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
```
