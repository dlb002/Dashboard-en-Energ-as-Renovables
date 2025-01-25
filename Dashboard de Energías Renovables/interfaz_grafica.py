import tkinter as tk
from tkinter import messagebox
from api_client import PVWattsAPI
from calculos import CalculosEnergia
from visualizacion import VisualizacionEnergia
from database import DatabaseManager

class InterfazSolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard de Energía Solar")

        # Campo de entrada para la ubicación
        tk.Label(root, text="Latitud:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_latitud = tk.Entry(root, width=20)
        self.entrada_latitud.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Longitud:").grid(row=1, column=0, padx=10, pady=10)
        self.entrada_longitud = tk.Entry(root, width=20)
        self.entrada_longitud.grid(row=1, column=1, padx=10, pady=10)

        # Botón para calcular
        tk.Button(root, text="Calcular", command=self.calcular).grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para graficar energía mensual
        tk.Button(root, text="Graficar Mensual", command=self.graficar_mensual).grid(row=3, column=0, pady=10)

        # Botón para graficar energía anual
        tk.Button(root, text="Graficar Anual", command=self.graficar_anual).grid(row=3, column=1, pady=10)

        # Botón para ver búsquedas guardadas
        tk.Button(root, text="Ver Búsquedas", command=self.ver_busquedas).grid(row=4, column=0, columnspan=2, pady=10)

        # Variables para almacenar datos
        self.energia_mensual = None
        self.ac_annual = None
        self.db = DatabaseManager()
        self.db.conectar()

    def calcular(self):
        latitud = self.entrada_latitud.get()
        longitud = self.entrada_longitud.get()
        if not latitud or not longitud:
            messagebox.showwarning("Error", "Por favor, ingresa latitud y longitud.")
            return

        try:
            # Obtener datos de la API
            pvwatts = PVWattsAPI()
            data = pvwatts.get_solar_data(latitude=float(latitud), longitude=float(longitud))

            # Procesar datos
            self.ac_annual = data["outputs"]["ac_annual"]  # Energía anual en kWh
            system_capacity = 4  # Capacidad del sistema en kW (ajusta según sea necesario)

            # Calcular energía mensual y eficiencia
            calculos = CalculosEnergia()
            self.energia_mensual = calculos.calcular_energia_mensual(self.ac_annual)
            eficiencia = calculos.calcular_eficiencia(self.ac_annual, system_capacity)

            # Guardar la búsqueda en la base de datos
            self.db.guardar_busqueda(latitud=float(latitud), longitud=float(longitud), energia_anual=self.ac_annual)

            # Mostrar resultados en un mensaje
            resultados = (
                f"Energía generada anual: {self.ac_annual:.2f} kWh\n"
                f"Energía generada mensual: {[f'{x:.2f} kWh' for x in self.energia_mensual]}\n"
                f"Eficiencia del sistema: {eficiencia:.2f}%"
            )
            messagebox.showinfo("Resultados", resultados)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def graficar_mensual(self):
        if self.energia_mensual is None:
            messagebox.showwarning("Error", "Primero calcula la energía generada.")
            return
        visualizacion = VisualizacionEnergia()
        visualizacion.graficar_energia_mensual(self.energia_mensual)

    def graficar_anual(self):
        if self.ac_annual is None:
            messagebox.showwarning("Error", "Primero calcula la energía generada.")
            return
        visualizacion = VisualizacionEnergia()
        visualizacion.graficar_energia_anual(self.ac_annual)

    def ver_busquedas(self):
        """Muestra las búsquedas almacenadas en la base de datos."""
        busquedas = self.db.obtener_busquedas()
        if not busquedas:
            messagebox.showinfo("Búsquedas", "No hay búsquedas almacenadas.")
            return

        # Formatear las búsquedas para mostrarlas en un mensaje
        resultados = "Búsquedas almacenadas:\n\n"
        for busqueda in busquedas:
            resultados += (
                f"ID: {busqueda[0]}\n"
                f"Latitud: {busqueda[1]}\n"
                f"Longitud: {busqueda[2]}\n"
                f"Energía Anual: {busqueda[3]:.2f} kWh\n"
                f"Fecha: {busqueda[4]}\n\n"
            )
        messagebox.showinfo("Búsquedas", resultados)

    def __del__(self):
        """Cierra la conexión a la base de datos al cerrar la aplicación."""
        if hasattr(self, "db"):
            self.db.cerrar()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSolar(root)
    root.mainloop()