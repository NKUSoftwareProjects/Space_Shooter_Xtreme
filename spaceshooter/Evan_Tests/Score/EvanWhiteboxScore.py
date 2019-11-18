
global score
score = 0
global gotScore
gotScore = 0

def calculateScore(radius):
    global score
    global gotScore
    if radius < 10:
        gotScore = 50
    elif radius == 10:
        gotScore = 500
    elif radius < 15:
        gotScore = 40
    elif radius < 30:
        gotScore = 30
    elif radius < 50:
        gotScore = 20
    elif radius < 55:
        gotScore = 10
    else:
        gotScore = 5
    score += gotScore

#----------- Start white box testing
with open("spaceshooter/Evan_Tests/Score/evan_whitebox_suite.txt", "r") as input_file:
    tests = input_file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
tests = [x.strip() for x in tests]

with open("spaceshooter/Evan_Tests/Score/evan_expected_values.txt", "r") as expected_file:
    expected = expected_file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
expected = [x.strip() for x in expected]
expected = [x.split(",") for x in expected]

with open("spaceshooter/Evan_Tests/Score/evan_whitebox_suite_output.txt", "w+") as output:
    for x in range(len(tests)):
        print(expected[x])
        radius = int(tests[x])
        calculateScore(radius)
        if (int(gotScore) == int(expected[x][0]) and score == int(expected[x][1])):
            output.write("Test " + str(x) + " PASSED ---------------------\n")
            output.write("Given radius: " + str(radius) + "\n")
            output.write("gotScore is: " + str(expected[x][0]) + "\n")
            output.write("Score is: " + str(expected[x][1]) + "\n")
            output.write("This matched the expected value: " + expected[x][0] + ":" + expected[x][1] + "\n\n")
        else:
            output.write("Test " + str(x) + " FAILED ---------------------\n")
            output.write("Given radius: " + str(radius) + "\n")
            output.write("gotScore is: " + str(expected[x][0]) + "\n")
            output.write("Score is: " + str(expected[x][1]) + "\n")
            output.write("This did not match the expected values: " + expected[x][0] + ":" + expected[x][1] + "\n\n")
        gotScore = 0

print("Done Testing")