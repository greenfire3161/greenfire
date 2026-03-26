-- database/seed_data.sql

-- 1. Insertar Configuración Inicial
INSERT INTO configuracion (usd_bna_venta, costo_descarga_champi, alquiler_fabrica, cuota_inversion_credito)
VALUES (1410.00, 750000.00, 750000.00, 2000000.00);

-- 2. Insertar Materias Primas (Costos Unitarios Netos Calculados)
-- Turba Austral: ($94.000 * 54 + $4M flete + $150k descarga) / (54 * 1800L) = 94.91
-- Perlita: ($1.6M flete / (900 bolsas * 120L)) = 14.81 (solo flete) + costo mat. prima
INSERT INTO insumos (nombre, unidad_medida, costo_neto_unidad, moneda)
VALUES 
('Turba Sphagnum Austral', 'Litro', 94.91, 'ARS'),
('Perlita Tucuman', 'Litro', 111.11, 'ARS'),
('Champicompost Crudo', 'Litro', 25.00, 'ARS'),
('Bolsa Champicompost 25L', 'Unidad', 0.378, 'USD'),
('Bolsa Premium/Grow 50L', 'Unidad', 0.498, 'USD'),
('Bolsa Premium/Grow 25L', 'Unidad', 0.369, 'USD'),
('Bolsa Industrial 80L', 'Unidad', 869.00, 'ARS');

-- 3. Insertar Productos (Basado en Lista Distribuidor Febrero)
INSERT INTO productos (nombre_producto, linea, litros_por_unidad, precio_distribuidor_neto, comision_porcentaje)
VALUES 
('Champicompost 25L', 'Champicompost', 25, 4169.88, 0.0600),
('Mix Premium 50L', 'Sustratos', 50, 11874.14, 0.0400),
('Sustrato Completo 80L', 'Sustratos', 80, 15092.00, 0.0400),
('Growlight 50L', 'Sustratos', 50, 10796.88, 0.0400),
('Huertero 50L', 'Sustratos', 50, 9332.32, 0.0400);

-- 4. Ejemplo de Receta (Mix Premium 50L - Proporción por Canchada de 400L)
-- Basado en tu Excel (Ejemplo simplificado para el seed)
INSERT INTO recetas (id_producto, id_insumo, cantidad_por_canchada)
VALUES 
(2, 1, 240.00), -- 60% Turba en 400L
(2, 2, 80.00),  -- 20% Perlita en 400L
(2, 3, 80.00),  -- 20% Champi en 400L
(2, 5, 8.00);   -- 8 bolsas de 50L por cada canchada (aprox)
