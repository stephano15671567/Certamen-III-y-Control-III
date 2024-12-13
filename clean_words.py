import re

# Lista de palabras no deseadas
unwanted_terms = [
    "a", "an", "the", "and", "or", "but", "if", "while", "to", "in", "out", "on", "at", "by", "with", "for", "from", "as", "is", "are", "be", "been", "being", "was", "were", "will", "would", "should", "could", "may", "might", "must"
]

input_path = "new_inverted_index.txt"
output_path = "clean_index.txt"
log_path = "filter_log.txt"

def filter_terms(line, terms_to_filter):
    elements = re.split(r'\W+', line)
    return ' '.join([element for element in elements if element.lower() not in terms_to_filter])

with open(input_path, 'r') as infile, open(output_path, 'w') as outfile, open(log_path, 'w') as log:
    for line in infile:
        if any(term in line.lower() for term in unwanted_terms):
            log.write(f"Removed: {line}")
        else:
            filtered_line = filter_terms(line, unwanted_terms)
            outfile.write(filtered_line + '\n')

print(f"Proceso de limpieza completado. Archivo de salida: {output_path}, Log: {log_path}")
