from Bio.Seq import Seq


print("======================================")
print(" EJERCICIO 1 - REPLICACIÓN DEL ADN")
print("======================================")

# Secuencias proporcionadas en el ejercicio
hebra_1 = Seq("ATGCCGTTAGCT")
hebra_2 = Seq("TACGGCAATCGA")

print("\nADN original:\n")

print("5' -", hebra_1, "- 3'")
print("3' -", hebra_2, "- 5'")


# Generamos las nuevas hebras complementarias
nueva_hebra_1 = hebra_1.complement()
nueva_hebra_2 = hebra_2.complement()


print("\n--- REPLICACIÓN ---")

print("\nMolécula de ADN 1:")

print("Hebra original:")
print("5' -", hebra_1, "- 3'")

print("Nueva hebra:")
print("3' -", nueva_hebra_1, "- 5'")


print("\nMolécula de ADN 2:")

print("Hebra original:")
print("3' -", hebra_2, "- 5'")

print("Nueva hebra:")
print("5' -", nueva_hebra_2, "- 3'")


print("\nLa replicación es semiconservativa:")
print("cada molécula contiene una hebra original y una hebra nueva.")


print("\n--- ENZIMAS IMPLICADAS ---")

print("\nHelicasa:")
print("Separa las dos hebras del ADN.")

print("\nPrimasa:")
print("Sintetiza los cebadores necesarios para iniciar la replicación.")

print("\nADN polimerasa:")
print("Añade nucleótidos complementarios y sintetiza la nueva hebra.")

print("\nLigasa:")
print("Une los fragmentos de ADN de la hebra retardada.")


print("\n--- REFLEXIÓN ---")

print(
    "Si la ADN polimerasa cometiera un error y no se corrigiera, "
    "podría quedar fijado como una mutación en el ADN."
)