module Solucion where

-- Ejercicio 1
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int  -> Float
porcentajeDeVotosAfirmativos formulas listaVotos votosTotal = (division (votosNoBlancos listaVotos) votosTotal) * 100

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

votosNoBlancos :: [Int] -> Int
votosNoBlancos[] = 0
votosNoBlancos (v:vs) = v + votosNoBlancos vs

-- Ejercicio 2
formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas [x] = (componentesIguales x)
formulasInvalidas (x:xs) | not (componentesIguales x) && not (perteneceFormulas x xs) = formulasInvalidas xs
                         | otherwise = True

componentesIguales :: (String, String) -> Bool
componentesIguales (x,y) = (x == y)

candidatoRepetido :: (String, String) -> (String, String) -> Bool
candidatoRepetido (a1,a2) (b1,b2) | a1 == b1 || a1 == b2 = True
                                  | a2 == b1 || a2 == b2 = True
                                  | otherwise = False

perteneceFormulas :: (String, String) -> [(String, String)] -> Bool
perteneceFormulas _ [] = False
perteneceFormulas formula (f:fs) | (candidatoRepetido formula f) = True
                                 | otherwise = perteneceFormulas formula fs

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos vice formulas votos = division (votosDelVice vice (votosDeVices formulas votos)) (votosNoBlancos votos) * 100

votosDeVices :: [(String, String)] -> [Int] -> [(String, Int)]
votosDeVices [] _ = []
votosDeVices (f:fs) (v:vs) = (snd f, v) : votosDeVices fs vs

votosDelVice :: String -> [(String, Int)] -> Int
votosDelVice _ [] = 0
votosDelVice vice ((v,cant):fs) | vice == v = cant 
                                | otherwise = votosDelVice vice fs

-- Ejercicio 4
menosVotado :: [(String, String)] -> [Int] -> String
menosVotado formulas votos = fst (compararMinimo (votosDeFormula formulas votos))

votosDeFormula :: [(String, String)] -> [Int] -> [((String, String), Int)]
votosDeFormula [] _ = []
votosDeFormula (f:fs) (v:vs) = (f,v) : votosDeFormula fs vs

compararMinimo :: [((String, String), Int)] -> (String, String)
compararMinimo [x] = fst x
compararMinimo (((pres1,vice1),cant1):((pres2,vice2),cant2):xs) | cant1 < cant2 = compararMinimo (((pres1,vice1),cant1):xs)
                                                                | otherwise = compararMinimo (((pres2,vice2),cant2):xs)