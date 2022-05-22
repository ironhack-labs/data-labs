import unittest
from vikingsClases import Viking
from inspect import signature


class TestViking(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.name = 'Harald'
        cls.strength = 150
        cls.health = 300
        cls.viking = Viking(cls.name, cls.health, cls.strength)

    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Viking).parameters), 3)

    def testName(self):
        self.assertEqual(self.viking.name, self.name)

    def testHealth(self):
        self.assertEqual(self.viking.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.viking.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.viking.attack), True)

    def testAttackReciveNoParameters(self):
        self.assertEqual(len(signature(self.viking.attack).parameters), 0)

    def testAttackShouldReturnStrength(self):
        self.assertEqual(self.viking.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.viking.receiveDamage), True)

    def testReceiveDamageReciveOneParam(self):
        self.assertEqual(
            len(signature(self.viking.receiveDamage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        self.viking.receiveDamage(50)
        self.assertEqual(self.viking.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        self.assertEqual(self.viking.receiveDamage(50), self.name +
                         ' has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        self.assertEqual(self.viking.receiveDamage(70), self.name +
                         ' has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        self.assertEqual(self.viking.receiveDamage(self.health),
                         self.name + ' has died in act of combat')

    def testBattleCry(self):
        self.assertEqual(callable(self.viking.battleCry), True)

    def testBattleCryReturnString(self):
        self.assertEqual(self.viking.battleCry(), 'Odin Owns You All!')


if __name__ == '__main__':
    unittest.main()
