hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
num_replace = int(input("Escribe un numero entero: "))
hat_list[2] = num_replace

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista: " , len(hat_list))
print(hat_list)