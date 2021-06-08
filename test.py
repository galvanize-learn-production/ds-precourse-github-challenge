"""Unit Tests for Student Submission"""
import unittest
import distributions as student_dists
from scipy.stats import poisson, binom, geom
from inspect import getsource


class Test(unittest.TestCase):
    def test_binomial(self):
        msg = "\n\nYour binomial pmf is not implemented correctly."
        n, p = 12, 0.5
        student_binom = student_dists.binomial_pmf
        student_solution = {k: student_binom(n, p, k) for k in range(1, 25)}
        target_solution = {k: binom.pmf(k, n, p) for k in range(1, 25)}
        self.assertEqual(target_solution, student_solution, msg=msg)

    def test_poisson(self):
        msg = "\n\nYour poisson pmf is not implemented correctly."
        student_pois = student_dists.poisson_pmf
        lam = 10
        student_solution = {k: student_pois(k, lam) for k in range(1, 25)}
        target_solution = {k: poisson.pmf(k, lam) for k in range(1, 25)}
        self.assertEqual(target_solution, student_solution, msg=msg)

    def test_geometric(self):
        msg = "\n\nYour geometric pmf is not implemented correctly."
        student_geom = student_dists.geometric_pmf
        p = 0.25
        student_solution = {k: student_geom(k, p) for k in range(1, 25)}
        target_solution = {k: geom.pmf(k, p) for k in range(1, 25)}
        self.assertEqual(target_solution, student_solution, msg=msg)
    
    def test_no_imports(self):
        msg = "\n\nToo many 'import' statements! You may only import 'math'."
        src = getsource(student_dists)
        self.assertLessEqual(src.count("import"), 1, msg=msg)


if __name__ == "__main__":
    print("running tests . . .")
    unittest.main()
