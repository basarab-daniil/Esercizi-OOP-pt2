from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def scheda(self):
        return f"{super().scheda()}, Numero porte: {self.numero_porte}"