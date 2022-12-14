from requests import get 
from json import dumps

API_KEY = '7b6b43b1bb33a616f913f59369510479'
dados = []

while True:
    opcao = input('Escolha uma opção: - Adicionar uma cidade na API 2 - Ver as cidades adicionadas 3 - Delete uma cidade 4 - Gerar dados das cidades 0 - Para sair Digite a opção que deseja: ')
    
    if opcao == "1":

        cidade = str(input('Digite o nome da cidade: '))
        latitude = float(input('Digite a latitude: '))
        longitude = float(input('Digite a longitude: '))
        lista = [cidade,latitude,longitude]
        dados.append(lista)
    
    elif opcao == "2":
        
        print(dados)
    
    elif opcao == "3":
        
        item = input("Digite a cidade que será retirada: ")

        for i in dados:
            for x in i:
        
                if x == item:
                
                    indice_item = dados.index(i)
                    del dados[indice_item]

        print(f'A cidade {item} foi retirada.')
        
    elif opcao == "4":
        for info in dados:
        
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[1]}&lon={info[2]}&appid={API_KEY}'   
            resposta = get(url)
    
            if resposta.status_code == 200:
                print(f'Criando arquivo: {info[0]}.json')
                with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
                    dadosjson = dumps({info[0]:resposta.json()}, indent=4) 
                    arquivo.write(dadosjson)
            else:
                print(f'Ocorreu um erro para: {info}')
                               
    elif opcao == "0":
        break
    
    else:
        print('Opção desconhecida.')