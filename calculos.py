class CalculosEnergia:
    @staticmethod
    def calcular_energia_mensual(ac_annual):
        """
        Calcula la energía generada mensual a partir de la energía anual.
        :param ac_annual: Energía anual generada (kWh).
        :return: Lista con la energía generada por mes.
        """
        # Distribución mensual aproximada (puedes ajustar estos valores según la ubicación)
        distribucion_mensual = [
            0.08,  # Enero
            0.07,  # Febrero
            0.09,  # Marzo
            0.10,  # Abril
            0.11,  # Mayo
            0.12,  # Junio
            0.12,  # Julio
            0.11,  # Agosto
            0.10,  # Septiembre
            0.08,  # Octubre
            0.07,  # Noviembre
            0.07   # Diciembre
        ]
        return [ac_annual * factor for factor in distribucion_mensual]

    @staticmethod
    def calcular_eficiencia(ac_annual, system_capacity):
        """
        Calcula la eficiencia del sistema fotovoltaico.
        :param ac_annual: Energía anual generada (kWh).
        :param system_capacity: Capacidad del sistema en kW.
        :return: Eficiencia del sistema en porcentaje.
        """
        horas_sol_equivalentes = 8760  # Horas equivalentes de sol al año
        return (ac_annual / (system_capacity * horas_sol_equivalentes)) * 100

# Ejemplo de uso
if __name__ == "__main__":
    calculos = CalculosEnergia()
    energia_mensual = calculos.calcular_energia_mensual(ac_annual=5000)  # Ejemplo: 5000 kWh anuales
    print("Energía mensual generada:", energia_mensual)

    eficiencia = calculos.calcular_eficiencia(ac_annual=5000, system_capacity=4)  # Ejemplo: 4 kW de capacidad
    print("Eficiencia del sistema:", eficiencia)