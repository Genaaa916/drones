class pilot:
    def __init__(self, serial) -> None:
        self.serial = serial

    def __str__(self):
        return f"\nPilot name: {(self.nimi)}\nEmail: {self.mail}\nPhone number: {self.puhelinnumero}"

    def lisaa_nro(self, nro):
        self.number = nro

    def lisaa_pilot_tiedot(self, tiedot):
        self.nimi = (" ").join((tiedot[1], tiedot[2]))
        self.mail = tiedot[3]
        self.puhelinnumero = tiedot[0]

    def tulosta_pilot_tiedot(self):
        for i in [self.nimi, self.mail, self.puhelinnumero]:
            print(i)

    def lisaa_x(self, x):
        self.x = x

    def lisaa_y(self, y):
        self.y = y

    def print(self):
        print(self.number, self.x, self.y, self.serial)

    def add_serial(self, serial):
        self.serial = serial

    def write_to_file(self):
        with open("pilots.txt", "a") as f:
            f.write(f"{self.__str__()}\n")


class pilot_list:
    def __init__(self):
        self.list = []
        self.printed_list = []

    def return_serials(self):
        if len(self.list) > 0:
            return [i.serial for i in self.list]
        return []

    def add_printed(self, pilot: pilot):
        self.printed_list.append(pilot)

    def add_pilot(self, pilot: pilot):
        if pilot.serial not in self.return_serials():
            self.list.append(pilot)

    def pilot_text(self):
        return f"\nPilot name: {(self.nimi)}\nEmail: {self.mail}\nPhone number: {self.puhelinnumero}"
