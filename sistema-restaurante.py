print("==== Seja bem-vindo ao restaurante Panela de Ouro ====")
print("--------------------------- CARDÁPIO ---------------------------")
print("| Tamanho | Carne de Panela (CP) | Frango Grelhado (FG) |")
print("|   P     |        R$ 17.00      |        R$ 14.50       |")
print("|   M     |        R$ 19.50      |        R$ 17.50       |")
print("|   G     |        R$ 24.00      |        R$ 23.00       |")
print("----------------------------------------------------------------")

# Acumulador do valor total
total = 0
# Lista para armazenar os pedidos
pedidos = []

# Loop principal de pedidos
while True:
    # Escolha do sabor
    sabor = input("Entre com o sabor desejado (CP/FG): ").upper()

    # Validação do sabor
    if sabor not in ["CP", "FG"]:
        print("Sabor inválido. Tente novamente.")
        continue

    # Escolha do tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

    # Validação do tamanho
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue

    # Definição dos preços
    if sabor == "CP":
        if tamanho == "P":
            preco = 17.00
        elif tamanho == "M":
            preco = 19.50
        else:
            preco = 24.00
        nome_prato = "Carne de Panela"
    else:
        if tamanho == "P":
            preco = 14.50
        elif tamanho == "M":
            preco = 17.50
        else:
            preco = 23.00
        nome_prato = "Frango Grelhado"

    # Adiciona pedido à lista e soma ao total
    pedidos.append((nome_prato, tamanho, preco))
    total += preco

    print(f"Você pediu {nome_prato} no tamanho {tamanho}. Valor: R$ {preco:.2f}")

    # Verifica se o cliente deseja mais alguma coisa
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if continuar == "N":
        break

# Exibição do resumo final
print("\n====================================================")
print("                 Restaurante Panela de Ouro          ")
print("====================================================")
for prato, tam, preco in pedidos:
    print(f"- {prato} ({tam}) .......... R$ {preco:.2f}")
print("----------------------------------------------------")
print(f"TOTAL A PAGAR: .................. R$ {total:.2f}")
print("====================================================")
print("Obrigado pela preferência! Volte sempre 🍲🔥")
