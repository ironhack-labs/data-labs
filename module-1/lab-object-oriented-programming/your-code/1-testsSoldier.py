import unittest
from vikingsClases import Soldier
from inspect import signature


class TestSoldier(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.strength = 150
        cls.health = 300
        cls.soldier = Soldier(cls.health, cls.strength)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(Soldier).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.soldier.health, self.health)

    def testStrength(self):
        self.assertEqual(self.soldier.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.soldier.attack), True)

    def testAttackHasNoParams(self):
        self.assertEqual(len(signature(self.soldier.attack).parameters), 0)

    def testAttackRetunsStrength(self):
        self.assertEqual(self.soldier.attack(), self.strength)

    def testReceivesDamage(self):
        self.assertEqual(callable(self.soldier.receiveDamage), True)

    def testReceivesDamageHasParams(self):
        self.assertEqual(
            len(signature(self.soldier.receiveDamage).parameters), 1)

    def testReceiveDamageReturnNone(self):
        self.assertEqual(self.soldier.receiveDamage(50), None)

    def testCanReceiveDamage(self):
        self.soldier.receiveDamage(50)
        self.assertEqual(self.soldier.health, self.health - 50)


if __name__ == '__main__':
    unittest.main()
