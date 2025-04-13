import pandas as pd
from sklearn.cluster import KMeans
import joblib

def entrenar_modelo_cluster(df):
    df["hora_salida_num"] = pd.to_datetime(df["hora_salida"]).dt.hour
    X = df[["distancia_km", "hora_salida_num", "pasajeros"]]

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)

    joblib.dump(kmeans, "models/modelo_cluster.pkl")
    return kmeans

def predecir_cluster(modelo, datos_input):
    return modelo.predict([datos_input])[0]
