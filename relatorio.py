def gerar_relatorio(lista):
    total = len(lista)
    concluidas = sum(1 for t in lista if t["concluida"])
    pendentes = total - concluidas
    print("\n===== RELATÓRIO =====")
    print(f"Total      : {total}")
    print(f"Concluídas : {concluidas}")
    print(f"Pendentes  : {pendentes}")
    if total > 0:
        print(f"Progresso  : {(concluidas/total)*100:.0f}%")
    print("=====================")