class Address:
    def __init__(self, index, citi, street, house, appartment):
        self.index = index
        self.citi = citi
        self.street = street
        self.house = house
        self.appartment = appartment
        self.addresss = str(index), citi, street, str(house), str(appartment)
    def postAddress(self):
        return self.addresss



class Mailing:
    def __init__(self, address_to, address_from, cost, track):
        self.to = address_to
        self.froms = address_from
        self.costs = cost
        self.tracks = track
    def postTrack(self):
        print("Отправление ", self.tracks, "из ", self.froms, "в ", self.to, "стоимость ", self.costs, "рублей.")

