# EJERCICIO 3
# Carreras de caballos

def carreras_de_caballos(caballos: list, carreras: dict) -> dict:
    res = {}
    for caballo in caballos:
        res[caballo] = [0]*len(caballos)
    
    for i in range(0, len(caballos), 1):
        for caballo, posiciones in res.items():
            for carrera, resultados in carreras.items():
                if caballo == resultados[i]:
                    posiciones[i] += 1
    
    return res


caballos = ['rayo', 'pepe', 'lolo', 'mengana']
carreras = {'carreras1': ['rayo', 'lolo', 'mengana', 'pepe'],
            'carreras2': ['lolo','mengana', 'rayo', 'pepe']}
print(carreras_de_caballos(caballos, carreras))