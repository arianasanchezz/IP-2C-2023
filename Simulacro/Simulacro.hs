-- SIMULACRO
-- EJERCICIO 1
relacionesValidas :: [([Char], [Char])] -> Bool -- no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar el orden)
relacionesValidas [x] = not (relacionInvalida x)
relacionesValidas (x:y:xs) | not (perteneceRel x (y:xs)) && not (relacionInvalida x) = relacionesValidas (y:xs)
                           | otherwise = False

tuplasIguales :: ([Char], [Char]) -> ([Char], [Char]) -> Bool -- comprueba tuplas repetidas
tuplasIguales (a1,a2) (b1,b2) | (a1 == b1) && (a2 == b2) = True
                              | (a1 == b2) && (a2 == b1) = True
                              | otherwise = False

relacionInvalida :: ([Char], [Char]) -> Bool -- comprueba tuplas con ambas componentes iguales
relacionInvalida (x1, x2) = (x1 == x2)

perteneceRel :: ([Char], [Char]) -> [([Char],[Char])] -> Bool -- pertenece para relaciones
perteneceRel (_,_) [] = False
perteneceRel x (y:ys) | tuplasIguales x y = True
                      | otherwise = perteneceRel x ys

-- EJERCICIO 2
personas :: [([Char], [Char])] -> [[Char]] -- resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en cualquiera de las dos posiciones, sin repetir
personas [] = []
personas ((a1,a2):xs) | not (pertenece a1 (personas xs)) && not (pertenece a2 (personas xs)) = [a1,a2] ++ personas xs
                      | not (pertenece a1 (personas xs)) = a1 : personas xs
                      | not (pertenece a2 (personas xs)) = a2 : personas xs
                      | otherwise = personas xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys

-- EJERCICIO 3
amigosDe :: [Char] -> [([Char], [Char])] -> [[Char]] -- resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las componentes es persona
amigosDe _ [] = []
amigosDe p xs = relacionadosCon p (relacionesDondeEsta p xs)

relacionesDondeEsta :: [Char] -> [([Char], [Char])] -> [([Char], [Char])] -- devuelve la lista de relaciones en las que aparece la persona
relacionesDondeEsta _ [] = []
relacionesDondeEsta p ((p1,p2):xs) | (p == p1) || (p == p2) = (p1,p2) : relacionesDondeEsta p xs
                                   | otherwise = relacionesDondeEsta p xs

amigoDe :: [Char] -> ([Char], [Char]) -> [Char] -- dada una relación donde aparece la persona, me devuelve a su amigo
amigoDe p (p1,p2) | (p == p1) = p2
                  | otherwise = p1

relacionadosCon :: [Char] -> [([Char], [Char])] -> [[Char]] -- devuelve la lista de los amigos que tiene la persona
relacionadosCon _ [] = []
relacionadosCon p ((p1,p2):xs) = amigoDe p (p1,p2) : relacionadosCon p xs

-- EJERCICIO 4
personaConMasAmigos :: [([Char], [Char])] -> [Char] -- resu es el Strings que aparece mas veces en las tuplas de relaciones (o alguno de ellos si hay empate)
personaConMasAmigos = undefined

cantidadDeAmigos :: [Char] -> [([Char],[Char])] -> Integer
cantidadDeAmigos p xs = longitud (amigosDe p xs)

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- Ejemplos

usuario1 = "Juan"
usuario2 = "Natalia"
usuario3 = "Pedro"
usuario4 = "Lionel"
usuario5 = "Andres"

relacion1_2 = (usuario1, usuario2)
relacion1_1 = (usuario1, usuario1)
relacion1_3 = (usuario1, usuario3)
relacion2_3 = (usuario3, usuario2)
relacion1_4 = (usuario4, usuario1)
relacion2_4 = (usuario2, usuario4)
relacion1_5 = (usuario1, usuario5)

listaDeRelaciones = [relacion1_2, relacion1_3]
listaDeRelaciones2 = [relacion1_3, relacion2_3, relacion1_4]
listaDeRelaciones3 = [relacion1_2, relacion1_3, relacion1_4, relacion1_5, relacion2_3, relacion2_4]
listaDeRelacionesInvalida = [relacion1_2, relacion1_3, relacion1_2]
listaDeRelacionesInvalida2 = [relacion1_2, relacion1_3, relacion1_1]