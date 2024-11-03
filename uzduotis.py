class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas

        print(f"Metai: {metai}\nModelis: {modelis}\nKuro tipas: {kuro_tipas}\n")

    def vaziuoti(self):
        return "Vaziuoja"

    def stoveti(self):
        return "Priparkuota"

    def pildyti_degalu(self):
        return "Degalai ipilti"


class Elektromobilis(Automobilis):

    def kraunasi(self):
        return "Baterija kraunasi"

    def pildyti_degalu(self):
        return "Baterija ikrauta"

    def vaziuoti_autonomiskai(self):
        return "Vaziuoja autonomiskai"


vdv_automobilis = Automobilis(2024, "Audi", "Dyzelinas")
print(
    f"{vdv_automobilis.vaziuoti()}, {vdv_automobilis.stoveti()}, {vdv_automobilis.pildyti_degalu()}"
)

print()
ev_automobilis = Elektromobilis(2013, "Nissan", "Elektra")
print(
    f"{ev_automobilis.kraunasi()} {ev_automobilis.vaziuoti()}, {ev_automobilis.stoveti()}, {ev_automobilis.pildyti_degalu()}, {ev_automobilis.vaziuoti_autonomiskai()}"
)