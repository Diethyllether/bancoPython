import json

path = "banco.json"

def abrir_banco():
    with open(path, "r", encoding="utf-8") as caminho:
        banco = json.load(caminho, "utf8");
        return banco;

def inserir(json_obj):
    t = abrir_banco();
    json_obj["id"] = t["pecas"][-1]["id"] + 1;
    t["pecas"].append(json_obj);
    with open(path, "w", encoding="utf-8") as caminho:
        json.dump(t, caminho, indent=4, ensure_ascii=False);
        
        
def pesquisar(string):
    banco = abrir_banco;
    

# def atualizar()
# def deletar()