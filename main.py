import banco
import datetime

print("+--------------------+")
print("| 1. Cadastrar peças |")
print("| 2. Pesquisar peças |")
print("| 3. Deletar peças   |")
print("| 4. Inserir peças   |")
print("+--------------------+")

peca = {"id":0,
        "peca":"",
        "tipo":"",
        "parte":"",
        "veiculos":[""],
        "fabricante":"",
        "data_fabricacao":""
        }

opt = int(input());


#TODO Lucas
while True:
    match(opt):
        case 1:
            print("Insira as informações da peça: ");
            peca["peca"] = input("Qual a peça? ")
            peca["tipo"] = input("De qual tipo é a peca? ")
            peca["parte"] = input("De qual parte é a peça? ")
            lista = []
            while True:
                lista.append(input("Para quais carros é a peça? (-1 para parar) "))
                if lista[-1] == "-1":
                    lista.pop()
                    break;
            peca["veiculos"] = lista
            peca["fabricante"] = input("Qual o fabricante da peça? ")
            ano = int(input("Ano de fabricação: "))
            mes = int(input("Mes de fabricação: "))
            dia = int(input("Dia de fabricação: "))
            peca["data_fabricacao"] = datetime.datetime(ano,mes,dia).strftime("%x")

            banco.inserir(peca)
            break
        case 2:
            break
        case 3:
            break
        case 4:
            break