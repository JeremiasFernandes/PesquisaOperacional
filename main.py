
import pandas as pd
import requests
import json
import datetime




if __name__ == '__main__':
    distribuidoras_df = pd.read_csv("distribuidoras.csv")
    fabricas_df = pd.read_csv("fabricas.csv")

    num_amostras = 3

    fabricas = fabricas_df.sample(n=num_amostras)
    distribuidoras = distribuidoras_df.sample(n=num_amostras)
    custos = []

    for index, fabrica in fabricas.iterrows():
        aux = []
        for index2, distribuidora in distribuidoras.iterrows():
            r = requests.get(f"http://router.project-osrm.org/route/v1/car/{fabrica['longitude']},{fabrica['latitude']};{distribuidora['longitude']},{distribuidora['latitude']}?overview=false""")
            routes = json.loads(r.content)
            route_1 = routes.get("routes")[0]
            horas = "%.3f" % (route_1["duration"]/3600)
            custo_caminhoneiro = int(fabrica['horaCaminhoneiro']) * float(horas)
            distancia = route_1["distance"]/1000
            litro_diesel = distancia/2.5

            custo_viagem = litro_diesel * fabrica['diesel']
            custo_por_tonelada = custo_viagem + custo_caminhoneiro
            aux.append(custo_por_tonelada)

        custos.append(aux)









