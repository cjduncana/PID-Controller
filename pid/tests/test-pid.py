import decimal
import unittest

import pid

class TestPID(unittest.TestCase):

    def test_pid_created(self):
        xpid = pid.PID(decimal.Decimal("50"))
        assert xpid.model[-1] == decimal.Decimal("50")

    def test_pid_update(self):
        xpid = pid.PID(decimal.Decimal("50"))
        for x in xrange(1,100):
            xpid.update()
        assert xpid.update() == decimal.Decimal("0")

    def test_tuning(self):
        xpid = pid.PID(decimal.Decimal("50"))
        xpid.tune(decimal.Decimal("2"),
                  decimal.Decimal("0.0001"),
                  decimal.Decimal("11"))
        assert xpid.kp == decimal.Decimal("2") \
           and xpid.ki == decimal.Decimal("0.0001") \
           and xpid.kd == decimal.Decimal("11")

    def test_setting_new_setpoint(self):
        xpid = pid.PID(decimal.Decimal("50"))
        xpid.set_setpoint(decimal.Decimal("100"))
        assert xpid.setPoint == decimal.Decimal("100")
