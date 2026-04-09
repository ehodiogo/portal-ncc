import contador_instancias as ci

file = "Alunos CC e SI-NORMALIZADO.csv"

print(ci.headers(file))
print(ci.unique_values(file, 6))
print(ci.value_counts(file, 6)["FALECIMENTO"])