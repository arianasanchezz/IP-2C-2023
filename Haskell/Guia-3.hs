-- TUTORIAL
doubleMe :: Integer -> Integer
doubleMe x = x + x

-- GUIA PRACTICA 3 (Introduccion a Haskell)
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

-- e) Dados dos numeros racionales, decide si ambos son igualemetro (debe funcionar para elementos de cualquier tipo) s a 0
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

-- Otra forma de hacerlo usando fst y snd (hecho en Clase Práctica)
todoMenor2 :: (Float, Float) -> (Float, Float) -> Bool
todoMenor2 u v = (fst u < fst v) && (snd u < snd v)

-- c) calcula la distancia entre dos puntos de R^2
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (ax,ay) (bx,by) = sqrt ((bx-ax)^2 + (by-ay)^2)

-- d) dada una terna de enteros, calcula la suma de sus tres elementos
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a, b, c) = a + b + c

-- e) dada una terna de numeros enteros y un natural, calcula la suma de los elementos de la terna que son múltiplos del número natural
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a, b, c) n | (a `mod` n == 0) && (b `mod` n == 0) && (c `mod` n == 0) = a + b + c 
                               | (a `mod` n == 0) && (b `mod` n == 0) = a + b 
                               | (a `mod` n == 0) && (c `mod` n == 0) = a + c 
                               | (b `mod` n == 0) && (c `mod` n == 0) = b + c
                               | otherwise = 0

-- f) dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno, y devuelve 4 si son todos impares
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | x `mod` 2 == 0 = 1
                       | y `mod` 2 == 0 = 2
                       | z `mod` 2 == 0 = 3
                       | otherwise = 4

esPar :: Integer -> Bool
esPar x = (x `mod` 2 == 0)

-- Otra forma usando esPar
posPrimerPar2 :: (Integer, Integer, Integer) -> Integer
posPrimerPar2 (x, y, z) 
        | esPar x = 1
        | esPar y = 2
        | esPar z = 3
        | otherwise = 4

-- g) crea un par a partir de sus dos componentes dadas por separado (debe funcionar para elementos de cualquier tipo).
crearPar :: a -> b -> (a,b)
crearPar a b = (a, b)

-- h) invierte los elementos del par pasado como parametro (debe funcionar para elementos de cualquier tipo)
invertir :: (a,b) -> (b,a)
invertir (a, b) = (b, a)

-- EJERCICIO 5

f5 :: Integer -> Integer
f5 n | n <= 7 = n^2
     | n > 7 = (2*n - 1)

g5 :: Integer -> Integer
g5 n | esPar n = n `div` 2
     | otherwise = 3*n + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = ((f5 n1) > (g5 n1)) && ((f5 n2) > (g5 n2)) && ((f5 n3) > (g5 n3))

-- EJERCICIO 6
bisiesto :: Integer -> Bool
bisiesto n | not (n `mod` 4 == 0) = False
           | (n `mod` 100 == 0) && not (n `mod` 400 == 0) = False
           | otherwise = True

-- EJERCICIO 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1,p2,p3) (q1,q2,q3) = abs ((p1-q1) + (p2-q2) + (p3-q3))

-- EJERCICIO 8
comparar :: Integer -> Integer -> Integer
comparar a b | (sumaUltimosDosDigitos a) < (sumaUltimosDosDigitos b) = 1
             | (sumaUltimosDosDigitos a) > (sumaUltimosDosDigitos b) = (-1)
             | (sumaUltimosDosDigitos a) == (sumaUltimosDosDigitos b) = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos n = ultimoDigito n + penultimoDigito n

ultimoDigito :: Integer -> Integer
ultimoDigito n = n `mod` 10

penultimoDigito :: Integer -> Integer
penultimoDigito n = ultimoDigito (n `div` 10)

-- falta ej 9 de especificacion :)