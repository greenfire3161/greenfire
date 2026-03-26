# logic/control_produccion.py

class ControlProduccion:
    def __init__(self):
        self.litros_por_canchada = 400
        self.merma_envasado = 0.05 # El 5% que definimos

    def registrar_lote(self, producto_nombre, canchadas_realizadas, litros_bolsa):
        """
        Calcula el rinde real de la producción diaria.
        """
        litros_brutos = canchadas_realizadas * self.litros_por_canchada
        litros_netos = litros_brutos * (1 - self.merma_envasado)
        
        # Unidades teóricas que deberían estar en el pallet
        unidades_estimadas = litros_netos / litros_bolsa
        
        return {
            "producto": producto_nombre,
            "litros_procesados": litros_brutos,
            "litros_reales_envasados": litros_netos,
            "unidades_teoricas": int(unidades_estimadas),
            "alerta_eficiencia": "🟢 Objetivo 6000L alcanzado" if litros_brutos >= 6000 else "🟡 Producción por debajo del objetivo diario"
        }

    def verificar_desvio(self, unidades_reales, unidades_teoricas):
        """
        Compara lo que Tobías anotó vs lo que el sistema calculó.
        """
        desvio = unidades_reales - unidades_teoricas
        if abs(desvio) > (unidades_teoricas * 0.02): # Alerta si el desvío es mayor al 2%
            return f"⚠️ Desvío detectado: {desvio} unidades de diferencia con el cálculo teórico."
        return "✅ Producción consistente."
