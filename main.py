class MemoryManager:
    def __init__(self, total_memory_kb=128):
        self.total_memory_kb = total_memory_kb
        self.memory = [None] * total_memory_kb
        self.processes = {}  

    def allocate_first_fit(self, process_id, size_kb):
        for i in range(self.total_memory_kb):
            if not self.memory[i]:
                if i + size_kb <= self.total_memory_kb:
                    for j in range(i, i + size_kb):
                        self.memory[j] = process_id
                    self.processes[process_id] = (i, size_kb)
                    print(f"Alocado {size_kb} KB para o Processo {process_id} a partir do endereço {i}")
                    return True
                else:
                    print(f"Espaço insuficiente para o Processo {process_id}")
                    return False
        print(f"Nenhum espaço disponível para o Processo {process_id}")
        return False

    def allocate_best_fit(self, process_id, size_kb):
        best_fit_index = None
        best_fit_size = float('inf')
        for i in range(self.total_memory_kb):
            if not self.memory[i]:
                block_size = 1
                while i + block_size < self.total_memory_kb and not self.memory[i + block_size]:
                    block_size += 1
                if block_size >= size_kb and block_size < best_fit_size:
                    best_fit_index = i
                    best_fit_size = block_size

        if best_fit_index is not None:
            for i in range(best_fit_index, best_fit_index + size_kb):
                self.memory[i] = process_id
            self.processes[process_id] = (best_fit_index, size_kb)
            print(f"Alocado {size_kb} KB para o Processo {process_id} usando Best Fit no endereço {best_fit_index}")
            return True
        print(f"Espaço insuficiente para o Processo {process_id}")
        return False

    def allocate_worst_fit(self, process_id, size_kb):
        worst_fit_index = None
        worst_fit_size = 0
        for i in range(self.total_memory_kb):
            if not self.memory[i]:
                block_size = 1
                while i + block_size < self.total_memory_kb and not self.memory[i + block_size]:
                    block_size += 1
                if block_size >= size_kb and block_size > worst_fit_size:
                    worst_fit_index = i
                    worst_fit_size = block_size

        if worst_fit_index is not None:
            for i in range(worst_fit_index, worst_fit_index + size_kb):
                self.memory[i] = process_id
            self.processes[process_id] = (worst_fit_index, size_kb)
            print(f"Alocado {size_kb} KB para o Processo {process_id} usando Worst Fit no endereço {worst_fit_index}")
            return True
        print(f"Espaço insuficiente para o Processo {process_id}")
        return False

    def deallocate(self, process_id):
        if process_id in self.processes:
            start_index, size_kb = self.processes[process_id]
            for i in range(start_index, start_index + size_kb):
                self.memory[i] = None
            del self.processes[process_id]
            print(f"Desalocada a memória do processo {process_id}")
            return True
        print(f"Processo {process_id} não encontrado")
        return False

    def print_memory(self):
        for i in range(self.total_memory_kb):
            if self.memory[i]:
                print(f"Endereço {i}: Processo {self.memory[i]}")
            else:
                print(f"Endereço {i}: Livre")

if __name__ == "__main__":
    memory_manager = MemoryManager()

    memory_manager.allocate_best_fit("P1", 20)
    memory_manager.allocate_best_fit("P2", 38)
    memory_manager.allocate_best_fit("P3", 38)
    memory_manager.allocate_best_fit("P4", 20)
    memory_manager.deallocate("P2")
    memory_manager.allocate_best_fit("P6", 8)
    memory_manager.allocate_best_fit("P7", 5)
    
    
    

    #memory_manager.allocate_best_fit("P2", 15)
    #memory_manager.allocate_worst_fit("P3", 30)

    #memory_manager.deallocate("P2")

    #memory_manager.allocate_first_fit("P8", 1)

    memory_manager.print_memory()
