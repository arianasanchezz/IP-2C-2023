-- GUIA PRACTICA 5 (Recursion sobre listas)

-- EJERCICIO 4 (hechos en clase)
-- a)  reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la segunda lista.
sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos (x:[]) = [x]
sacarEspaciosRepetidos (x:y:ys) | ((x == y) && (x == ' ')) = sacarEspaciosRepetidos (y:ys)
                               | otherwise = x : sacarEspaciosRepetidos (y:ys)

-- b) que dada una lista de caracteres devuelve la cantidad de palabras que tiene
contarPalabras :: [Char] -> Integer
contarPalabras xs = contarEspacios(sacarEspacioIniFin (sacarEspaciosRepetidos xs)) + 1

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs

sacarEspacioIniFin :: [Char] -> [Char]
sacarEspacioIniFin [] = []
sacarEspacioIniFin (x:xs) | (x == ' ') = sacarEspacioFinal xs
                          | otherwise = x : sacarEspacioFinal xs

sacarEspacioFinal :: [Char] -> [Char]
sacarEspacioFinal [] = []
sacarEspacioFinal (x:[]) | (x == ' ') = []
                         | otherwise = [x]
sacarEspacioFinal (x:xs) = x : sacarEspacioFinal xs
