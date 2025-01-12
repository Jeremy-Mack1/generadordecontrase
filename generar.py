import random
import string

def generar_contrasena(longitud=12):
    # Definir los posibles caracteres para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar una contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

# Llamada a la función para generar una contraseña de 12 caracteres
contrasena_segura = generar_contrasena(12)
print("Contraseña segura generada:", contrasena_segura)
