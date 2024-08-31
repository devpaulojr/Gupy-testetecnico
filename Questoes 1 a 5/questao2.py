lista_maisculo = []  # lista para 'A' maiúsculo
lista_minusculo = []  # lista para 'a' minúsculo

frase_usuario = str(input("Digite uma frase qualquer: "))

quantidade_A = frase_usuario.count("A")
quantidade_a = frase_usuario.count("a")

if quantidade_A > 0:
    lista_maisculo.extend(["A"] * quantidade_A) # replica a quantidade de 'A' na frase do usuario

if quantidade_a > 0:
    lista_minusculo.extend(["a"] * quantidade_a) # replica a quantidade de 'a' na frase do usuario

print("A quantidade de letras 'A' maiúsculas é: ", len(lista_maisculo))

print("A quantidade de letras 'a' minúsculas é: ", len(lista_minusculo))