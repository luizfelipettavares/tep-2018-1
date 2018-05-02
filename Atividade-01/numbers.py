'''

1. Numbers API
2. Uma API para fatos interessantes sobre números.
3. http://numbersapi.com/
4. http://numbersapi.com/number/type/
	number: 
		> um inteiro
		> a palavra-chave random
		> um dia no formato mês/ano (exemplo 5/2), se type for date

	type:
		> trivia: algum fato aleatorio relacionado ao numero
		> math: algum fato matematico relacionado ao numero
		> date: algum fato ao data
		> year: algum fato relacionado ao ano

5. Suporta metodo GET
6. Exemplo
'''

import requests

print("Retorna um numero aleatorio, do tipo math, e um fato relacionado ao mesmo")
url = 'http://numbersapi.com/random/math?json'
response = requests.get(url)
json = response.json()
print(json)

print("Retorna um fato relacionado ao numero 15")
url = 'http://numbersapi.com/15?json'
response = requests.get(url)
json = response.json()
print(json)

print("Retorna um fato relacionado a data 02 de maio")
url = 'http://numbersapi.com/5/2/date?json'
response = requests.get(url)
json = response.json()
print(json)

print("Retorna um fato relacionado a um ano aleatorio")
url = 'http://numbersapi.com/random/year?json'
response = requests.get(url)
json = response.json()
print(json)