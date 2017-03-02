#!/usr/bin/env python
class Problem1:
    """ If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
    https://projecteuler.net/problem=1
    """
    def solution(self):
        return sum(self.selectCyphers())

    def selectCyphers(self):
        '''Select the cyphers for this problem'''
        return [x for x in range(0, 1000) if not x % 3 or not x %5]

    def isOK(self):
        '''Check that solution returns the valid value'''
        return self.solution() == 233168;
