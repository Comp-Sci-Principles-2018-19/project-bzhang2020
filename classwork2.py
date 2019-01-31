import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
   # Add tests like these to your test suite ...
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55)  # 11 is not included in the list.




test_suite()