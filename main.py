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
