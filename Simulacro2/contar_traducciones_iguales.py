# SIMULACRO PARCIAL
# Ejercicio 3
def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: int = 0
    
    for clave, traduccion in ingles.items():
        if clave in aleman.keys():
            if traduccion == aleman[clave]:
                res += 1
    
    return res

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht", "Agosto": "August", "Julio": "Juli"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand", "Julio": "July", "Agosto": "August"}

print(contar_traducciones_iguales(ingles, aleman))