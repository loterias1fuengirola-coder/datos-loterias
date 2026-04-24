import requests
import json
import os

# Configuramos la extracción (Ejemplo Bonoloto)
url = "https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=BONO&fechaInicioInclusiva=20260410&fechaFinInclusiva=20260410"

headers = {"User-Agent": "Mozilla/5.0"}

def extraer():
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data:
            # Simplificamos el JSON para tu web
            resultado = {
                "fecha": data[0]['fecha_sorteo'],
                "combinacion": data[0]['combinacion'],
                "complementario": data[0]['complementario'],
                "reintegro": data[0]['reintegro'],
                "premios": data[0]['escrutinio']
            }
            
            # Guardamos el archivo
            with open("bonoloto.json", "w", encoding="utf-8") as f:
                json.dump(resultado, f, indent=4, ensure_ascii=False)
            print("Archivo bonoloto.json generado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extraer()
