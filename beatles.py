# Paso 1
beatles = []

# Paso 2

beatles.append ("John lennon")
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")

print(beatles)

# Paso 3

for i in range(2):
    nuevo_integrante = str(input("Agrege los nuevo integrante de los beatles: ")) #Pete Best y Stu Sutcliffe
    beatles.append (nuevo_integrante)

print(beatles)

# Paso 4
del beatles[3]
del beatles[3]
print(beatles)

# Paso 5
beatles.insert(0, "Ringo Star")
print(beatles)

# probando la longitud de la lista
print("Los Fav", len(beatles))