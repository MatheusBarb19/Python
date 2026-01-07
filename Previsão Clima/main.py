import requests

api_key = "2c3d69cede2715e35d376613b5badb81" #chave da api openweather
cidade = input("Cidade desejada: ") #cidade selecionada

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link) #get.    = Pegar informações da api
requisicao_dic = requisicao.json()


descricao = requisicao_dic['weather'][0]['description']

temperatura = requisicao_dic['main']['temp'] - 273.15 #Transf. Kelvin para Celsius
temp_max = requisicao_dic['main']['temp_max'] - 273.15
temp_min = requisicao_dic['main']['temp_min'] - 273.15

humidade = requisicao_dic['main']['humidity']


print(descricao, f"{temperatura} ºC", temp_max, temp_min, humidade)
