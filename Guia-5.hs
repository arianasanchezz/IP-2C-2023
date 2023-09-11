-- GUIA PRACTICA 5 (Recursión sobre listas)

-- EJERCICIO 1
-- 1. dada una lista devuelve su cantidad de elementos
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- 2.
ultimo :: [t] -> t
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | otherwise = ultimo xs

-- 3.
principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x : principio xs

-- 4. resultado tiene los mismos elementos que s pero en orden inverso
reverso :: [t] -> [t]
reverso [] = []
reverso xs = ultimo xs : reverso (principio xs)

-- EJERCICIO 2
-- 1.
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys

-- 2. dada una lista devuelve verdadero sí y solamente sí todos sus elementos son iguales
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) = True
todosIguales (x:y:ys) | (x == y) && (todosIguales (y:ys)) = True
                      | otherwise = False

-- 3.
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos xs = (hayRepetidos xs) == False

-- 4.
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs


-- EJERCICIO 4 (hasta inciso 5- hechos en clase del 7/9)
-- 1. reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la segunda lista.
sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos (x:[]) = [x]
sacarEspaciosRepetidos (x:y:ys) | ((x == y) && (x == ' ')) = sacarEspaciosRepetidos (y:ys)
                                | otherwise = x : sacarEspaciosRepetidos (y:ys)

-- 2. dada una lista de caracteres devuelve la cantidad de palabras que tiene
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

-- 3. dada una lista arma una nueva lista con las palabras de la lista original
palabras :: [Char] -> [[Char]]
palabras xs = palabrasAux (listaLimpia xs)

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux (x:xs) = primeraPalabra (x:xs) : palabrasAux (sacarPrimeraPalabra (x:xs))

listaLimpia :: [Char] -> [Char]
listaLimpia xs = sacarEspacioIniFin (sacarEspaciosRepetidos xs)

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x == ' ' = []
                      | otherwise = x : primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x == ' ' = xs
                           | otherwise = sacarPrimeraPalabra xs

-- 4. dada una lista de caracteres devuelve su palabra mas larga
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAux (listaLimpia xs)

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux (x:xs) | sacarPrimeraPalabra (x:xs) == [] = primeraPalabra (x:xs)
                          | length (primeraPalabra (x:xs)) > length (primeraPalabra (sacarPrimeraPalabra (x:xs))) = primeraPalabra (x:xs)
                          | otherwise = palabraMasLargaAux xs

-- 5. a partir de una lista de palabras arma una lista de caracteres concatenandolas
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (xs:xss) = xs ++ aplanar xss

