# Guia 8


# Ejercicio 2
def clonarSinComentarios(nombre_archivo: str):
    archivo = (nombre_archivo, "r")
    destino = ('sinComentarios.py', "w")

    for linea in archivo.readlines():
        if linea.strip()[0] != "#":
            destino.write(linea)

    archivo.close()
    destino.close()

# clonarSinComentarios("archivo-comentado.py")

    
    

