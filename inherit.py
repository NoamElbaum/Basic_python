import time
import datetime

class Time:
    def __init__(self):
        self.t = time.localtime(0)
        self.ftime = f"{self.t[3]}:{self.t[4]}:{self.t[5]}"

    def get_time(self):
        self.t = time.localtime()
        self.ftime = f"{self.t[3]}:{self.t[4]}:{self.t[5]}"
        print(self.ftime)

class Date:
    def __init__(self):
        self.date = datetime.date.today()

    def get_date(self):
        self.date = datetime.date.today()
        print(self.date)


if __name__ == "__main__":
    t = Time()
    d = Date()

    t.get_time()
    d.get_date()