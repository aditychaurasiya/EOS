
class Downlink:
    def __init__(self,timeSlotStart,timeSlotEnd ,satelliteid,groundstationid,duration,max_data):
        self.timeSlotStart = timeSlotStart
        self.timeSlotEnd = timeSlotEnd
        self.satelliteid = satelliteid
        self.groundstationid = groundstationid
        self.duration = duration
        self.max_data = max_data
    
        