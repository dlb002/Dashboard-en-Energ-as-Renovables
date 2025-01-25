import requests

class PVWattsAPI:
    def __init__(self):
        self.base_url = "https://developer.nrel.gov/api/pvwatts/v6.json"

    def get_solar_data(self, latitude, longitude):
        params = {
            "api_key": "DEMO_KEY",  # Clave de demostración (puedes obtener una propia)
            "lat": latitude,
            "lon": longitude,
            "system_capacity": 4,  # Capacidad del sistema en kW
            "azimuth": 180,        # Orientación del panel (180 = sur)
            "tilt": 20,            # Inclinación del panel
            "array_type": 1,       # Tipo de instalación (1 = fija)
            "module_type": 0,      # Tipo de módulo (0 = estándar)
            "losses": 14           # Pérdidas del sistema en %
        }
        response = requests.get(self.base_url, params=params)
        print("URL de la solicitud:", response.url)  # Para depuración
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener datos: {response.status_code}")

# Ejemplo de uso
if __name__ == "__main__":
    pvwatts = PVWattsAPI()
    data = pvwatts.get_solar_data(latitude=-33.8569, longitude=151.2153)  # Ejemplo: Sydney
    print(data)