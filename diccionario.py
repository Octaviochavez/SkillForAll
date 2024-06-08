""""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprimir valores aquí.
print(dictionary['cat'])
print(phone_numbers['Suzy'])
"""
"""
dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
"""
# Ejemplo 1:
#Sangria francesa
"""
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}
"""
#Funcion .key 
"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
"""
#Funcion .items
"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)
"""
#Cambiar, modificar o eliminar  valores

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'

print(dictionary)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.update({"pato": "canard"}) 
print(dictionary)

#Funcion .values()
"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for french in dictionary.values():
    print(french)
"""