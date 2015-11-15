
from decimal import Decimal

class PID:

    def __init__(self, setPoint, timeInterval = Decimal("10"), kp = Decimal("1"), ki = Decimal("0.0005"), kd = Decimal("10")):
        self.model = []
        self.previousError = Decimal("0")
        self.sumOfPastErrors = Decimal("0")
        self.setPoint = setPoint
        self.timeInterval = timeInterval
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def update(self):
        if self.model:
            error = self.setPoint - self.model.pop()
            self.sumOfPastErrors = self.sumOfPastErrors + (error * self.timeInterval)
            changeInError = (error - self.previousError) / self.timeInterval
            controlVariable = self.kp * error + self.ki * self.sumOfPastErrors + self.kd * changeInError
            self.previousError = error
            return controlVariable
        else:
            return Decimal("0")

    