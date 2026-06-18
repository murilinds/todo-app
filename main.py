from tarefas import Tarefas

def menu():
    print("\n=== To-Do App ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")
    return input("Opção: ")

def main():
    app = Tarefas()
    while True:
        op = menu()
        if op == "1":
            nome = input("Nome: ")
            app.adicionar(nome)
            print("✓ Adicionada!")
        elif op == "2": app.listar()
        elif op == "3":
            i = int(input("Número: ")) - 1
            app.concluir(i)
        elif op == "4": break

if __name__ == "__main__": main()