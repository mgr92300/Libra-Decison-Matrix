import os

def getScript(fileHandleR = "Test"):
    file = open(f'{fileHandleR}.txt', 'r')
    text = ""
    for line in file:
        text += line
    return(text)

def promptFilter(Script):
    for line in Script:
        #print(line)    #Checks by printing each character
        if '*' in line:
            input(line)

def QuestionFilter(Script):
    questionList = []
    for line in Script:
        if '?' in line:
            questionList.append(line)
    return questionList
def main():
    Intro = getScript("Intro")
    promptFilter(Intro)
    print(Intro)    

if __name__ == '__main__':
    main()