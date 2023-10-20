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
