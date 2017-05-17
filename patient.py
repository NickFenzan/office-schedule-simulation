import names

class Patient(object):
    def __init__(self):
        self.name = names.get_full_name()

    def checkIn(self, office, appointment):
        print("checking in")
        self.env = office.env
        self.appointmentType = appointment.type
        yield self.env.timeout(5)
        office.lobby.put(self)
        print("waiting in lobby")
