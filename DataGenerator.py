
import random
import pandas as pd
from geopy.geocoders import Nominatim

def createDataFrame():
    fabricas = ["Rio Branco", "Maceio", "Macapa", "Manaus", "Salvador", "Fortaleza", "Vitoria", "Goiania", "São Luis",
                "Cuiaba", "Campo Grande", "Belo Horizonte", "Belem", "Joao Pessoa", "Curitiba", "Recife", "Teresina",
                "Rio de Janeiro", "Natal", "Porto Alegre", "Boa Vista", "Florianopolis", "Sao Paulo", "Aracaju", "Palmas",
                "Brasilia"]


    distribuidoras = ["Rio Branco", "Maceio", "Macapa", "Manaus", "Salvador", "Fortaleza", "Vitoria", "Goiania", "São Luis",
                "Cuiaba", "Campo Grande", "Belo Horizonte", "Belem", "Joao Pessoa", "Curitiba", "Recife", "Teresina",
                "Rio de Janeiro", "Natal", "Porto Alegre", "Boa Vista", "Florianopolis", "Sao Paulo", "Aracaju", "Palmas",
                "Brasilia","Cruzeiro do Sul", "Arapiraca", "Santana", "Parintins", "Feira de Santana", "Caucaia", "Vila Velha",
                "Aparecida de Goiânia", "Imperatriz", "Varzea Grande", "Dourados", "Uberlandia", "Ananindeua", "Campina Grande",
                "Londrina", "Joboatao dos Guararapes", "Parnaiba", "Sao Goncalo", "Mossoro", "Caxias do Sul", "Ji Parana", "Rorainopolis",
                "Florianopolis", "Nossa Senhora do Socorro", "Araguaina", "Serra"]




    dados = []

    geolocator = Nominatim(user_agent="MyApp", timeout=3)

    for fabrica in fabricas:
        aux = []
        location = geolocator.geocode(fabrica)
        aux.append(location.latitude)
        aux.append(location.longitude)
        #local da fabrica
        aux.append(fabrica)
        #capacidade
        aux.append(random.randint(5,15))
        #custo hora caminhoneiro
        aux.append(random.randint(50,80))
        #custo diesel
        aux.append(random.uniform(3.5,5.0))
        dados.append(aux)

    baseFabricas = pd.DataFrame(dados, columns=["latitude", "longitude", "cidade", "produção", "horaCaminhoneiro", "diesel"])

    dados = []

    for distribuidora in distribuidoras:
        aux = []
        #local da distribuidora
        location = geolocator.geocode(distribuidora)
        if location:
            aux.append(location.latitude)
            aux.append(location.longitude)
            aux.append(distribuidora)
            # capacidade
            aux.append(random.randint(5, 15))
            dados.append(aux)

    baseDistribuidoras = pd.DataFrame(dados, columns=["latitude", "longitude", "local", "capacidade"])

    # baseFabricas.to_csv("fabricas.csv", index=False)
    baseDistribuidoras.to_csv("distribuidoras.csv", index=False)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    createDataFrame()