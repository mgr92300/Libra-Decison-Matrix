import os
import ProConListBST

#Impelement BST Pro Con List

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