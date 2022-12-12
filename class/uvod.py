class NazivKlase:
    """
        blablalbablalblabldocstring
    """
    pass

# ovo se zove INSTANCIRANJE: 
objekt = NazivKlase() # ovo je objekt ! # instanca klase NazivKlase

class TVDevice:
    """
        Klasa koja opisuje TV uređaja
    """
    brand = "Samsung"
    model = "LED TV"
    diagonal = 55
    smart = True
    is_on = False
    channel_on = None
    volume = 0
    room = "Living Room"

    def power_on(self):
        self.is_on = True

tv_boravak = TVDevice()
print(type(tv_boravak))

print(f"brend: {tv_boravak.brand}")
print(f"model: {tv_boravak.model}")
print(f"dijagonala: {tv_boravak.diagonal}")
print(f"smart: {tv_boravak.smart}")
print(f"ukljucen: {tv_boravak.is_on}")
print(f"program: {tv_boravak.channel_on}")
print(f"glasnoca: {tv_boravak.volume}")
print(f"soba: {tv_boravak.room}")
tv_boravak.power_on()
print(f"ukljucen: {tv_boravak.is_on}")

print(TVDevice.is_on)



