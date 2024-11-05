import logging
import AA12
import unittest


logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')




class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            nik = AA12.Runner('Nikita', -5)
            logging.info('"test_walk" выполнен успешно',exc_info=True)
            for _ in range(10):
                nik.walk()
            self.assertEqual(nik.distance, 50)
        except ValueError:
             logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            nikita = AA12.Runner(1, 5, 100)
            for _ in range(10):
                nikita.run()
            self.assertEqual(nikita.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


    def test_challenge(self):
        niki = AA12.Runner('Niki')
        ta = AA12.Runner('Ta')
        for _ in range(10):
            niki.walk()
            ta.run()
        self.assertEqual((niki.distance,ta.distance), (50,100))



if __name__ == '__main__':
    a = RunnerTest()

    print(a.test_walk())
    print(a.test_run())





