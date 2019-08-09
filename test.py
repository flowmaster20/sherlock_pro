import unittest
from functions import *
from run import *
"""
File with tests that are running every time that project is pushed to github
if you want to trigger them manualy run this file

"""
class TestSherlockPro(unittest.TestCase):

    def test_create_mutations(self):
        input = "dom"
        ex_output = ["d","do","dom"]
        msg = "should be [\"d\",\"do\",\"dom\"]"
        self.assertEqual(create_mutations(input),ex_output,msg)

    def test_prepare(self):
        ex_output = {'mkoj', 'mateusz', '3', '2000', 'mateu', 'mkojro', 'koj', '0', 'mara', 'mateus', 'mkojro2', 'kojro', '2', '1', 'matr', '16', 'k', '200', 'marato', 'kojr', 'mate', 'matri', 'mat', 'mkojro20', '18', '20', '30', 'mati', 'matrix', 'ko', 'mk', '06', 'mko', 'mkojr', 'm', 'ma', 'mar', 'marat', 'maraton'}
        msg = "wrong output from main function"
        self.assertEqual(prepare("mateusz","kojro",["16","18"],["mati"],["30","06","2000"],["maraton"],["mkojro20","matrix"]),ex_output,msg)

    def test_idioticly_create_combintations(self):
        input = ["1","2"]
        ex_output = ["111","112","121","122","211","212","221","222"]
        ex_output.sort()
        msg = "creating combinations failed"
        self.assertEqual(idioticly_create_combinations(input),ex_output,msg)


if __name__ == '__main__':
    unittest.main()
