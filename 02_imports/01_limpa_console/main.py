#fazendo importação de de bibliotecas 
import os 

#loop
while True:
    # limpeza de console 
    ''' A identação, sempre vem após os : ( dois pontos ).
    Preciso lembrar que a identação ela vem após os :
    Exemplo: 
    if idade > 10:
        aqui é a identação, dentro do bloco if, os : '''
    os.system("cls")
    
    # tratamento de excecção 
    
    try:
        nome = input("informe o nome: ").strip().title()
        email = input("informe o e-mail: ").strip().lower()
        cpf = input("informe o cpf: ").strip()
            # TODO
        pass

        #limpeza de console
    
        os.system("cls")
    
        #saida de dados
        print(f"Nome: {nome}")
        print(f"e-mail:{email}")
        print(f"cpf: {cpf}")

        #menu
        print("1 - inserir novos dados.")
        print("2 - Sair do programa.")
        opcao = input("opção desejada")

    # verifica a opção escolhida
        match opcao:
            case "1":
                continue 
            case "2":
                print("programa encerrado.")
                break
            case _:
                print("Opção inválida")
                break 
    
    except:
        print("Não foi possivel receber informações")