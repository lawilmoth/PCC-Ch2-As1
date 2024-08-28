"""For this assignment, you will need to follow the directions for each of the examples functions below."""


def hello_world():
    """This problem should print hello
    To solve this
    1. Delete the word pass.
    2. Uncomment the print statement"""
    pass
    #print("hello")


#This calls the function to test if it is working. You can delete it when you are done testing it, and call the function you are working on.
hello_world()

def problem_one():
    """Create a variable called 'name' and set it equal to your name,
    then print 'Hello <name>' 
    be sure to delete the pass."""
    name = ""

    return name

def problem_two():
    """Use the strip method remove the whitespace """
    x = "                               \t\t          \n          <( o-o )>\n\n\t\t\t          \t"

    #Add the left strip to remove whitespace on the left
    ls = x
    print(ls)
    #Add the right strip to remove whitespace on the right
    rs = x
    print(rs)
    #Add a method to remove all whitespace
    s = x
    print(s)
    return x, ls, rs, s


def problem_three():
    """Use the appropriate string methods to solve the problems"""
    x = "WE ARE the KNights WHO SAY ni!"

    #Use the appropriate method to write this in all capital letters
    caps = x
    print(caps)

    #Use the appropriate method to write this in all lowercase letters
    lower = x
    print(lower)
    #Use the appropriate method to write this in title case
    title_case = x
    print(title_case)

    return x, caps, lower, title_case
