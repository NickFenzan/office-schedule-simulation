import office

class Room(office.OfficeResource):
    def __init__(self, office):
        super(Room, self).__init__(office)
        office.rooms.put(self)

class ProcedureRoom(Room):
    def __init__(self, office):
        super(ProcedureRoom, self).__init__(office)

class ConsultRoom(Room):
    def __init__(self, office):
        super(ConsultRoom, self).__init__(office)
