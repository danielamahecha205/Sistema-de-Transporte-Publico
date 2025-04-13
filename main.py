import pandas as pd
from models.model_supervisado import entrenar_modelo_supervisado, predecir_tiempo
from models.model_cluster import entrenar_modelo_cluster, predecir_cluster
import joblib

# Cargar datos
df = pd.read_csv("data/transmilenio_viajes.csv")

# Entrenar y guardar modelos (solo una vez)
modelo_sup = entrenar_modelo_supervisado(df)
modelo_cluster = entrenar_modelo_cluster(df)

# Ejemplo de entrada nueva
nueva_ruta = {
    "origen_enc": 2,
    "destino_enc": 5,
    "distancia_km": 7,
    "hora_salida_num": 8,
    "pasajeros": 100,
    "dia_semana_enc": 1,
    "linea_enc": 0,
    "evento_enc": 0
}
input_sup = list(nueva_ruta.values())

tiempo_estimado = predecir_tiempo(modelo_sup, input_sup)
print(f"🕒 Tiempo estimado de viaje: {tiempo_estimado:.2f} minutos")

# Cluster de este viaje
input_cluster = [7, 8, 100]  # distancia, hora, pasajeros
grupo = predecir_cluster(modelo_cluster, input_cluster)
print(f"📊 Este viaje pertenece al grupo (cluster): {grupo}")
