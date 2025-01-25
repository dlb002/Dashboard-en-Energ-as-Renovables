import matplotlib.pyplot as plt

class VisualizacionEnergia:
    @staticmethod
    def graficar_energia_mensual(energia_mensual):
        """
        Grafica la energía generada mensual.
        :param energia_mensual: Lista con la energía generada por mes (kWh).
        """
        meses = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ]

        plt.figure(figsize=(10, 5))
        plt.bar(meses, energia_mensual, color="orange")
        plt.title("Energía Generada Mensual")
        plt.xlabel("Mes")
        plt.ylabel("Energía (kWh)")
        plt.grid(True)
        plt.show()

    @staticmethod
    def graficar_energia_anual(ac_annual):
        """
        Grafica la energía generada anual.
        :param ac_annual: Energía anual generada (kWh).
        """
        plt.figure(figsize=(6, 4))
        plt.bar(["Anual"], [ac_annual], color="green")
        plt.title("Energía Generada Anual")
        plt.ylabel("Energía (kWh)")
        plt.grid(True)
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    energia_mensual = [400, 380, 420, 450, 500, 520, 530, 510, 480, 460, 420, 400]
    ac_annual = sum(energia_mensual)

    # Graficar
    visualizacion = VisualizacionEnergia()
    visualizacion.graficar_energia_mensual(energia_mensual)
    visualizacion.graficar_energia_anual(ac_annual)