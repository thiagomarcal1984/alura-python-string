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
