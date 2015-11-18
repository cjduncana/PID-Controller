import decimal
import unittest

import pid

class TestPID(unittest.TestCase):

    def test_pid_created(self):
        apid = pid.PID(decimal.Decimal("50"))
        assert xpid.model[-1] == decimal.Decimal("50")

    def test_pid_update(self):
        bpid = pid.PID(decimal.Decimal("50"))
        for x in xrange(1,100):
            xpid.update()
        assert xpid.update() == decimal.Decimal("0")