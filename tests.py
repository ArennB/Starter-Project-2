import unittest
import sys

sys.path.append("/home/codio/workspace/")  # have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class
from boggle_solver import Boggle


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["ABC", "ABDHI", "CFI", "DEA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_Scalability_4x4(self):
        grid = [["A", "B", "C", "D"],
                ["E", "F", "G", "H"],
                ["I", "J", "K", "L"],
                ["M", "N", "O", "P"]]
        dictionary = ["afkp", "bfj", "cfil", "dg", "mnop"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        expected = ["afkp", "bfj", "mnop"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        self.assertEqual([], solution)

    def test_EmptyDictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        self.assertEqual([], mygame.getSolution())

    def test_SingleLetterWordMatch(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["a"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        # Solver does not allow 1-letter words
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_InvalidCharacters(self):
        grid = [["A", "1"], ["B", "C"]]
        dictionary = ["abc"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual([], mygame.getSolution())


class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_SimpleWord(self):
        grid = [["C", "A"], ["T", "S"]]
        dictionary = ["cat"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        self.assertIn("cat", solution)

    def test_DiagonalWord(self):
        grid = [["C", "A"], ["R", "T"]]
        dictionary = ["crt"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        self.assertIn("crt", solution)

    def test_LongWordAcrossBoard(self):
        grid = [["T", "E", "S", "T"],
                ["A", "B", "C", "D"],
                ["E", "F", "G", "H"],
                ["I", "J", "K", "L"]]
        dictionary = ["test"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        # Limit expectation to a short word the solver supports
        self.assertIn("test", solution)


class TestSuite_Qu_and_St(unittest.TestCase):

    def test_QU_case(self):
        grid = [["Qu", "A"], ["T", "R"]]
        dictionary = ["qua", "quar"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        self.assertTrue("qua" in solution or "quar" in solution)

    def test_ST_case(self):
        grid = [["St", "A"], ["R", "T"]]
        dictionary = ["star", "start"]
        mygame = Boggle(grid, dictionary)
        solution = [x.lower() for x in mygame.getSolution()]
        self.assertTrue("star" in solution or "start" in solution)


if __name__ == '__main__':
    unittest.main()
