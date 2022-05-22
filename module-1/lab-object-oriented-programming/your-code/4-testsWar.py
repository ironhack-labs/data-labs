import unittest
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
from inspect import signature


class TestWar(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.war = War()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(War).parameters), 0)

    def testVikingArmy(self):
        self.assertEqual(self.war.vikingArmy, [])

    def testSaxonArmy(self):
        self.assertEqual(self.war.saxonArmy, [])


class TestWar2(unittest.TestCase):
    @classmethod
    def setUp(cls):
        def generateViking():
            cls.name = 'Harald'
            cls.strength = 150
            cls.health = 300
            return Viking(cls.name, cls.health, cls.strength)

        def generateSaxon():
            cls.health = 60
            cls.strength = 25
            return Saxon(cls.health, cls.strength)

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.war = War()
        cls.war.addSaxon(cls.saxon)
        cls.war.addViking(cls.viking)

    def testAddViking(self):
        self.assertEqual(callable(self.war.addViking), True)

    def testAddVikingShouldReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.addViking).parameters), 1)

    def testAddVikingInList(self):
        self.assertEqual(self.war.vikingArmy, [self.viking])

    def testAddVikingReturnNull(self):
        self.assertEqual(self.war.addViking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        self.assertEqual(callable(self.war.addSaxon), True)

    def testAddSaxonReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.addSaxon).parameters), 1)

    def testSaxonArmyReturnEmptyList(self):
        self.assertEqual(self.war.saxonArmy, [self.saxon])

    def testAddSaxonReturnNone(self):
        self.assertEqual(self.war.addSaxon(self.saxon), None)

    def testVikingAttackIsFunction(self):
        self.assertEqual(callable(self.war.vikingAttack), True)

    def testVikingAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.vikingAttack).parameters), 0)

    def testSaxonHealth(self):
        oldHealt = self.saxon.health
        self.war.vikingAttack()
        self.assertEqual(self.saxon.health, oldHealt - self.viking.strength)

    def testVikingAttack(self):
        self.war.vikingAttack()
        self.assertEqual(len(self.war.saxonArmy), 0)

    def testAddSaxon(self):
        print(self.war.__dict__)
        self.assertEqual(self.war.vikingAttack(), 'A Saxon has died in combat')

    def testSaxonAttackIsFunction(self):
        self.assertEqual(callable(self.war.saxonAttack), True)

    def testSaxonAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.saxonAttack).parameters), 0)

    def testVikingHealth(self):
        oldHealt = self.viking.health
        self.war.saxonAttack()
        self.assertEqual(self.viking.health, oldHealt - self.saxon.strength)

    def testVikingArmyList(self):
        for i in range(12):
            if(len(self.war.vikingArmy) == 0):
                break
            self.war.saxonAttack()
        self.assertEqual(len(self.war.vikingArmy), 0)

    def testReturnOfSaxonAttack(self):
        self.assertEqual(self.war.saxonAttack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testShowStatusShouldIsFunction(self):
        self.assertEqual(callable(self.war.showStatus), True)

    def testShowStatusReceiveNoParams(self):
        self.assertEqual(len(signature(self.war.showStatus).parameters), 0)

    def testShouldReturnStringVikingsWon(self):
        self.war.vikingAttack()
        self.assertEqual(self.war.showStatus(),
                         'Vikings have won the war of the century!')

    def testShouldReturnStringSaxonsWon(self):
        for i in range(12):
            self.war.saxonAttack()
        self.assertEqual(self.war.showStatus(
        ), 'Saxons have fought for their lives and survive another day...')

    def testShouldReturnStringStillFighting(self):
        self.assertEqual(
            self.war.showStatus(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
