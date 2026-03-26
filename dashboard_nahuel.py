# dashboard_nahuel.py
from logic.calculadora_rentabilidad import CalculadoraGreenFire
from logic.gestion_pedidos import GestionPedidos
from logic.control_produccion import ControlProduccion

# 1. SIMULACIÓN DE DATOS DE CONFIGURACIÓN (Lo que vendría de la DB)
config_actual = {
    'usd_bna_venta': 1410.00,
    'costo_descarga_champi': 750000.00,
    'alquiler_fabrica': 750000.00,
    'cuota_inversion_credito': 2000000.00
}

# 2. INICIALIZACIÓN DE MOTORES
calc = CalculadoraGreenFire(config_actual)
ventas = GestionPedidos(calc)
fabrica = ControlProduccion()

def generar_reporte_gerencial():
    print("--- 🌿 REPORTE DE GESTIÓN GREEN FIRE ---")
    
    # Ejemplo: Rentabilidad de Mix Premium 50L
    # Datos de la "Canchada" del Excel (simplificado para el reporte)
    receta_mix = [
        {'cantidad': 30, 'costo': 94.91, 'moneda': 'ARS'}, # Turba
        {'cantidad': 10, 'costo': 25.00, 'moneda': 'ARS'}, # Champi
        {'cantidad': 10, 'costo': 111.11, 'moneda': 'ARS'}, # Perlita
        {'cantidad': 1, 'costo': 0.498, 'moneda': 'USD'}   # Bolsa
    ]
    
    prod_info = {
        'nombre': 'Mix Premium 50L',
        'precio_neto': 11874.14, # Precio Distribuidor
        'comision_pct': 0.04     # 4%
    }
    
    analisis = calc.calcular_margen_producto(prod_info, receta_mix)
    
    print(f"\nANÁLISIS DE PRODUCTO: {analisis['nombre']}")
    print(f" > Costo Producción: ${analisis['costo_produccion']}")
    print(f" > Comisión Vendedor: ${analisis['comision_vendedor']}")
    print(f" > MARGEN NETO REAL: ${analisis['margen_limpio_pesos']} ({analisis['margen_porcentaje']}%)")

    # Ejemplo de Producción Diaria
    reporte_fabrica = fabrica.registrar_lote("Mix Premium 50L", 15, 50)
    print(f"\nESTADO DE FÁBRICA (HOY):")
    print(f" > Litros Procesados: {reporte_fabrica['litros_procesados']}L")
    print(f" > Unidades Teóricas en Pallet: {reporte_fabrica['unidades_teoricas']}")
    print(f" > {reporte_fabrica['alerta_eficiencia']}")

    # Punto de Equilibrio (Simulado con margen promedio)
    margen_promedio_litro = analisis['margen_limpio_pesos'] / 50
    litros_pe = calc.calcular_punto_equilibrio(margen_promedio_litro)
    print(f"\nMETAS FINANCIERAS:")
    print(f" > Punto de Equilibrio Mensual: {litros_pe} litros.")
    print(f" > Equivalente a: {round(litros_pe / 50)} bolsas de 50L.")

if __name__ == "__main__":
    generar_reporte_gerencial()
