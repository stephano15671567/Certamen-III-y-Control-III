# custom_search.py - Buscador con recursividad y entrada por teclado
index_file = "custom_index.txt"

# Leer el índice invertido
def cargar_indice(file_path):
    inverted_index = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            term, urls = line.strip().split(": ", 1)
            inverted_index[term.strip()] = set(urls.strip().split(", "))
    return inverted_index

# Función recursiva para calcular la intersección
def interseccion_recursiva(sets, idx=0):
    if idx == len(sets) - 1:  # Caso base: último conjunto
        return sets[idx]
    return sets[idx] & interseccion_recursiva(sets, idx + 1)

# Main
def main():
    # Cargar índice invertido
    inverted_index = cargar_indice(index_file)
    print("Índice invertido cargado en memoria.")

    while True:
        # Leer consulta desde el teclado
        query = input("Ingrese la consulta (o 'salir' para terminar): ").strip().lower()
        if query == "salir":
            print("Saliendo del buscador.")
            break

        # Dividir la consulta en términos
        terms = query.split()

        # Verificar si los términos existen en el índice
        result_sets = []
        for term in terms:
            if term in inverted_index:
                result_sets.append(inverted_index[term])
            else:
                result_sets = []  # Si algún término no tiene resultados, no hay intersección
                break

        # Calcular intersección usando recursión
        if result_sets:
            intersection = interseccion_recursiva(result_sets)
            if intersection:
                print(f"Resultados encontrados para '{query}':")
                print(", ".join(intersection))
            else:
                print(f"No se encontraron resultados para '{query}'.")
        else:
            print(f"No se encontraron resultados para '{query}'.")

if __name__ == "__main__":
    main()
