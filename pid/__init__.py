
import decimal
import time

class PID(object):

    def __init__(self, setPoint,
                 kp = decimal.Decimal("1"),
                 ki = decimal.Decimal("0.0005"),
                 kd = decimal.Decimal("10")):
        self.setPoint = setPoint
        self.model = []
        self.model.append(setPoint)

        self.previousInput = decimal.Decimal(setPoint)
        self.integral = decimal.Decimal("0")

        self.previousTime = decimal.Decimal(time.time())

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def update(self):
        now = decimal.Decimal(time.time())
        changeInTime = now - self.previousTime

        processVariable = self.model[-1]

        error = self.setPoint - processVariable
        integral = self.integral + (self.ki * error \
        * changeInTime)
        changeInInput = (processVariable - self.previousInput) \
        / changeInTime

        controlVariable = self.kp * error + self.integral - self.kd \
        * changeInInput

        self.integral = integral.normalize()
        self.previousInput = processVariable.normalize()
        self.previousTime = now

        return controlVariable.normalize()

    def tune(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def set_setpoint(self, setPoint):
        self.setPoint = setPoint
