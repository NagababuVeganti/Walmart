import traceback
from Database import *

class Driver:
    def __init__(self):
        self.database_obj= TickerCounter(4,5)
        self.closebooking=False
    
    def getRowPointer(self,req):
        low=0
        high=self.database_obj.rows
        reservationRow=-1
        while low<=high:
            print(high,low,mid)
            mid=(low+high)//2
            if self.database_obj.trackRows.get(mid)>=req:
                reservationRow=mid
                low=mid+1
            else:
                high=mid-1
        
        return reservationRow

    def ReserveTicket(self,reservationID,numseats):
        if self.database_obj.totalSeatsAvail<=0:
            self.closebooking=True
            return "No More Seats"
        else:
            reservationRow=self.getRowPointer(numseats)
            
            if reservationRow>=0:
                reservationSeats=[]
                seatRow=chr(65+reservationRow)
                while(numseats>0):
                    reservationSeats.append(seatRow+str(heapq.heappop(self.database_obj.theater[reservationRow])))
                    numseats-=1
                    self.database_obj.totalSeatsAvail-=1
                    self.database_obj.trackRows[reservationRow]-=1
                return reservationSeats
            else:
                reservationSeats=[]
                while(numseats>0):
                    reservationRow=self.getRowPointer(1)
                    
                    seatRow=chr(65+reservationRow)
                    #print(reservationID,reservationRow)
                    reservationSeats.append(seatRow+str(heapq.heappop(self.database_obj.theater[reservationRow])))
                    #print("resevation",reservationSeats)
                    numseats-=1
                    self.database_obj.totalSeatsAvail-=1
                    self.database_obj.trackRows[reservationRow]-=1
                return reservationSeats


try:
        obj=Driver()
        file=open('Reservation.txt','r')
        file2=open('result.txt','w')
        for line in file.readlines():
            reservation_id,numseats=line.split(" ")
            if int(numseats)<=0:
                print("Invalid number of Seats")
                continue
            if  obj.closebooking:
                print("Raie")
                raise Exception('Bookings closeed')
            reservation_id,numseats=line.split(" ")
            file2.writelines(reservation_id+":  " + " ".join(obj.ReserveTicket(reservation_id,int(numseats)))+str("\n"))
            print(obj.database_obj.trackRows)
except Exception :
        traceback.print_exc()

