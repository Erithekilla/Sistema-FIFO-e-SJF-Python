import time
import threading

class Processos:
    def __init__(self, nome, tempo, chegada):
        self.nome = nome
        self.tempo = tempo
        self.chegada = chegada

    def __repr__(self):
        return f"Processo: {self.nome} | Tempo de execução: {self.tempo} | Tempo de chegada: {self.chegada}\n"

def executar_processo(processo):
    print(f"Iniciando {processo.nome}. \nDuração prevista: {processo.tempo}")

    time.sleep(processo.tempo)

    print(f"Processo {processo.nome} finalizado.")

def simulador(lista_processos, algoritmo):
    threads = []
    
    print(f"Será executado o algoritmo {algoritmo}")
    

    if algoritmo.upper() == 'FIFO':
        lista_processos.sort(key=lambda x: x.chegada)

    if algoritmo.upper() == 'SJF':
        lista_processos.sort(key=lambda x: x.tempo)
    
    print(f"Lista de processos:")
    for p in lista_processos: print(p)

    for p in lista_processos:
        t = threading.Thread(target=executar_processo, args=(p,))

        threads.append(t)

        t.start()

        t.join()

        time.sleep(0.1)

        print("Executando próximo processo.")

    print("Foi concluido!")

def main():
    processos = int(input("Digite a quantia de processos: "))
    meus_processos = []

    for processos in range(processos):
        nome = input("Digite um nome: ")
        tempo = int(input("Digite o tempo de duração: "))
        chegada = int(input("Digite a chegada: "))
        meus_processos.append(Processos(nome=nome, tempo=tempo, chegada=chegada))
    
    algo = input("Digite que tipo de algoritmo você deseja utilizar (FIFO/SJF)").upper()

    simulador(list(meus_processos), algo)

if __name__ == '__main__':
    main()
