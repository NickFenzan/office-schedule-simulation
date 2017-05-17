class MedTech(object):
    def __init__(self, office):
        self.env = office.env
        self.office = office
        self.action = self.env.process(self.lookForPatient())

    def lookForPatient(self):
        while True:
            yield self.env.timeout(1)
            patient = yield self.office.lobby.get()
            print(patient.name)
