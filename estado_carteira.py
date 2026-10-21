import os
import json

class Carteira:
    def __init__(self, saldo, status):
        self.saldo = saldo
        self.status = status
    def save_status(self):
        self.lista = {"tipo": self.status, "valor": self.saldo}
        return self.lista
class Arquivos:
    def save(self, carteira):
        lista = []
        dados = carteira.save_status()
        lista.append(dados)
        print("DADOS -> ", dados)
        if not os.path.exists("status_carteira.json"):
            with open("status_carteira.json", "x", encoding="utf-8") as arquivo:
                json.dump(lista, arquivo, indent=4, ensure_ascii=False)
        else:
            with open("status_carteira.json", "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
            lista.append(dados)
            with open("status_carteira.json", "w", encoding="utf-8") as arquivo:
                json.dump(lista, arquivo, indent=4, ensure_ascii=False)