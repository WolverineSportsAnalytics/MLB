class WsaLineup():
    def __init__(self, players, date, time, points):
        self.pitcher = players[0]
        self.c_or_1B = players[1]
        self.P2B = players[2]
        self.P3B = players[3]
        self.SS = players[4]
        self.OF1 = players[5]
        self.OF2 = players[6]
        self.OF3 = players[7]
        self.UTIL = players[8]
        self.time = time
        self.date = date
        self.points = points

    def insertTable(self, cursor, lineupNumber):

        query = "Insert into lineups (lineupNumber, date, P, C1B, 2B, 3B, SS, OF1, OF2, OF3, UTIL, lineupTime, projectedPoints) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        inserts = (lineupNumber, self.date, self.pitcher, self.c_or_1B, self.P2B, self.P3B, self.SS, self.OF1, self.OF2, self.OF3, self.UTIL, self.time, self.points)
        cursor.execute(query, inserts)
