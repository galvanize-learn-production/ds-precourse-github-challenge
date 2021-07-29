"""Probability mass functions for the Binomial, Poisson, and Geometric distributions"""
from math import exp, comb, factorial


def binomial_pmf(n, p, k):
    return comb(n, k) * (1 - p)**(n - k) * p**k


def poisson_pmf(k, lam):
    return lam**k * exp(-lam) / factorial(k)


def geometric_pmf(n, p):
    return (1 - p)**(n - 1) * p
