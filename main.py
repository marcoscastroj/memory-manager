class Processo:
    def __init__(self, processo_id, tamanho):
        self.processo_id = processo_id
        self.tamanho = tamanho

class Memoria:
    def __init__(self, tamanho_total):
        self.tamanho_total = tamanho_total
        self.espaco_livre = tamanho_total
        self.processos = [None] * tamanho_total

    def alocar_processo_first_fit(self, processo_id, tamanho_processo):
        if tamanho_processo > self.espaco_livre:
            print("Erro: Não há espaço suficiente na memória para alocar o processo.")
            return

        indice_inicio = 0
        espaco_atual = 0
        for i, processo in enumerate(self.processos):
            if processo is None:
                espaco_atual += 1
                if espaco_atual >= tamanho_processo:
                    indice_inicio = i - espaco_atual + 1
                    break
            else:
                espaco_atual = 0

        if espaco_atual < tamanho_processo:
            indice_inicio = len(self.processos)

        for i in range(indice_inicio, indice_inicio + tamanho_processo):
            self.processos[i] = processo_id
        self.espaco_livre -= tamanho_processo
        print(f"Processo {processo_id} alocado na memória.")

    def alocar_processo_best_fit(self, processo_id, tamanho_processo):
            if tamanho_processo > self.espaco_livre:
                print("Erro: Não há espaço suficiente na memória para alocar o processo.")
                return

            melhor_inicio = -1
            melhor_tamanho_livre = float('inf')
            inicio_atual = -1
            tamanho_atual = 0
            for i, processo in enumerate(self.processos):
                if processo is None:
                    tamanho_atual += 1
                    if tamanho_atual >= tamanho_processo:
                        if tamanho_atual < melhor_tamanho_livre:
                            melhor_inicio = i - tamanho_atual + 1
                            melhor_tamanho_livre = tamanho_atual
                else:
                    inicio_atual = -1
                    tamanho_atual = 0

            if melhor_inicio == -1:
                melhor_inicio = len(self.processos)

            for i in range(melhor_inicio, melhor_inicio + tamanho_processo):
                self.processos[i] = processo_id
            self.espaco_livre -= tamanho_processo
            print(f"Processo {processo_id} alocado na memória.")

    def alocar_processo_worst_fit(self, processo_id, tamanho_processo):
        if tamanho_processo > self.espaco_livre:
            print("Erro: Não há espaço suficiente na memória para alocar o processo.")
            return

        pior_inicio = -1
        pior_tamanho_livre = -1
        inicio_atual = -1
        tamanho_atual = 0
        for i, processo in enumerate(self.processos):
            if processo is None:
                tamanho_atual += 1
                if tamanho_atual >= tamanho_processo:
                    if tamanho_atual > pior_tamanho_livre:
                        pior_inicio = i - tamanho_atual + 1
                        pior_tamanho_livre = tamanho_atual
            else:
                inicio_atual = -1
                tamanho_atual = 0

        if pior_inicio == -1:
            pior_inicio = len(self.processos)

        for i in range(pior_inicio, pior_inicio + tamanho_processo):
            self.processos[i] = processo_id
        self.espaco_livre -= tamanho_processo
        print(f"Processo {processo_id} alocado na memória.")


    def exibir_processos(self):
        processos = {}
        for i, processo in enumerate(self.processos):
            if processo is not None:
                if processo not in processos:
                    processos[processo] = []
                processos[processo].append(i)

        print("\nProcessos na memória:")
        for processo, posicoes in processos.items():
            posicoes_str = ", ".join(str(posicao) for posicao in posicoes)
            print(f"Processo {processo}: Posições {posicoes_str}")

    def liberar_processo(self, processo_id):
        for i, processo in enumerate(self.processos):
            if processo == processo_id:
                self.processos[i] = None
                self.espaco_livre += 1
        print(f"Processo {processo_id} liberado da memória.")

def main():
    memoria = Memoria(128)

    while True:
        print("\nMenu:")
        print("1. Adicionar processo (First Fit)")
        print("2. Adicionar processo (Best Fit)")
        print("3. Adicionar processo (Worst Fit)")
        print("4. Liberar processo")
        print("5. Exibir processos na memória")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            processo_id = input("Digite o ID do processo: ")
            tamanho_processo = int(input("Digite o tamanho do processo: "))
            memoria.alocar_processo_first_fit(processo_id, tamanho_processo)
        elif escolha == "2":
            processo_id = input("Digite o ID do processo: ")
            tamanho_processo = int(input("Digite o tamanho do processo: "))
            memoria.alocar_processo_best_fit(processo_id, tamanho_processo)
        elif escolha == "3":
            processo_id = input("Digite o ID do processo: ")
            tamanho_processo = int(input("Digite o tamanho do processo: "))
            memoria.alocar_processo_worst_fit(processo_id, tamanho_processo)
        elif escolha == "4":
            processo_id = input("Digite o ID do processo a ser liberado: ")
            memoria.liberar_processo(processo_id)
        elif escolha == "5":
            memoria.exibir_processos()
        elif escolha == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
