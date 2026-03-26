# logic/gestion_pedidos.py

class GestionPedidos:
    def __init__(self, calculadora_rentabilidad):
        self.calc = calculadora_rentabilidad

    def registrar_pedido(self, cliente, transporte, monto_neto, flete_interno=0):
        """
        Registra un pedido evaluando si el flete interno es un riesgo.
        """
        # Alerta de Logística
        es_riesgoso = False
        if transporte.lower() in ['schneider', 'otros'] and flete_interno == 0:
            es_riesgoso = True
            mensaje_alerta = "⚠️ ALERTA: Transporte tercerizado sin flete interno cargado. ¿Quién paga el envío al depósito?"
        else:
            mensaje_alerta = "✅ Logística validada."

        return {
            "cliente": cliente,
            "transporte": transporte,
            "monto_neto": monto_neto,
            "flete_interno": flete_interno,
            "estado_pago": "Pendiente",
            "alerta": mensaje_alerta,
            "riesgo_logistico": es_riesgoso
        }

    def liquidar_comision(self, pedido, cobrado_100):
        """
        Solo permite liquidar la comisión si el cobro fue total.
        """
        if not cobrado_100:
            return "❌ Comisión NO disponible: El pago está pendiente o parcial."
        
        # Si es Champi 6%, si es Sustrato 4% (promediado para el cálculo rápido)
        # Aquí el sistema usará los porcentajes del schema.sql
        comision_estimada = pedido['monto_neto'] * 0.05 
        return f"💰 Comisión disponible para liquidar: ${round(comision_estimada, 2)}"
