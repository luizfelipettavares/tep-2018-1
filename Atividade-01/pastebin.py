'''
PASTEBIN

Endpoint: https://pastebin.com/api/api_post.php


O pastebin eh uma aplicacao web onde voce pode enviar trechos de codigo. 
Nele voce pode determinar o tempo que o codigo ficara armazenado no site e 
quem poderah ter acesso. Essa API eh disponibilizada para desenvolvedores 
que queiram construir algo para o pastebin

Recursos: number, type (date, math, random, trivia)

Metodos: POST, GET, DELETE
'''

import requests
 
url = "http://pastebin.com/api/api_post.php"
 
key = "xxxxx"
 
code = '''
import requests

print("Retorna um numero aleatorio, do tipo math, e um fato relacionado ao mesmo")
url = 'http://numbersapi.com/random/math?json'
response = requests.get(url)
json = response.json()
print(json)
'''

data = {
		'api_dev_key':key,
        'api_option':'paste',
        'api_paste_code':code,
        'api_paste_format':'python',
        'api_paste_private':0
        }
 
response = requests.post(url = url, data = data)
 
pastebin_url = response.text
print("The pastebin URL is:%s"%pastebin_url)