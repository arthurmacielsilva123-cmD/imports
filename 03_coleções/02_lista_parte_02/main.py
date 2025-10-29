#declaração de lista
nomes = []

try: 
    while True:
        print("1 - inserir nome na lista\n")
        print("2 - exibir lista\n")
        print("3 - sair do programa\n")
        opção = input("informe a opção desejada\n").strip()
        match opção:
            case "1":
                 novo_nome = input("informe o novo nome:").strip().title()
                 nomes.append(novo_nome)
                 print(f"{novo_nome} inserido com sucesso")
            case "2":
                print("\nlista de nomes:\n")
                for nome in nomes:
                    print(nome)
            case "3":
                break
            case _:
                print("opção invalida.")
                continue
    
except Exception as e:
    print(f"erro ao exibir a lista. {e}.")
finally:
    print("programa encerrada.")