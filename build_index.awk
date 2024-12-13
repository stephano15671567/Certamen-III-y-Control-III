BEGIN {
    FS = "\\|\\|"; # Separador personalizado para campos
    salida = "custom_index.txt"; # Archivo de salida
}

{
    # Construir la URL combinando los campos iniciales
    enlace = $1;
    for (i = 2; i < NF; i++) {
        enlace = enlace "||" $i;
    }

    # Extraer el contenido de la última columna
    texto = $NF;

    # Ignorar líneas incompletas
    if (enlace == "" || texto == "") {
        next;
    }

    # Normalizar y dividir el contenido en palabras
    gsub(/[^a-zA-Z0-9 ]/, " ", texto); # Sustituir caracteres no alfanuméricos por espacios
    num_palabras = split(texto, palabras, " ");

    for (j = 1; j <= num_palabras; j++) {
        termino = tolower(palabras[j]); # Convertir a minúsculas para uniformidad

        # Filtrar palabras irrelevantes
        if (termino != "" && length(termino) > 1) {
            if (!(termino in indice)) {
                indice[termino] = enlace;
            } else if (!busca_enlace(indice[termino], enlace)) {
                indice[termino] = indice[termino] ", " enlace;
            }
        }
    }
}

function busca_enlace(cadena, enlace) {
    # Verifica si el enlace ya está en la lista
    return (index(cadena, enlace) > 0);
}

END {
    # Escribir el índice invertido en el archivo de salida
    for (termino in indice) {
        print termino ": " indice[termino] >> salida;
    }

    print "Índice generado exitosamente en: " salida;
}




















