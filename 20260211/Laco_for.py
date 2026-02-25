frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

print("Início da lista de frutas.")
for fruta in frutas:
    print(f"Eu gosto de {fruta}.")
print("Fim da lista de frutas.")

texto = "TeStE"

print(texto.upper())
print(texto.lower())
print(texto.capitalize())

frutas.sort()
print(frutas)

frutas.sort(reverse=True)
print(frutas)

print("Início da lista de frutas, pulando a banana.")
for fruta in frutas:
    if fruta == "banana":
        continue
    print(f"Eu gosto de {fruta}.")
print("Fim da lista de frutas.")

print("Início da lista de frutas, parando na uva.")
for fruta in frutas:
    if fruta == "uva":
        break
    print(f"Eu gosto de {fruta}.")
print("Fim da lista de frutas.")
