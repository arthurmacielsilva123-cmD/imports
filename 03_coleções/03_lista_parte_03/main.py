# Biblioteca
import os

# declaração de lista
nomes = []

#limpa o console
os.system("cls")


# loop
while True:
    #menu
    print("1 - inserir novo nome")
    print("2 - exibir lista de nomes")
    print("3 - Excluir nome da lista")
    print("4 - sair do programa")
    opcao = input("informe a opçao desejada: ").strip()
    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("informe o novo nome: ").strip().title()
            nomes.append(novo_nome) # insere novo nome na lista
            os.system("cls")
            print(f"{novo_nome} cadastro com sucesso")
        case "2":
             os.system("cls")
             print("lista de nomes\n")
             for i in range (len(nomes)):     # FIXME
                  print(f"{i} - {nomes[i]}")
             print(f"\n{'-'*40}\n")
             continue
        case "3":
            try:
                posicao = int(input("informe a posição a ser exluida: ").strip())
                if posicao >= 0 and posicao < len(nomes):
                     del(nomes[posicao])
                     print("nome excluido com sucesso.")
                else:
                     print("Posição inexistente.")
            except Exception as e:
                 print(f"Posição inválida. {e}.")
            continue
        case "4":
             print("programa encerrado.")
             break
        case _:
             pass