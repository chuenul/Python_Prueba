print("ejemplo 1")
hola = ' \t\t\n\tHola \n '
print(hola) 
hola_limpio = hola.strip()
print(hola_limpio)

print("ejemplo 2")
texto = ' hola mundo hola \ni'
print(texto.strip(' oahl'))
 
print(texto.strip(' \nioahl'))

print("ejemplo 3")
hola = ' hola '
print(hola.rstrip())
#' hola'
print(hola.lstrip())
#'hola '
