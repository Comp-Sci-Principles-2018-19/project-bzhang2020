import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def startgame(choice=None):
    print("The main character wakes up under a broken bridge. You would find a box under the bridge and you have to choose the tools in there.")
    if choice==None:
        choice=input("knife or hammer")
    if choice=="knife":
        return "knife" 
    else :
        return "hammer"
    
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(startgame("knife") == "knife")
    
startgame()
test_suite()