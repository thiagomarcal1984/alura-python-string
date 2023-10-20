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
