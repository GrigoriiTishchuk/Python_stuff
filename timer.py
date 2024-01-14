class Timer:

     def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
     def __str__(self):
        return self.__format_time()
     def next_second(self):
       self.seconds += 1
       if self.seconds == 60:
           self.seconds = 0
           self.minutes += 1
           if self.minutes == 60:
               self.minutes = 0
               self.hours += 1
               if self.hours == 24:
                    self.hours = 0

     def prev_second(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -=  1
            if self.minutes < 0:
                self.minutes = 59
                self.hours -=  1
                if self.hours < 0:
                    self.hours = 23

# pad a given value with lading zeros
     def __pad_zero(self, value):
        return str(value).zfill(2)
     
# format time in hh:mm:ss 
     def __format_time(self):
        return f"{self.__pad_zero(self.hours)}:{self.__pad_zero(self.minutes)}:{self.__pad_zero(self.seconds)}"

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)