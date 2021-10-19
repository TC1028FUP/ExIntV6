# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
     # Test case 1
    (
    [2, 3, 5, 18, 0, 21, -1, 7],
    ["Ingresa números positivos, para terminar de capturar ingresa un negativo",">>> ", ">>> ", ">>> ", 
    ">>> ", ">>> ", ">>> ", ">>> ", "[2, 3, 5, 18, 0, 21]", "Mayores que: ", "[18, 21]", "[2, 3, 5, 0]"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
    ["-1", "-1"],
    ["Ingresa números positivos, para terminar de capturar ingresa un negativo",">>> ","[]","Mayores que: ","Error"],
    ["Qué pasa si de entrada recibes un -1 y n no es un número positivo"]
    )
    ]
