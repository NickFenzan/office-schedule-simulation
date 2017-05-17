import simpy
import simpy.rt
import names
from office import *
from patient import *
from staff import *
from room import *
from schedule import *


env = simpy.Environment()
# env = simpy.rt.RealtimeEnvironment(factor=.1)

office = Office(env)
for i in range(2):
    room = ConsultRoom(office)
for i in range(2):
    room = ProcedureRoom(office)

for i in range(2):
    medtech = MedTech(office)

schedule = Schedule()
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:15 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:20 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:25 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:30 am"))
schedule.appointments.append(Appointment(Patient(), "New Patient", "8:45 am"))
schedule.appointments.sort(key=lambda x: x.timerTime)

# for a in schedule.appointments:
#     print(a.patient.name + " " + str(a.timerTime) + " " + a.time)

office.runSchedule(schedule)


env.run(until=120)
