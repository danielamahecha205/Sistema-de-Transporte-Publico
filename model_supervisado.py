import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

def entrenar_modelo_supervisado(df):
    # Codificadores
    for col in ["origen", "destino", "dia_semana", "linea", "evento"]:
        df[col + "_enc"] = LabelEncoder().fit_transform(df[col])
    
    df["hora_salida_num"] = pd.to_datetime(df["hora_salida"]).dt.hour
    
    X = df[["origen_enc", "destino_enc", "distancia_km", "hora_salida_num", "pasajeros", "dia_semana_enc", "linea_enc", "evento_enc"]]
    y = df["tiempo_est_min"]
    
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)

    joblib.dump(modelo, "models/modelo_supervisado.pkl")
    return modelo

def predecir_tiempo(modelo, datos_input):
    return modelo.predict([datos_input])[0]
