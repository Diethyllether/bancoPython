import json

path = "banco.json"

def abrir_banco():
    with open(path, "r", encoding="utf-8") as caminho:
        banco = json.load(caminho);
        return banco;

def inserir(json_obj):
    t = abrir_banco();
    json_obj["id"] = t["pecas"][-1]["id"] + 1;
    t["pecas"].append(json_obj);
    with open(path, "w", encoding="utf-8") as caminho:
        json.dump(t, caminho, indent=4, ensure_ascii=False);
        

#TODO Ansur
def pesquisar(id_busca):
  banco = abrir_banco()
  for i in range(len(banco["pecas"])):
    if banco["pecas"][i]["id"] == id_busca:
      print(f"ID: {banco["pecas"][i]["id"]} | {banco["pecas"][i]["peca"]}")
pesquisar(101)

#TODO Miguel
def atualizar(id_atualizar, novo_nome, novo_tipo, nova_parte, novo_veiculo, nova_fabricante, nova_data):
    banco = abrir_banco()
    for p in banco["pecas"]:
        if int(p["id"]) == int(id_atualizar):
            p["peca"] = novo_nome
            p["tipo"] = novo_tipo
            p["parte"] = nova_parte
            p["veiculos"] = novo_veiculo
            p["fabricante"] = nova_fabricante
            p["data_fabricacao"] = nova_data
            with open(path, "w", encoding="utf-8") as caminho:
                json.dump(banco, caminho, indent=4, ensure_ascii=False)
            print(f"Peça ID {id_atualizar} atualizada com sucesso!")
            return
    print(f"Peça com ID {id_atualizar} não encontrada!")
            

     
#TODO Miggs
def deletar():
    banco = abrir_banco();