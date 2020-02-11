'''
import requests
import json

bozulanDoviz = input('Bozulan Döviz Türü : ')
alinanDoviz = input('Alınan Döviz Türü : ')

result = requests.get(f'https://api.exchangeratesapi.io/latest?base={bozulanDoviz}')
jsonData = json.loads(result.text)
alinanDovizOrani = jsonData['rates'][alinanDoviz]

money = int(input(f'Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz: '))
print(f'1 {bozulanDoviz} = {alinanDovizOrani} {alinanDoviz}')
print(f'{money} {bozulanDoviz} = {alinanDovizOrani * money} {alinanDoviz}')
'''
import requests
import json 

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input('Bozulan Döviz Türü : ')
alinan_doviz = input('Alınan Döviz Türü : ')
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,result['rates'][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result['rates'][alinan_doviz],alinan_doviz))