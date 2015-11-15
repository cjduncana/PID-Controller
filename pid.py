
from decimal import Decimal
from time import time

class PID:

    def __init__(self, setPoint,
                 kp = Decimal("1"),
                 ki = Decimal("0.0005"),
                 kd = Decimal("10")):
        self.setPoint = setPoint
        self.model = []
        self.model.append(setPoint)

        self.previousInput = Decimal("0")
        self.integral = Decimal("0")

        self.previousTime = Decimal(time())

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def update(self):
        now = Decimal(time())
        changeInTime = now - self.previousTime

        processVariable = self.model.pop()

        error = self.setPoint - processVariable
        self.integral = self.integral + (ki * error * changeInTime)
        changeInInput = (processVariable - self.previousInput) /
                        changeInTime

        controlVariable = self.kp * error + self.integral -
                          self.kd * changeInInput

        self.previousInput = processVariable
        self.previousTime = now

        return controlVariable

    def tune(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def set_setpoint(self, setPoint):
        self.setPoint = setPoint
