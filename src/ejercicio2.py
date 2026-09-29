from Bio import SeqIO


print("======================================")
print(" EJERCICIO 2 - TRANSCRIPCIÓN ADN → ARN")
print("======================================")


# Lectura del archivo FASTA
registro = SeqIO.read("data/ejercicio2.fasta", "fasta")

hebra_codificante = registro.seq

# Obtenemos la hebra molde
hebra_molde = hebra_codificante.complement()


print("\nSecuencia leída desde FASTA:")
print("Identificador:", registro.id)


print("\nADN original:\n")

print("Hebra codificante:")
print("5' -", hebra_codificante, "- 3'")

print("\nHebra molde:")
print("3' -", hebra_molde, "- 5'")


# Transcripción
arnm = hebra_codificante.transcribe()


print("\n--- TRANSCRIPCIÓN ---")

print("\nARNm obtenido:")
print("5' -", arnm, "- 3'")


print("\nLa ARN polimerasa utiliza la hebra molde")
print("y sintetiza el ARNm en dirección 5' → 3'.")


print("\n--- REGIONES DEL ADN ---")

print(
    "\nLa región promotora se encuentra antes de la región transcrita "
    "y permite el inicio de la transcripción."
)

print(
    "\nLa región codificante contiene la información que puede "
    "ser traducida posteriormente a proteína."
)


# Cambio de orientación
print("\n--- CAMBIO DE ORIENTACIÓN ---")

hebra_invertida = hebra_codificante.reverse_complement()

print("\nHebra en orientación inversa:")
print("5' -", hebra_invertida, "- 3'")

arnm_invertido = hebra_invertida.transcribe()

print("\nARN obtenido con la orientación inversa:")
print("5' -", arnm_invertido, "- 3'")

print(
    "\nAl cambiar la orientación de la secuencia cambia también "
    "el ARN obtenido."
)