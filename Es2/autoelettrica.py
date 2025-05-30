from veicolo import Veicolo

class AutoElettrica(Veicolo):
    def __init__(self, marca, modello, autonomia_km):
        super().__init__(marca, modello)
        self.autonomia_km = autonomia_km

    def scheda(self):
        return f"{super().scheda()}, Autonomia km: {self.autonomia_km}"