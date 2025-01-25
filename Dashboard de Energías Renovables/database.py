import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="busquedas.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def conectar(self):
        """Conecta a la base de datos y crea la tabla si no existe."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS busquedas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitud REAL NOT NULL,
            longitud REAL NOT NULL,
            energia_anual REAL NOT NULL,
            fecha TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def guardar_busqueda(self, latitud, longitud, energia_anual):
        """
        Guarda una búsqueda en la base de datos.
        :param latitud: Latitud de la ubicación.
        :param longitud: Longitud de la ubicación.
        :param energia_anual: Energía anual generada (kWh).
        """
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
        INSERT INTO busquedas (latitud, longitud, energia_anual, fecha)
        VALUES (?, ?, ?, ?)
        """, (latitud, longitud, energia_anual, fecha))
        self.conn.commit()

    def obtener_busquedas(self):
        """
        Obtiene todas las búsquedas almacenadas en la base de datos.
        :return: Lista de búsquedas.
        """
        self.cursor.execute("SELECT * FROM busquedas")
        return self.cursor.fetchall()

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    db = DatabaseManager()
    db.conectar()

    # Guardar una búsqueda de ejemplo
    db.guardar_busqueda(latitud=-33.8569, longitud=151.2153, energia_anual=5000)

    # Obtener todas las búsquedas
    busquedas = db.obtener_busquedas()
    print("Búsquedas almacenadas:")
    for busqueda in busquedas:
        print(busqueda)

    db.cerrar()