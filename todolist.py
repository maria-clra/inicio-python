tarefas = []

def mostrar_tarefas():
    print("\nSuas Tarefas:")
    if not tarefas:
        print("  - Nenhuma tarefa por enquanto!")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"  {i}. {tarefa}")

def adicionar_tarefa():
    nova = input("Digite a nova tarefa: ")
    tarefas.append(nova)
    print("Tarefa adicionada! ✅")

def remover_tarefa():
    mostrar_tarefas()
    try:
        num = int(input("Número da tarefa a remover: "))
        if 0 < num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número!")

def menu():
    while True:
        print("\n📋 Menu:")
        print("1. Ver tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_tarefas()
        elif escolha == "2":
            adicionar_tarefa()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida!")

menu()
