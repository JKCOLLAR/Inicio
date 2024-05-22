import datetime

class Estacionamento:
    def __init__(self, total_vagas):
        self.total_vagas = total_vagas
        self.vagas_disponiveis = total_vagas
        self.vagas_ocupadas = {}
        self.preco_por_hora = 5.5  # Preço por hora
        
    def entrada_veiculo(self, placa):
        if self.vagas_disponiveis > 0:
            hora_entrada = datetime.datetime.now()
            self.vagas_ocupadas[placa] = hora_entrada
            self.vagas_disponiveis -= 1
            print(f"Veículo {placa} entrou às {hora_entrada}. Vagas disponíveis: {self.vagas_disponiveis}")
        else:
            print("Estacionamento cheio. Entrada não permitida.")
        
    def saida_veiculo(self, placa):
        if placa in self.vagas_ocupadas:
            hora_saida = datetime.datetime.now()
            hora_entrada = self.vagas_ocupadas.pop(placa)
            self.vagas_disponiveis += 1
            tempo_total = (hora_saida - hora_entrada).total_seconds() / 3600
            custo_total = tempo_total * self.preco_por_hora
            print(f"Veículo {placa} saiu às {hora_saida}. Tempo total: {tempo_total:.2f} horas. Custo: R${custo_total:.2f}. Vagas disponíveis: {self.vagas_disponiveis}")
        else:
            print("Veículo não encontrado.")
        
    def status(self):
        print(f"Vagas Totais: {self.total_vagas}, Vagas Disponíveis: {self.vagas_disponiveis}, Vagas Ocupadas: {len(self.vagas_ocupadas)}")
        print("Veículos Estacionados:")
        for placa, hora_entrada in self.vagas_ocupadas.items():
            print(f"{placa} - Entrada: {hora_entrada}")

def main():
    estacionamento = Estacionamento(total_vagas=10)
    
    while True:
        print("\nSistema de Estacionamento")
        print("1. Entrada de Veículo")
        print("2. Saída de Veículo")
        print("3. Status do Estacionamento")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            placa = input("Digite a placa do veículo: ")
            estacionamento.entrada_veiculo(placa)
        elif escolha == '2':
            placa = input("Digite a placa do veículo: ")
            estacionamento.saida_veiculo(placa)
        elif escolha == '3':
            estacionamento.status()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
