import simpy
class Office(object):
    def __init__(self, env):
        self.env = env
        self.lobby = simpy.Store(self.env, capacity=10)
        self.rooms = simpy.FilterStore(self.env)
        self.staff = simpy.FilterStore(self.env)

    def runSchedule(self, schedule):
        schedule.appointments.sort(key=lambda x: x.timerTime)
        self.env.process(self.scheduleProcess(schedule))

    def scheduleProcess(self, schedule):
        while True:
            print(self.env.now)
            for appointment in [a for a in schedule.appointments if a.timerTime == self.env.now]:
                print(appointment.patient.name + " " + appointment.time)
                self.env.process(appointment.patient.checkIn(self, appointment))

            yield self.env.timeout(1)
        # if self.env.now



class OfficeResource(object):
    """
    Pulls the environment from the office object and generates a name based on
    the class
    """

    i = 1;

    def __init__(self, office):
        self.env = office.env
        self.name = self.__class__.__name__ + str(self.__class__.i);
        self.__class__.i += 1
