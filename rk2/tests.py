import unittest
from main import g1, g2, g3
from main import dets, dets_prods, prods


one_to_many = [(det.name, det.price, prod.name)
                   for prod in prods
                   for det in dets
                   if det.prod_id == prod.id]


many_to_many_temp = [(p.name, dp.prod_id, dp.det_id)
                     for p in prods
                     for dp in dets_prods
                     if p.id == dp.prod_id]

many_to_many = [(d.name, d.price, prod_name)
                for prod_name, _, det_id in many_to_many_temp
                for d in dets if d.id == det_id]


class Test(unittest.TestCase):
    def test_g1(self):
        self.assertEqual(g1(one_to_many), [('Шнур usb 3.0', 11, 'Apple'), ('Блок питания 12 v', 12, 'Apple'),\
                                           ('Блок питания 14 v', 16, 'Apple')])

    def test_g2(self):
        self.assertEqual(g2(one_to_many), [('Samsung', 10), ('LG', 15), ('Apple', 16)])

    def test_g3(self):
        self.assertEqual(g3(many_to_many), [('Кабель type-c', 10, 'Acronis'), ('Шнур usb 3.0', 11, 'Apple'),\
                                            ('Блок питания 12 v', 12, 'Apple'), ('Блок питания 14 v', 16, 'Apple'),\
                                            ('Шнур usb 2.0', 15, 'LG'), ('Шнур usb 2.0', 15, 'Microsoft'),\
                                            ('Шнур usb 3.0', 11, 'Panasonic'), ('Блок питания 12 v', 12, 'Panasonic'),\
                                            ('Блок питания 14 v', 16, 'Panasonic'), ('Кабель type-c', 10, 'Samsung')])


if __name__ == '__main__':
    unittest.main()


