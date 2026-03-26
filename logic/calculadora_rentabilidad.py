# logic/calculadora_rentabilidad.py

class CalculadoraGreenFire:
    def __init__(self, db_config):
        """
        db_config: Diccionario con los valores de la tabla 'configuracion'
        (usd_bna, costo_descarga_champi, alquiler, etc.)
        """
        self.usd_bna = db_config['usd_bna_venta']
        self.merma = 1.05 # 5% de merma técnica en envasado
        self.alquiler = db_config['alquiler_fabrica']
        self.credito = db_config['cuota_inversion_credito']
        self.descarga_champi = db_config['costo_descarga_champi']

    def calcular_costo_insumo(self, costo_unidad, moneda):
        """Convierte USD a ARS si es necesario"""
        if moneda == 'USD':
            return costo_unidad * self.usd_bna
        return costo_unidad

    def calcular_margen_producto(self, producto, receta_insumos):
        """
        producto: Dict con datos de la tabla 'productos'
        receta_insumos: Lista de dicts con cantidad y costo de cada insumo
        """
        # 1. Calcular Costo de Materia Prima + Packaging
        costo_total_produccion = 0
        for item in receta_insumos:
            unitario = self.calcular_costo_insumo(item['costo'], item['moneda'])
            costo_total_produccion += (item['cantidad'] * unitario)
        
        # Aplicamos la merma al costo de MP
        costo_final = costo_total_produccion * self.merma
        
        # 2. Calcular Comisión del Vendedor (sobre el Neto)
        comision = producto['precio_neto'] * producto['comision_pct']
        
        # 3. Margen de Contribución (Lo que queda para pagar la estructura)
        margen_pesos = producto['precio_neto'] - costo_final - comision
        porcentaje_margen = (margen_pesos / producto['precio_neto']) * 100
        
        return {
            "nombre": producto['nombre'],
            "costo_produccion": round(costo_final, 2),
            "comision_vendedor": round(comision, 2),
            "margen_limpio_pesos": round(margen_pesos, 2),
            "margen_porcentaje": round(porcentaje_margen, 2)
        }

    def calcular_punto_equilibrio(self, margen_promedio_por_litro):
        """
        Calcula cuántos litros hay que vender para cubrir Alquiler + Crédito + Champi
        """
        costos_fijos_totales = self.alquiler + self.credito + self.descarga_champi
        litros_necesarios = costos_fijos_totales / margen_promedio_por_litro
        return round(litros_necesarios, 2)
