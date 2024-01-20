import os
import ProConListBST

#Make Too Many Options Statefule. Have it remember the options and then be able to delete them for anothr round

def getScript(fileHandleR = 'Test', Title = "Intro"):
    file = open(f'{fileHandleR}.txt', 'r')
    text = ''
    for line in file:
        text += line
    print(text)
    
def main():
    getScript()

if __name__ == '__main__':
    main()