from collections import defaultdict
from email.policy import default
import heapq
class TickerCounter:
    def __init__(self,rows,seats):
        self.rows=rows
        self.seats=seats
        self.totalSeatsAvail=rows*seats
        self.theater=[self.getSeats(seats) for i in range(self.rows)]
        self.trackRows=dict({i:seats for i in range(self.rows)})
    def getSeats(self,seats):
        seats=[i for i in range(seats)]
        heapq.heapify(seats)
        return seats

    