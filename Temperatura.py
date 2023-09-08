import pandas as pd
import requests

df = pd.read_csv('Local.csv') #carrega os dados
api_key = '2868bf4953a28e273c2128d10d8da3ed' #key da api Openweather


#Capitura os dados da Api
def get_local(lat,long,key):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&lang=pt_br&appid={key}')
        return response.json() if response.status_code == 200 else None

#Cria colunas para preencher posteriormente
df['Cidade']= None
df['Temperatura'] = None


# intera sobre o df, capitura a latitude e longitude do local de acordo com o index e atualiza o df
for i,latitude in enumerate(df['Latitude']):

    longitude = df.loc[i,'Longitude']
    local= get_local(latitude,longitude,api_key)

    temperatura = round((local['list'][0]['main']['temp']) - 273.15, 2) #captura a temperatura e converte para °C
    city = local ['city']['name']

    df.loc[df['Latitude'] == latitude , 'Cidade'] = city
    df.loc[df['Latitude'] == latitude , 'Temperatura'] = temperatura

print(df)
#df.to_csv('Temperaturas.csv', index=False)