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
def  escape_bridge(choice=None):
    print("the bridge collapses, you have two choices. You can use your tools to get [away] on bridge or choose to go [under] the bridge")
    if choice==None:
        choice=input("away or under")
    if choice=="away":
        print("the bridge is collapsing, but you survive")
        return "survive"
    if choice=="under":
        print("you die as pieces since bridge breaks down")
        return "die"
    
def fight(s,choice=None):
    print("you will face the lions and tigers that escaped from the zoo")
    if choice==None:
        choice=input("fight or flee")
    if choice=="fight" and s=="hammer":
        print("your hammer is not sharp enough, so you die")
        return "die"
    elif choice=="fight" and s=="knife":
        print(" you defeat the animals and you win")
        return "survive"
    else:
        print("if you choose to flee, as you are running away, the animal catches you and you die")
        return "die"
def battle():
    import random
    while True:
        rng = random.Random()    
        #Pick a random number between -1 and 1
        result = rng.randrange(-1,2)
        print( "winner={0}".format( result))
        return result

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(startgame("knife") == "knife")
    test(startgame("hammer") == "hammer")
    test(escape_bridge("away") == "survive")
    test(escape_bridge("under") == "die")
    
    test(fight("hammer", "flee") == "die")
    test(fight("knife", "flee") == "die")   
    test(fight("knife", "fight") == "survive")
    test(fight("hammer", "fight") == "die")
    
def main ():
    stuff=""
    if startgame()=="knife":
        stuff="knife"
        
    else:
        stuff="hammer"
    if escape_bridge()=="survive":
        if fight(stuff)=="survive":
            print("congradulation you won")
        else:
            print("you die, start again")
            main()
    else:
        main()
     
##test_suite()
#main()
battle()        