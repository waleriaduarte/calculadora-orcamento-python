# criando um dicionário com os tipos de adesivos e seus preços por metro quadrado
adesivos = {
    "leitoso": 70.00,
    "transparente": 75.00,
    "recorte": 90.00
}

print("Qual o tipo de adesivo?") # mostra as opções de adesivos disponibilizados por mim no dicionário
for nome in adesivos:
    print(f"- {nome.capitalize()} (R$ {adesivos[nome]:.2f} por m²)")

# pede para que o usuário insira o tipo de ades e o elemento ".lower()" coloca tudo em minusculo p/ evitar erros com letras maiusculas

escolha = input("digite o tipo de adesivo: ").lower()

if escolha in adesivos:  # verifica se o nome está disponível no nosso dicionário
    print(f"Você escolheu {escolha.capitalize()} que custa R$ {adesivos[escolha]:.2f} por m²")

    # Vamos pedir as medidas do adesivo para o usuário agora
    largura = float(input("Digite a largura em metros: "))  # input recebe os valores inseridos pelo usuário e float converte em decimal
    altura = float(input("Digite a altura em metros: "))

    # Agora o programa vai calcular o valor final que seria -> largura x altura x preço do adesivo
    preco_total = largura * altura * adesivos[escolha]

    # Exibe o preço total
    print(f"O preço total do adesivo escolhido é: R$ {preco_total:.2f}")

else:
    print("Esse adesivo não está na lista, tente novamente!")