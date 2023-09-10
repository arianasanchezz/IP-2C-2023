-- GUIA PRACTICA 4 (Recursion sobre números enteros)

-- Funcion de factorial hecha en clase
factorial :: Int -> Int
factorial n | n == 0 = 1
            | otherwise = n * factorial (n-1)

-- EJERCICIO 1
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | n > 1 = fibonacci (n-1) + fibonacci (n-2)

-- EJERCICIO 2
parteEntera :: Float -> Integer
parteEntera x | 0 <= x && x < 1 = 0
              | x >= 1 = 1 + parteEntera (x-1)
              | x < 0 && x >= -1 = -1
              | x < -1 = (-1) + parteEntera (x+1)

-- EJERCICIO 3
esDivisible :: Integer -> Integer -> Bool
esDivisible a b | b == 0 = False
                | a < b = False
                | a == 0 = True
                | a == b = True
                | b == 1 = True
                | b < 0 = esDivisible (a + b) b
                | otherwise = esDivisible (a - b) b

-- EJERCICIO 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 0 = 0
              | (esPar n == True) = sumaImpares (n-1)
              | otherwise = sumaImpares (n-1) + n

esPar :: Integer -> Bool
esPar x = (x `mod` 2 == 0) --no me salió todavía

-- EJERCICIO 5

-- EJERCICIO 6
sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito n + sumaDigitos (sacarUltimo n)

-- EJERCICIO 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = (ultimoDigito n == anteultimoDigito n) && todosDigitosIguales (sacarUltimo n)

--Funciones auxiliares
ultimoDigito :: Integer -> Integer
ultimoDigito x = x `mod` 10 

anteultimoDigito :: Integer -> Integer
anteultimoDigito x = (x `div` 10) `mod` 10

sacarUltimo :: Integer -> Integer
sacarUltimo x = x `div` 10

-- EJERCICIO 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | (i == cantidadDigitos n) = ultimoDigito n
                 | otherwise = iesimoDigito (sacarUltimo n) i 

cantidadDigitos :: Integer -> Integer
cantidadDigitos x | x < 10 = 1
                  | otherwise = 1 + cantidadDigitos (sacarUltimo x)

-- EJERCICIO 9 (esCapicua)

-- EJERCICIO 10
-- a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = (2 ^ n) + f1 (n-1)

-- EJERCICIO 13 (doble sumatoria, hecho en clase 7/9)
sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaInterna n m + sumatoriaInterna (n-1) m

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n m = n ^ m + sumatoriaInterna n (m-1)