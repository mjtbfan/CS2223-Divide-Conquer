# Nicholas Delli Carpiini | 11/15/17
from time import perf_counter
import sys
import math
import ast

# Opens the file and catches any errors when trying to open / convert to tuple   
def openFile(name):
    if (name == ""):
        name = "input.txt"
    try:
        with open (name) as f:                               # ] Taken off of Canvas
            try:
                points = ast.literal_eval(f.read())          # ] Taken off of Canvas
            except (ValueError, SyntaxError) as error:       
                f.close()
                print("Error: Input File is Invalid, Please Check that the Input is in the Form")
                print("[(a,b),(b,c),(c,d),(e,f)...]")
                return 0
            f.close
            return points
    except FileNotFoundError:
        print("Error: File Not Found, Please Type the Correct Name / Make Sure the File is in the Same Folder as this File")
        return 0

# Prints the greeting an continually loops until the user gives it a valid file
def inputStatement():
    print("Welcome to the Divide & Conquer Algorithm Comparison")
    print("Please Put Your Input File in the Same Folder as this .py File")
    print("(If the File is name 'input.txt', Just Press Enter)")

    name = input()
    
    while True:
        if (openFile(name) == 0):
            name = None
            name = input()
            continue
        else:
            points = openFile(name)
            return points

# Gets the closest points using repurposed code from bruteForce
def closestPoints(points):
    for i in range(0,len(points)):
        for j in range((i + 1),len(points)):
            temp = math.sqrt((math.pow((points[i][0] - points[j][0]), 2) + math.pow((points[i][1] - points[j][1]), 2)))
            if (i == 0 and j == 1):
                final = temp
                finalPoint1 = points[i]
                finalPoint2 = points[j]
            else:
                if (temp < final):
                    final = temp
                    finalPoint1 = points[i]
                    finalPoint2 = points[j]
    return finalPoint1, finalPoint2;

# Uses a double loop to compare every possible combination of points
def bruteForce(points):
    for i in range(0,len(points)):
        for j in range((i + 1),len(points)):
            temp = math.sqrt((math.pow((points[i][0] - points[j][0]), 2) + math.pow((points[i][1] - points[j][1]), 2)))
            if (i == 0 and j == 1):
                final = temp
            else:
                if (temp < final):
                    final = temp
    return abs(final);

# Taken from the Project Sheet and edited to work with tuples
def efficient(xsorted, ysorted):
    if (len(xsorted) <= 3):
        return bruteForce(xsorted)
    else:
        x1 = xsorted[:len(xsorted)//2]
        y1 = ysorted[:len(ysorted)//2]
        x2 = xsorted[len(xsorted)//2:]
        y2 = ysorted[len(ysorted)//2:]
        
        d1 = efficient(x1, y1)
        d2 = efficient(x2, y1)
        d3 = min(d1, d2)
        
        m = xsorted[(len(xsorted))//2 - 1][0]
        s = ()
        for i in (0, len(ysorted) - 1):
            if(abs(ysorted[i][0] - m) < d3):
                s = s + (ysorted[i],)
        
        dminsq = d3* d3
        for j in range(0, (len(s) - 2)):
            k = j + 1
            while ((k <= (len(s) - 1)) and (pow(s[k][1] - s[j][1]) < dminsq)):
                dminsq = min(pow((s[k][0] - s[j][0]), 2) + pow((s[k][1] - s[j][1]), 2), dminsq)
                k = k + 1
    return math.sqrt(abs(dminsq))

# Prints the time in a more readable format using shorthand units and only 2 decimal places   
def printTime(ans): # ] REPURPOSED FROM GCD
    if (ans > 1e-02):
        print ("Time: %.2f" % ans, "s")
    if (ans <= 0.01 and ans > 0.00001):
        ans = ans * 1000
        print ("Time: %.2f" % ans, "ms")
    if (ans <= 0.00001 and ans > 0.00000001):
        ans = ans * 1000000
        print ("Time: %.2f" % ans, "\u00B5s")
    if (ans <= 0.00000001):
        ans = ans * 1000000000
        print ("Time: %.2f" % ans, "ns")

# Prints the final results
def printResults(points, xsorted, ysorted):
    print("\nInput Points:", points)
    print("Closest Points:", closestPoints(points))
    print("\nUsing Brute Force (Iteration)")
    print("Distance: %.2f units" % bruteForce(points))
    start = perf_counter()      # ] REPURPOSED FROM GCD
    bruteForce(points)          # ] Calculates the time seperately from printing the answer in order to give the most
    end = perf_counter()        # ] accurate time. Gets the uptime of the system before and after the function call and
    time = end - start          # ] then subtracts them, the uses printTime to make the numbers easier on the eyes
    printTime(time)             # ]
    
    print("\nUsing Efficient Closest Pair (Recursion)")
    print("Distance: %.2f units" % efficient(xsorted, ysorted))
    start = perf_counter()
    efficient(xsorted, ysorted)
    end = perf_counter()
    time = end - start
    printTime(time)
    
points = inputStatement()
xsorted = sorted(points, key=lambda tup: tup[0])
ysorted = sorted(points, key=lambda tup: tup[1])
printResults(points, xsorted, ysorted)


