from library import*
import unittest


class TestGarden(unittest.TestCase):

    __HERBS = ['картофель', 'томат', 'перец']
    __TREE = ['яблоня', 'груша']

    def setUp(self):
        self.garden = Garden()
        self.garden.get_data_from_file('data.json')
        self.tomato = Tomato(100, 100, 0, 0, False, False)

    def test_add_garden_bed(self):
        if self.assertGreater(self.garden.money, 10):
            self.garden.add_garden_bed()
            self.assertEqual(self.garden.garden_bed_kol, 1)

    def test_plant_cultivated_plant(self):
        name = 'томат'
        if self.garden.add_garden_bed() and self.assertGreater(self.garden.money, 20):
            self.garden.plant_cultivated_plant(name, 0)
            self.assertGreater(self.__HERBS.count(name), 0)

    def test_plant_tree(self):
        name = 'груша'
        if self.assertGreater(self.garden.money, 25):
            self.garden.plant_tree(name)
            self.assertGreater(self.__TREE.count(name), 0)

    def test_money(self):
        self.assertEqual(type(self.garden.money), int)

    def test_day(self):
        self.assertEqual(type(self.garden.day), int)

    def test_check_alive(self):
        if not self.tomato.check_alive():
            self.assertGreater(0, self.tomato.water_level())
            self.assertGreater(0, self.tomato.fertilization_level())

    def test_get_name(self):
        self.assertEqual(type(self.tomato.get_name()), str)


if __name__ == "__main__":
    unittest.main()
