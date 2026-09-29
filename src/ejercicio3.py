from Bio.Seq import Seq


print("======================================")
print(" EJERCICIO 3 - TRADUCCIÓN ARN → PROTEÍNA")
print("======================================")

# ARNm proporcionado
arnm = Seq("AUGUAUGCUUAA")

print("\nARNm:")
print("5' -", arnm, "- 3'")


print("\n--- CODONES ---")

for i in range(0, len(arnm), 3):
    codon = arnm[i:i + 3]
    print(codon)


print("\nCodón de inicio: AUG")
print("Codón de parada: UAA")


# Traducción con Biopython
proteina = arnm.translate()

print("\n--- TRADUCCIÓN ---")

print("\nProteína obtenida:")
print(proteina)

print("\nM = Metionina")
print("Y = Tirosina")
print("A = Alanina")
print("* = STOP")


print("\n--- MUTACIONES ---")

print("\nMutación AUG → GUG:")
print(
    "La alteración del codón de inicio puede impedir o dificultar "
    "el inicio normal de la traducción."
)

print("\nDesaparición del codón de parada:")
print(
    "El ribosoma podría continuar traduciendo hasta encontrar "
    "otro codón de parada, produciendo una proteína más larga."
)