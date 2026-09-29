print("======================================")
print(" EJERCICIO 4 - SPLICING ALTERNATIVO")
print("======================================")


# Exones del gen original
exones = [
    "Exón 1",
    "Exón 2",
    "Exón 3",
    "Exón 4",
    "Exón 5"
]


print("\nGen original:")
print(" - ".join(exones))


# Primera isoforma: 1-2-4-5
isoforma_1 = [
    exones[0],
    exones[1],
    exones[3],
    exones[4]
]


# Segunda isoforma: 1-3-5
isoforma_2 = [
    exones[0],
    exones[2],
    exones[4]
]


print("\n--- SPLICING ALTERNATIVO ---")

print("\nIsoforma 1:")
print(" - ".join(isoforma_1))

print("\nIsoforma 2:")
print(" - ".join(isoforma_2))


print("\n--- INTERPRETACIÓN ---")

print(
    "\nLas dos isoformas contienen combinaciones diferentes de exones, "
    "por lo que generan ARNm diferentes."
)

print(
    "\nEstos ARNm pueden producir proteínas con distinta longitud, "
    "estructura y función."
)

print(
    "\nEl splicing alternativo permite que un mismo gen produzca "
    "varias proteínas sin necesidad de aumentar el número de genes."
)