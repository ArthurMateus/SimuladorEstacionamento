# Arthur Ferreira da Silva Mateus
# Lucas Gazoni Araújo 
# Sérgio Murilo Moreira Morais
# Henrique Weirich Meurer siegel

class Estacionamento:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.pilha = []
    
    def chegada(self, placa):
        if len(self.pilha) < self.capacidade:
            self.pilha.append(placa)
            print(f"Carro com a placa {placa} entrou no estacionamento. Vagas Disponíveis: {self.capacidade - len(self.pilha)}")
        else:
            print(f"O estacionamento está em sua capacidade máxima. O carro {placa} não pode entrar.")
    
    def saida(self, placa):
        if placa in self.pilha:
            manobras = 0
            pilha_auxiliar = []
            
            while self.pilha and self.pilha[-1] != placa:
                manobras += 1
                pilha_auxiliar.append(self.pilha.pop())
            
            if self.pilha:
                self.pilha.pop()
                print(f"Carro {placa} saiu do estacionamento. Manobras necessárias: {manobras}")
            
            while pilha_auxiliar:
                self.pilha.append(pilha_auxiliar.pop())
        else:
            print(f"Carro {placa} não está no estacionamento.")
            
def processador(estacionamento, tipo, placa):
    if tipo == 'E':
        estacionamento.chegada(placa)
    elif tipo == 'S':
        estacionamento.saida(placa)

def main():
    estacionamento = Estacionamento()
    while True:
        placa = input("Qual é a placa do carro? ")
        if len(placa) != 7:
            print("A placa deverá ter 7 caracteres.")
            continue
        
        tipo = input("O que o carro está fazendo? ([E]ntrando/[S]aindo) ").upper()
        if tipo not in ['E', 'S']:
            print("Tipo inválido. Por favor, insira 'E' para entrada ou 'S' para saída.")
            continue

        processador(estacionamento, tipo, placa)
        
        continuar = input("Deseja continuar? (s/n) ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
