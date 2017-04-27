import os.path

def fileExists(fName):
    if os.path.isfile("./Data/{0}/q.csv".format(fName)) and os.path.isfile("./Data/{0}/o.csv".format(fName)) and os.path.isfile("./Data/{0}/a.csv".format(fName)):
        return True
    else:
        return False

def appendData(data):
    #Data: [Module, Question, [Options], [Answers]]
    print("appending")
    fDataQ = open("./Data/{0}/q.csv".format(data[0]), 'a')

    question = ""
    question += ";"
    question += "{0}".format(data[1])

    fDataQ.write(question)
    fDataQ.close()

    fDataO = open("./Data/{0}/o.csv".format(data[0]), 'a')

    options = ""
    options += ";"
    options += "{0}".format(data[2])
    options = options.replace("'", "")
    options = options.replace("[", "")
    options = options.replace("]", "")

    fDataO.write(options)
    fDataO.close()

    fDataA = open("./Data/{0}/a.csv".format(data[0]), 'a')

    answers = ""
    answers += ";"
    answers += "{0}".format(data[3])
    answers = answers.replace("]", "")
    answers = answers.replace("]", "")

    fDataA.write(answers)
    fDataA.close()

def createData(data):
    #Data: [Module, Question, [Options], [Answers]]
    print("Writing")
    fDataQ = open("./Data/{0}/q.csv".format(data[0]), 'w')

    question = "{0}".format(data[1])

    fDataQ.write(question)
    fDataQ.close()

    fDataO = open("./Data/{0}/o.csv".format(data[0]), 'w')

    options = ""
    options += "{0}".format(data[2])
    options = options.replace("'", "")
    options = options.replace("[", "")
    options = options.replace("]", "")

    fDataO.write(options)
    fDataO.close()

    fDataA = open("./Data/{0}/a.csv".format(data[0]), 'w')

    answers = ""
    answers += "{0}".format(data[3])
    answers = answers.replace("[", "")
    answers = answers.replace("]", "")

    fDataA.write(answers)
    fDataA.close()

def handleData(mNum, kind):
    if kind == "q":
        q = open("./Data/{0}/q.csv".format(mNum), "r")
        return q.read()
        q.close()

    elif kind == "o":
        o = open("./Data/{0}/o.csv".format(mNum), "r")
        return o.read()
        o.close()

    elif kind == "a":
        a = open("./Data/{0}/a.csv".format(mNum), "r")
        return a.read()
        a.close()
