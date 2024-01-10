# solicitar al usuario que ingrese el nombre de un elemento quimico de la tabla periodica
elemento = input("Transcribir el nombre de un elemento quimico de la tabla periódica: ")

# creamos un diccionario con los numeros atomicos de algunos elementos que vamos a utilizar como lo son, metales alcalinos, metales alcalinoterreo, halogeno y gases nobles
numeros_atomicos = {
    "hidrogeno": 1,
    "litio": 3,
    "berilio": 4,
    "sodio": 11,
    "magnesio": 12,
    "potasio": 19,
    "calcio": 20,
    "rubidio": 37,
    "estroncio": 38,
    "cesio": 55,
    "bario": 56,
    "francio": 87,
    "radio": 88,
    "fluor": 9,
    "cloro": 17,
    "bromo": 35,
    "yodo": 53,
    "astato": 85,
    "helio": 2,
    "neon": 10,
    "argon": 18,
    "cripton": 36,
    "xenon": 54,
    "radon": 86
}

# creamos una lista con los nombres de los metales alcalinos
metales_alcalinos = ["litio", "sodio", "potasio", "rubidio", "cesio", "francio"]

# creanos una lista con los nombres de los metales alcalinoterreos
metales_alcalinoterreos = ["berilio", "magnesio", "calcio", "estroncio", "bario", "radio"]

# creamos una lista con los nombres de los halogenos
halogenos = ["fluor", "cloro", "bromo", "yodo", "astato"]

# creamos una lista con los nombres de los gases nobles
gases_nobles = ["helio", "neon", "argon", "cripton", "xenon", "radon"]

# calculamos la masa atomica segun el tipo de elemento
if elemento in numeros_atomicos: 

# Verificamos si el elemento esta en el diccionario que creamos
    numero_atomico = numeros_atomicos[elemento] 

# si el elemento está en la lista, obtendremos el numero atomico del diccionario
    if elemento in metales_alcalinos: 

# Verificamos si el elemento es un metal alcalino y le asignamos la masa atomica que corresponde
        masa_atomica = 23
        
    elif elemento in metales_alcalinoterreos: 
 # Verificamos si el elemento es un metal alcalinoterreo y le asignamos la masa atomica que corresponde
        masa_atomica = 24
        
    elif elemento in halogenos: 
 
 # Verificamos si el elemento es un halogeno y le asignamos la masa atomica que corresponde
        masa_atomica = 35
        
    elif elemento in gases_nobles: 
    
 # Verificamos si el elemento es un gas noble y le asignamos la masa atomica que corresponde
        masa_atomica = 40
        
    else: # En cualquier otro caso si no aparece en nuestro diccionario entonces mostramos que la masa atómica es desconocida
        masa_atomica = "desconocida"
        
    print(f"El elemento {elemento} tiene un numero atomico de {numero_atomico} y una masa atomica de {masa_atomica}u.")
    
else: 
    print(f"El elemento {elemento} no aparece en nuestra base de datos.")
