print("======================================")
print(" EJERCICIO 5 - INTRODUCCIÓN A PROTEÍNAS")
print("======================================")


# Secuencia proporcionada
proteina = [
    "Met",
    "Ile",
    "Ser",
    "Gly",
    "Val",
    "Lys",
    "His"
]


print("\nSecuencia de aminoácidos:")
print(" - ".join(proteina))


# Extremos
extremo_n = proteina[0]
extremo_c = proteina[-1]


print("\n--- EXTREMOS DE LA PROTEÍNA ---")

print("\nExtremo N-terminal:")
print(extremo_n)

print("\nExtremo C-terminal:")
print(extremo_c)


print("\n--- SECUENCIA, ESTRUCTURA Y FUNCIÓN ---")

print(
    "\nEl orden de los aminoácidos influye en las interacciones "
    "que determinan el plegamiento de la proteína."
)

print(
    "Por ello, cambios en la secuencia pueden modificar "
    "su estructura y su función."
)


print("\n--- MUTACIÓN ---")

print(
    "\nSi un aminoácido hidrofóbico situado en una región interna "
    "fuera sustituido por uno hidrofílico, podrían alterarse "
    "las interacciones responsables del plegamiento."
)

print(
    "Esto podría reducir la estabilidad de la proteína "
    "y afectar a su función."
)