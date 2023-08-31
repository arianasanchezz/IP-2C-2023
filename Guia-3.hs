-- TUTORIAL
doubleMe :: Integer -> Integer
doubleMe x = x + x

-- EJERCICIO 1
-- a)
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

-- EJERCICIO 2
-- a) Calcula el valor absoluto de un número entero
absoluto :: Integer -> Integer
absoluto n = abs n

-- b) Devuelve el maximo entre el valor absoluto de dos numeros enteros
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | absoluto x >= absoluto y = x
                   | absoluto y >= absoluto x = y

-- c) Devuelve el maximo entre tres numeros enteros
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | maximoAbsoluto x y > z = maximoAbsoluto x y
              | otherwise = z

-- d) Dados dos numeros racionales, decide si alguno de los dos es igual a 0
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False

-- Con pattern matching:
algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 _ = True
algunoEs0PM _ 0 = True
algunoEs0PM _ _ = False

-- e) Dados dos numeros racionales, decide si ambos son iguales a 0
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y | x == 0 && y == 0 = True
              | otherwise = False

-- Con pattern matching:
ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False

-- f) Dados dos numeros reales, indica si pertenecen al mismo intervalo (−∞, 3], (3, 7] y (7, ∞)
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y | (x <= 3 && y <= 3) = True
                   | (3 < x && x < 8) && (3 < y && y < 8) = True
                   | (x > 7 && y > 7) = True
                   | otherwise = False

-- g) Dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera)
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && y == z = 0
                    | x == y = z
                    | x == z = y
                    | y == z = x

-- h) Dados dos numeros naturales, decidir si el primero es multiplo del segundo
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | x `mod` y == 0 = True
                 | otherwise = False

-- i) Dado un numero natural, extrae su digito de las unidades
digitoUnidades :: Int -> Int
digitoUnidades x | x < 0 = ((-1) * x) `mod` 10
                 | otherwise = x `mod` 10

-- j) Dado un numero natural, extrae su digito de las decenas
digitoDecenas :: Int -> Int
digitoDecenas x | x < 0 = (((-1) * x) `div` 10) `mod` 10
                | otherwise = (x `div` 10) `mod` 10

-- EJERCICIO 3
-- problema estanRelacionados (a:Z, b:Z) : Bool {
-- requiere: {a 6= 0 ∧ b 6= 0}
-- asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k /= 0)}
-- }

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = undefined

-- EJERCICIO 4
-- a) calcula el producto interno entre dos tuplas R × R
productoInterno :: (Integer, Integer) -> (Integer, Integer) -> Integer
productoInterno (a1, a2) (b1, b2) = a1 * b1 + a2 * b2

-- EJEMPLO DE CLASE TEORICA 31/8
sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresHasta n n

sumaDivisoresHasta :: Integer -> Integer -> Integer
sumaDivisoresHasta n 1 = 1
sumaDivisoresHasta n i | (n `mod` i == 0) = i + sumaDivisoresHasta n (i-1)
                       | otherwise = sumaDivisoresHasta n (i-1)

-- cont. Ej 4)
-- b) dadas dos tuplas R×R, decide si es cierto que cada coordenada de la primera tupla es menor a la coordenada 
-- correspondiente de la segunda tupla
todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor (ax,ay) (bx,by) | (bx > ax) && (by > ay) = True
                          | otherwise = False

-- c) calcula la distancia entre dos puntos de R^2
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (ax,ay) (bx,by) = sqrt ((bx-ax)^2 + (by-ay)^2)