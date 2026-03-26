-- 1. TABLA DE CONFIGURACIÓN (Dólar BNA y Variables Globales)
CREATE TABLE configuracion (
    id SERIAL PRIMARY KEY,
    usd_bna_venta DECIMAL(12, 2) DEFAULT 1410.00,
    costo_descarga_champi DECIMAL(12, 2) DEFAULT 750000.00,
    alquiler_fabrica DECIMAL(12, 2) DEFAULT 750000.00,
    cuota_inversion_credito DECIMAL(12, 2) DEFAULT 2000000.00,
    ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. MATERIAS PRIMAS (Insumos)
CREATE TABLE insumos (
    id_insumo SERIAL PRIMARY KEY,
    nombre VARCHAR(100), -- 'Turba Austral', 'Perlita', 'Bolsa 50L'
    unidad_medida VARCHAR(20), -- 'Litro', 'Unidad'
    costo_neto_unidad DECIMAL(12, 4), -- Costo puesto en planta (con flete y descarga)
    moneda VARCHAR(5) DEFAULT 'ARS' -- 'ARS' o 'USD'
);

-- 3. PRODUCTOS TERMINADOS (Fórmulas)
CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre_producto VARCHAR(100),
    linea VARCHAR(50), -- 'Sustratos', 'Champicompost'
    litros_por_unidad INTEGER, -- 25, 50, 80
    precio_distribuidor_neto DECIMAL(12, 2),
    comision_porcentaje DECIMAL(5, 4) -- 0.06 para Champi, 0.04 para Sustratos
);

-- 4. RECETAS POR CANCHADA (400 Litros)
CREATE TABLE recetas (
    id_receta SERIAL PRIMARY KEY,
    id_producto INTEGER REFERENCES productos(id_producto),
    id_insumo INTEGER REFERENCES insumos(id_insumo),
    cantidad_por_canchada DECIMAL(12, 4) -- Cantidad de la MP en 400L brutos
);

-- 5. MOVIMIENTOS DE PRODUCCIÓN (Tobías)
CREATE TABLE produccion_diaria (
    id_registro SERIAL PRIMARY KEY,
    id_producto INTEGER REFERENCES productos(id_producto),
    canchadas_producidas INTEGER, -- Unidad de medida de Nahuel P.
    unidades_envasadas INTEGER, -- Lo que efectivamente sale
    fecha DATE DEFAULT CURRENT_DATE,
    merma_detectada DECIMAL(5, 2) DEFAULT 5.00
);

-- 6. PEDIDOS Y LOGÍSTICA (Alejandro / Nahuel M.)
CREATE TABLE pedidos_mayoristas (
    id_pedido SERIAL PRIMARY KEY,
    cliente VARCHAR(150),
    transporte VARCHAR(100), -- 'Arias', 'Schneider', 'Propio'
    flete_interno_santafe DECIMAL(12, 2) DEFAULT 0.00, -- Lo que perdíamos con Schneider
    monto_total_neto DECIMAL(12, 2),
    estado_pago VARCHAR(20) DEFAULT 'Pendiente', -- 'Pendiente', '100%_Cobrado'
    comision_liquidada BOOLEAN DEFAULT FALSE,
    fecha_pedido DATE DEFAULT CURRENT_DATE
);
