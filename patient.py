import names

class Patient(object):
    def __init__(self):
        self.name = names.get_full_name()

    def checkIn(self, office, appointment):
        self.env = office.env
        self.appointment = appointment
        print(self.name + " checking in (" + str(self.env.now) + ")")
        yield self.env.timeout(5)
        office.lobby.put(self)
        self.appointment.status = "checked in"
        print(self.name + " waiting in lobby (" + str(self.env.now) + ")")
