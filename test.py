import simpy
import simpy.rt
import names
from office import *
from patient import *
from medtech import *
from room import *
from schedule import *


# env = simpy.Environment()
env = simpy.rt.RealtimeEnvironment(factor=.1)

office = Office(env)
for i in range(5):
    room = ConsultRoom(office)
for i in range(2):
    room = ProcedureRoom(office)

schedule = Schedule()
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:30 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "9:15 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "10:00 am"))
schedule.appointments.sort(key=lambda x: x.timerTime)

# for a in schedule.appointments:
#     print(a.patient.name + " " + str(a.timerTime) + " " + a.time)

office.runSchedule(schedule)


env.run()
