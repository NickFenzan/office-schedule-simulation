import time

class Schedule(object):
    def __init__(self):
        self.appointments = []


class Appointment(object):
    def __init__(self, patient, type, apptTime):
        self.time = apptTime
        self.timerTime = int((time.mktime(time.strptime("8:00 am", "%I:%M %p")) - time.mktime(time.strptime(self.time, "%I:%M %p"))) / -60)
        self.patient = patient
        self.status = "pending"
        self.type = type
