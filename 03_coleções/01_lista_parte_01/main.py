# declaração de lista
nomes = ["fulano", "Cicrano", "beltrano", "joao", "maria", "jose"]

# exibe o primeiro nome
for nome in nomes:
    print(nome)

# ordena a lista em ordem alfabética
nomes.sort()

# re-exibe a lista em ordem alfabética
print("\nOrdem alfabetica\n")
for nome in nomes:
    print(nome)

# reverte a ordem da lista
nomes.sort(reverse=True)

print("\nOrdem alfabético reversa:\n")
for nome in nomes:
    print(nome)