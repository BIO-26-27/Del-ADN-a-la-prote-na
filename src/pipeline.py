from Bio import SeqIO


print("======================================")
print(" PIPELINE - DEL ADN A LA PROTEÍNA")
print("======================================")


# ==================================================
# 1. LECTURA DEL ARCHIVO FASTA
# ==================================================

print("\n1. LECTURA DE LA SECUENCIA")
print("--------------------------")

registro = SeqIO.read("data/secuencia.fasta", "fasta")

adn = registro.seq

print("\nIdentificador:")
print(registro.id)

print("\nSecuencia de ADN:")
print("5' -", adn, "- 3'")

print("\nLongitud:")
print(len(adn), "nucleótidos")


# ==================================================
# 2. REPLICACIÓN
# ==================================================

print("\n======================================")
print("2. REPLICACIÓN DEL ADN")
print("======================================")

print("\nSeparando las hebras y generando la hebra complementaria...")

complementaria = adn.complement()

print("\nHebra original:")
print("5' -", adn, "- 3'")

print("\nNueva hebra complementaria:")
print("3' -", complementaria, "- 5'")


# Como la replicación es semiconservativa,
# se generan dos moléculas.

print("\nMolécula 1:")
print("Original: 5' -", adn, "- 3'")
print("Nueva:    3' -", complementaria, "- 5'")

print("\nMolécula 2:")
print("Original: 3' -", complementaria, "- 5'")
print("Nueva:    5' -", adn, "- 3'")

print(
    "\nLa replicación es semiconservativa: "
    "cada molécula conserva una hebra original."
)


# ==================================================
# 3. TRANSCRIPCIÓN
# ==================================================

print("\n======================================")
print("3. TRANSCRIPCIÓN ADN → ARNm")
print("======================================")

print("\nTranscribiendo el ADN...")

arnm = adn.transcribe()

print("\nADN codificante:")
print("5' -", adn, "- 3'")

print("\nCadena molde:")
print("3' -", complementaria, "- 5'")

print("\nARNm obtenido:")
print("5' -", arnm, "- 3'")

print(
    "\nDurante la transcripción, la información del ADN "
    "se copia a ARN y la timina (T) es sustituida por uracilo (U)."
)


# ==================================================
# 4. TRADUCCIÓN
# ==================================================

print("\n======================================")
print("4. TRADUCCIÓN ARNm → PROTEÍNA")
print("======================================")

print("\nPreparando el ARNm para la traducción...")


# La traducción utiliza codones completos de 3 nucleótidos.
# Si sobran 1 o 2 nucleótidos, se eliminan del final.
resto = len(arnm) % 3

if resto != 0:
    print(
        "\nLa longitud del ARNm no es múltiplo de 3."
    )

    print(
        "Se ignorarán",
        resto,
        "nucleótido(s) final(es) que no forman un codón completo."
    )

    arnm_traducible = arnm[:-resto]

else:
    arnm_traducible = arnm


print("\nARNm utilizado para traducir:")
print("5' -", arnm_traducible, "- 3'")


print("\nTraduciendo los codones a aminoácidos...")

proteina = arnm_traducible.translate()

print("\nProteína obtenida:")
print(proteina)

print(
    "\nCada grupo de tres nucleótidos forma un codón "
    "que determina un aminoácido."
)


# ==================================================
# 5. REFLEXIÓN
# ==================================================

print("\n======================================")
print("5. REFLEXIÓN")
print("======================================")

print(
    "\nLos errores que modifican de forma estable la secuencia "
    "del ADN pueden afectar a las etapas posteriores."
)

print(
    "Si una mutación modifica una región codificante, "
    "puede cambiar un codón y, en algunos casos, "
    "alterar la proteína producida."
)


# ==================================================
# 6. RESUMEN
# ==================================================

print("\n======================================")
print(" RESUMEN DEL PIPELINE")
print("======================================")

print("\nADN:")
print(adn)

print("\nHebra complementaria:")
print(complementaria)

print("\nARNm:")
print(arnm)

print("\nProteína:")
print(proteina)

print("\nPipeline finalizado correctamente.")