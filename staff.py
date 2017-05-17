import office

class Staff(office.OfficeResource):
    def __init__(self, office):
        super(Staff, self).__init__(office);

class MedTech(Staff):
    def __init__(self, office):
        super(MedTech, self).__init__(office);
        self.env = office.env
        self.office = office
        self.env.process(self.watchLobby())

    def watchLobby(self):
        while True:
            patient = yield self.office.lobby.get()
            if(patient):
                yield self.env.process(self.findRoomForPatient(patient))
            else:
                yield self.env.timeout(1)

    def findRoomForPatient(self, patient):
        room = yield self.office.rooms.get(lambda room: room.__class__.__name__ == "ConsultRoom")
        if(room):
            print(self.name + " put " + patient.name + " in " + room.name + " (" + str(self.env.now)+ ")")
            yield self.env.timeout(15)
            self.office.rooms.put(room);
        else:
            yield self.env.timeout(1)
