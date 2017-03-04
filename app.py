#!/usr/bin/env python
#
# Scripts in this repo start here
#


if __name__ == "__main__":
    ''' Main execution point. '''
    from euler.problem.problem1 import Problem1
    problem = Problem1()
    print "Euler Project Solutions:"
    print "Problem 1 - \t", problem.solution()
    if problem.isOK():
        print "OK"
    else:
        print "fail"

    from euler.problem.problem2 import Problem2
    problem = Problem2()
    print "Problem 2 - \t", problem.solution()
    if problem.isOK():
        print "OK"
    else:
        print "fail"
