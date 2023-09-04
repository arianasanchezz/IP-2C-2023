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
esDivisible = undefined