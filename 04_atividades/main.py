    # TODOS: atividade

try:
    #entrada de dados
    nome = input("informe o seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())

    # lista de filmes
    Sala_1 = "A Roda Quadrada"
    Sala_2 = "A Volta dos Que Não Foram"
    Sala_3 = "Poeira em Alto Mar"
    Sala_4 = "As Tranças do Rei Careca"
    Sala_5 = "A Vingança do Frango Assado"

    #loop
    while True:
    #menu de filmes
        print(f"sala 1 {Sala_1} - livre")
        print(f"sala 2 {Sala_2} - 12 anos")
        print(f"sala 3 {Sala_3} - 14 anos")
        print(f"sala 4 {Sala_4} - 16 anos")
        print(f"sala 5 {Sala_5} - 18 anos")
        sala = input("informe a sala desejada").strip()

        # verifica a sala selecionada
        match sala:
            case "1":
                filme = Sala_1
                idade_minima = 0
            case "2":
                filme = Sala_2
                idade_minima = 12
            case "3":
                filme = Sala_3
                idade_minima = 14
            case "4":
                filme = Sala_4
                idade_minima = 16
            case "5":
                filme = Sala_5
                idade_minima = 18
            case _:
                print("sala inexistente.")
        if idade  >= idade_minima:
            print(f"{nome} escolheu {filme}. tenha um bom filme!")
            break
        else:
            print(f"{nome} não foi autorizado a ver{filme}.")
            continue
except Exception as e:
    print(f"erro no programa. {e}")








"""
Crie um programa que recebe do usuário o nome e a idade, e em seguida, exiba na tela uma lista de filmes, suas respectivas salas e classificações indicativas:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Frango Assado - 18 anos
O usuário deverá escolher o filme, e caso ele tiver a idade mínima para ver o filme, imprime o ingresso e encerra o programa. Caso o usuário não tenha a idade mínima, o programa impede a entrada do usuário e re-exibe a lista de filmes para que o mesmo escolha outro filme.
"""