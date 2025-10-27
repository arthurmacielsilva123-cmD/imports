"""
Crie um programa que receba do usuário o nome, peso (em kg) e altura (em metros), calcule o IMC do usuário (arredondado para 2 casas decimais), e exiba o diagnóstico do usuário com base na tabela do IMC.
"""
# tratamento de exceçâo
try:
    # entrada de dados
    nome = input("informe o nome: ").strig().title()
    peso = float(input("informe o que em kg: ").strip().replace(",","."))
    altura = input("informe a altura em metros: ").strip().replace(",",".")
   #calculo do imc
    imc = peso(altura**2)
   # exibe o imc do usuario
    print(f"{nome}, e seu IMC é{imc:.2f}")

   # diagnosico do IMC
    if imc <18.5: 
     print(f"{nome} está abaixo do peso.")
    elif imc <25:
     print(f"{nome} está no peso ideal.")
    elif imc <30:
     print(f"{nome}está acima do peso.")
    elif imc <35:
     print(f"{nome}esta obeso")
    elif imc <40:
     print(f"{nome}está com obesidade nível II.")
    else:
     print(f"{nome}você ta imenso mermão")
except Exception as e:
     print(f"foi de vasco {e}")

