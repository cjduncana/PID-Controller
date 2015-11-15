
from decimal import Decimal
from time import time

class PID:

    def __init__(self, setPoint, kp = Decimal("1"), ki = Decimal("0.0005"), kd = Decimal("10")):
        self.model = []
        self.setPoint = setPoint

        self.previousError = Decimal("0")
        self.sumOfErrors = Decimal("0")

        self.previousTime = Decimal(time())

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def update(self):
        if self.model:
            now = Decimal(time())
            changeInTime = now - self.previousTime

            error = self.setPoint - self.model.pop()
            self.sumOfErrors = self.sumOfErrors + (error * self.changeInTime)
            changeInError = (error - self.previousError) / self.changeInTime

            controlVariable = self.kp * error + self.ki * self.sumOfErrors + self.kd * changeInError
            
            self.previousError = error
            self.previousTime = now

            return controlVariable
        else:
            return Decimal("0")

    def tune(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
