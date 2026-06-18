class Tarefas:
    def __init__(self):
        self.lista = []

    def adicionar(self, nome):
        self.lista.append({"nome": nome, "concluida": False})

    def listar(self):
        if not self.lista:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "○"
            print(f"{i}. [{s}] {t['nome']}")

    def concluir(self, indice):
        if 0 <= indice < len(self.lista):
            self.lista[indice]["concluida"] = True
            print("✓ Tarefa concluída!")
        else:
            print("Tarefa não encontrada.")