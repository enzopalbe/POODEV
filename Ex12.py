from enum import Enum, auto

# Enumeração DiasDaSemana
class DiasDaSemana(Enum):
    SEGUNDA = auto()
    TERCA = auto()
    QUARTA = auto()
    QUINTA = auto()
    SEXTA = auto()
    SABADO = auto()
    DOMINGO = auto()

# Classe Agenda
class Agenda:
    def __init__(self):
        # Dicionário para armazenar compromissos com base no dia da semana
        self.compromissos = {dia: [] for dia in DiasDaSemana}

    def marcar_compromisso(self, dia, compromisso):
        if dia in DiasDaSemana:
            self.compromissos[dia].append(compromisso)
            print(f"Compromisso '{compromisso}' marcado para {dia.name}.")
        else:
            print("Dia da semana inválido.")

    def exibir_compromissos(self):
        for dia, compromissos in self.compromissos.items():
            if compromissos:
                print(f"{dia.name}: {', '.join(compromissos)}")
            else:
                print(f"{dia.name}: Nenhum compromisso.")

# Exemplo de uso
agenda = Agenda()
agenda.marcar_compromisso(DiasDaSemana.SEGUNDA, "Reunião de equipe")
agenda.marcar_compromisso(DiasDaSemana.SEXTA, "Entrega de projeto")
agenda.marcar_compromisso(DiasDaSemana.SABADO, "Almoço com amigos")
agenda.marcar_compromisso(DiasDaSemana.QUARTA, "Treinar boxe")

agenda.exibir_compromissos()
