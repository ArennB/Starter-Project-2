import unittest
import sys

sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle

 TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

class TestSuite_Complete_Coverage(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(True, True)

class TestSuite_Qu_and_St(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(True, True)

# -------------------------------
# ADDITIONAL TEST CASES
# -------------------------------

class TestSuite_Additional(unittest.TestCase):

    def test_diagonal_word(self):
        grid = [["A","B","C"], ["D","E","F"], ["G","H","I"]]
        dictionary = ["AEI"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["AEI"]
        self.assertEqual(solution, expected)

    def test_large_grid_scalability(self):
        grid = [
            ["C","A","T","S","X"],
            ["D","O","G","S","Y"],
            ["R","A","T","Z","Q"],
            ["B","I","R","D","W"],
            ["F","I","S","H","E"]
        ]
        dictionary = ["CATS","DOG","RAT","BIRD","FISH"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["CATS","DOG","RAT","BIRD","FISH"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_qu_handling(self):
        grid = [["Q","U","A"], ["B","C","D"], ["E","F","G"]]
        dictionary = ["QUA"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["QUA"]
        self.assertEqual(solution, expected)

    def test_case_insensitivity(self):
        grid = [["a","b"], ["c","d"]]
        dictionary = ["ABCD"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABCD"]
        self.assertEqual(solution, expected)

    def test_no_matching_words(self):
        grid = [["A","B"], ["C","D"]]
        dictionary = ["XYZ","MNO"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), [])

    def test_word_too_long(self):
        grid = [["A","B"], ["C","D"]]
        dictionary = ["ABCDE"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(mygame.getSolution(), [])

    def test_multiple_words(self):
        grid = [["C","A","T"], ["D","O","G"], ["R","A","T"]]
        dictionary = ["CAT", "DOG", "RAT", "CAR"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["CAT","DOG","RAT"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_complex_paths(self):
        grid = [["T","A","P"], ["S","E","R"], ["N","O","L"]]
        dictionary = ["TAP","TEN","SON","PAT","NOSE"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["TAP","TEN","PAT","NOSE"]
        self.assertEqual(sorted(solution), sorted(expected))

if __name__ == "__main__":
    unittest.main()
