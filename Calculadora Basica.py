import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  

    print("""\n\nInsira o tipo de cálculo:
        
    1 - Soma
    2 - Multiplicação
    3 - Divisão
    4 - Subtração
    5 - Sair\n""")

    escolha_1 = input("Digite o número na opção escolhida: ")

    if escolha_1 == '1':
        print("\n ---------- SOMA ---------- ")
        try:
            soma_1 = int(input("Insira o primeiro número: "))
            soma_2 = int(input("Insira o segundo número: "))
            total_soma = soma_1 + soma_2
            print("O Total do seu cálculo é:", total_soma)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números inteiros.")
        input("Pressione Enter para continuar...")
        
    elif escolha_1 == '2':
        print("\n ---------- MULTIPLICAÇÃO ---------- ")
        try:
            mult_1 = int(input("Insira o primeiro número: "))
            mult_2 = int(input("Insira o segundo número: "))
            total_mult = mult_1 * mult_2
            print("O Total do seu cálculo é:", total_mult)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números inteiros.")
        input("Pressione Enter para continuar...")
        
    elif escolha_1 == '3':
        print("\n ---------- DIVISÃO ---------- ")
        try:
            div_1 = float(input("Insira o dividendo: "))
            div_2 = float(input("Insira o divisor: "))
            if div_2 != 0:
                total_div = div_1 / div_2
                print("O Total do seu cálculo é:", total_div)
            else:
                print("Erro: divisão por zero não é permitida.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números válidos.")
        input("Pressione Enter para continuar...")
        
    elif escolha_1 == '4':
        print("\n ---------- SUBTRAÇÃO ---------- ")
        try:
            sub_1 = int(input("Insira o primeiro número: "))
            sub_2 = int(input("Insira o segundo número: "))
            total_sub = sub_1 - sub_2
            print("O Total do seu cálculo é:", total_sub)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números inteiros.")
        input("Pressione Enter para continuar...")
        
    elif escolha_1 == '5':
        print("Saindo do programa...")
        break  

    else:
        print("Opção inválida, tente novamente!")
        input("Pressione Enter para continuar...")
