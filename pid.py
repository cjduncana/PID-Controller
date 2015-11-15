
from decimal import Decimal
from time import time

class PID:

    def __init__(self, setPoint, timeInterval = Decimal("10"), kp = Decimal("1"), ki = Decimal("0.0005"), kd = Decimal("10")):
        self.model = []
        self.previousError = Decimal("0")
        self.sumOfPastErrors = Decimal("0")
        self.setPoint = setPoint
        self.previousTime = Decimal(time())
        self.timeInterval = timeInterval
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def update(self):
        if self.model:
            now = Decimal(time())
            changeInTime = now - self.previousTime

            error = self.setPoint - self.model.pop()
            self.sumOfPastErrors = self.sumOfPastErrors + (error * self.changeInTime)
            changeInError = (error - self.previousError) / self.changeInTime

            controlVariable = self.kp * error + self.ki * self.sumOfPastErrors + self.kd * changeInError
            
            self.previousError = error
            self.previousTime = now

            return controlVariable
        else:
            return Decimal("0")

    