#Threapy Simulator Program

def getReply(line):
    lowLine = line.lower()
    words = lowLine.split()
    if len(words) == 0:
        return "You have to talk to me :("
    elif line[-1] == "?":
        return "Why do you want to know?"
    elif "mother" in words:
        return "Tell me more about your mother."
    elif "father" in words:
        return "Tell me more about your father."
    elif "uncle" in words:
        return "Tell me more about your uncle."
    elif "sister" i words:
        return "Tell me more about your sister."
    elif "brother" in words:
        return "Tell me more about your brother."
    elif words[0] == "i" and words[1] == "feel":
        return "Why do you feel that way?"
    elif words[0] == "i" and words[1] == "think":
        return "Do you really think so?"
    else:
        return "Tell me more."

def therapy():
    name = raw_input("Hello, Welcome To Therapy. What is your name?")
    print "Type quit any time you want to finish."
    line = raw_input("Well" + name + ", What can we do for you today?")
    while line != "quit":
        reply = getReply(line)
        line = raw_input(reply + "")
    print "Goodbye!"

therapy()
