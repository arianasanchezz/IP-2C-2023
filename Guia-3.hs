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
                   | absoluto y > absoluto x = y

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
