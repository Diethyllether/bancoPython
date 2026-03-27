import banco
import datetime
while True:

    print("+--------------------+")
    print("| 1. Cadastrar peças |")
    print("| 2. Pesquisar peças |")
    print("| 3. Deletar peças   |")
    print("| 4. Atualiazar peças|")
    print("| -1. para sair      |")
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

    if opt ==1:
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
    if opt ==2:
         print("Insira as informações da peça: ")
         peca["id"]= input("Qual o ID da peça?")
         banco.pesquisar(peca["id"])

    if opt == 3:
        id_pesquisa = int(input("digite o id da peça que você gostaria de deletar:"))
        banco.deletar(id_pesquisa)
    
    if opt == 4:
        print("Insira as informações da peça: ");
        peca["id"]= input("Qual o ID da peça?")
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
        banco.atualizar(peca["id"],peca["peca"],peca["tipo"],peca["parte"],peca["fabricante"],peca["data_fabricacao"])
      
    if opt==-1:
         break;
