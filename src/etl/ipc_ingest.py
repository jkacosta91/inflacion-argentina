import pandas as pd
import requests
import os

# 🟡 Leer archivo CSV desde carpeta ETL
def cargar_series_desde_archivo(archivo_csv):
    if not os.path.exists(archivo_csv):
        print(f"❌ Archivo inexistente: {archivo_csv}")
        return None
    return pd.read_csv(archivo_csv)

# 🟡 Descargar una serie por ID
def descargar_serie(id_serie, desde, hasta):
    base_url = "https://apis.datos.gob.ar/series/api/series"
    params = {
        "ids": id_serie,
        "start_date": desde,
        "end_date": hasta,
        "format": "json"
    }
    print(f">> 📦 Descargando: {id_serie}")
    r = requests.get(base_url, params=params)
    if r.status_code != 200:
        print(f"⚠️  Error HTTP: {r.status_code}")
        return None
    data = r.json()
    if 'data' not in data:
        print(f"⚠️  Serie fallida o inexistente: {id_serie}")
        return None
    df = pd.DataFrame(data['data'], columns=['periodo', id_serie])
    df['periodo'] = pd.to_datetime(df['periodo'])
    return df

# 🟢 Script principal
def main():
    print("📥 Iniciando descarga de series económicas...\n")

    # Ruta del archivo de entrada
    archivo = os.path.join("etl", "archivo_series.csv")

    # Ruta del archivo de salida
    archivo_salida = os.path.join("data", "datos_macro.csv")

    # Leer archivo
    series_info = cargar_series_desde_archivo(archivo)
    if series_info is None:
        return

    df_final = None
    id_to_nombre = {}

    for _, row in series_info.iterrows():
        id_serie, desde, hasta, nombre = row
        df = descargar_serie(id_serie, desde, hasta)
        if df is not None:
            df.rename(columns={id_serie: nombre}, inplace=True)
            id_to_nombre[id_serie] = nombre
            if df_final is None:
                df_final = df
            else:
                df_final = pd.merge(df_final, df, on='periodo', how='outer')

    if df_final is not None:
        df_final.sort_values(by='periodo', inplace=True)
        print("\n✅ Datos combinados correctamente:")
        print(df_final.head())

        # Guardar en carpeta data
        os.makedirs("data", exist_ok=True)
        df_final.to_csv(archivo_salida, index=False)
        print(f"📁 Archivo guardado como {archivo_salida}")
    else:
        print("⚠️  No se pudo obtener ninguna serie.")

if __name__ == "__main__":
    main()
