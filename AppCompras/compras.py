



from ast import Str
from re import I, M


print ("Olá, bem vindo (a) à sua lista de compras. Por favor, digite o seu nome para continuar: ")
user_Name = input()

print ("Você prefere ser tratado (a) por um pronome feminino ou masculino?\nM ou F? ")

sexo = ""

while True:
    sexo = str.upper(input())
    if sexo in ("M", "F"):
        break
    #se contiver as letras M ou F, o loop quebra.
    else:
        print("Não entendi")
    #se não, aparece essa mensagem e tenta outra vez.

if sexo == "M":
    print (f"Olá Sr.{user_Name}")
    full_Username = "Sr." + user_Name

elif sexo == "F":
    print(f"Olá Sra.{user_Name}")
    full_Username = "Sra." + user_Name

print ("Agora, vamos anotar o que você precisa comprar.\nSepare os itens por vírgula: ")

itens = str(input())

lista_compras = itens.split(",")
#Transformar as palavras pelo espaço

for name in lista_compras:
    print (name.strip().capitalize())

while True:
    print("Você gostaria de ver novamente a lista?\nA)Sim\tB)Não?")
    check_again = str(input()).upper()
    if check_again in ("SIM", "A"):
        print (lista_compras)
        
    elif check_again in ("NÃO", "B"):
        print ("Ok. Você gostaria de sair do programa ou zerar a lista?\nA.Sair\tB.Zerar")

        fail_check = str(input()).upper()

        if fail_check in ("B", "ZERAR"):
                lista_compras.clear()
                
                print("Digite os itens da nova lista, lembrando de separar por vírgula: ")
                itens = str(input())
            
                lista_compras = itens.split(",")

                for name in lista_compras:
                    print(name.strip().capitalize())

                    while True:
                        print("Você gostaria de ver novamente a lista completa?\nA)Sim\tB)Não?")
                        check_again = str(input()).upper()

                        if check_again in ("SIM", "A"):
                            print (lista_compras)

                        elif check_again in ("NÃO", "B"):
                            print("Obrigado por utilizar o programa {full_Username}!")
                            break
                        break
                    break
                break
        if fail_check in ("A", "SAIR"):
                break
        
            

    






    





