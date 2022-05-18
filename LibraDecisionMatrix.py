from random import randint

def Set_Up():
    Problems= ['Too Many Options', '50/50 Split', 'Should I or Shouldn\'t I?']
    for x , y in enumerate(Problems):
        print(f"{x} : {y}")    
    try:
        Problem = int(input('Please State Your Type of Problem: '))
    except:
        print('Te Crees. Okay, go off hunny. Ignore me.')
        print('I\'m just trying to help you but nooooooooooooooooooooo.')
        print('SOMEONE doesn\'t want to listen.')
        print('Ugly ass.')
        Problem = int(input('Enter a Number Pendejo, 0-2: '))
    return Problem

def Too_Many_Options():
    Option_List = []
    Option = int(input('Please Enter How Many Options There are: '))
    _ = 0
    while _ < Option:
        Options = input('Please insert an option: ')
        Option_List.append(Options)
        _ += 1
    Choice = randint(0,Option-1)
    print(Choice)
    print('ALAKAZAM!')
    print(f'I pick {Option_List[Choice]}.') 
    print('You\'re Welcome.')
    print('Fucking Slut')

def Fifty_Fifty_split():
    index = 0
    Conditions = []    
    while index < 2:
        if index == 0:
            Condition = input('Please State First Condition: ')
        else:
            Condition = input('Please State the Other Condition: ')        
        Conditions.append(Condition)
        index += 1
    Choice = randint(0,1)
    print('The Gods have Spoken')
    print(f'They want you to {Conditions[Choice].lower()}!')        

def To_Be_Or_Not_To_Be():
    print("Answer in Yes or No only")
    User = True
    while User:
        Decision = input('Do you even want to do this at all? ').upper()
        if Decision == 'YES':
            Decision = input('Are you Being Pressured into doing this by anyone else? ').upper()
            if Decision == 'YES':
                print('Don\'t Do it hun. You don\'t have anything to prove.')
                User = False
            elif Decision == 'NO':
                Decision = input('Alright. Do you want to leave this to fate? ').upper()
                if Decision == 'YES':
                    print('Okay, It\'s Hit or Miss. I guess they really do never miss huh')
                    Fifty_Fifty_split()
                    User = False
                elif Decision == 'NO':
                    print('Well alright then, Why did you want to do this in the first place Lmao.')
                    User = False
                else:
                    print('You were doing so well until you wanted to be the funny man... smh')
                    User = False
            else:
                print('If you don\'t wanna answer right to a computer then go ask an adult child headass.')
                User = False
        elif Decision == 'NO':
            print('Then you don\'t have to do this hunty. Just keep doing you and live on.')
            User = False
        else:
            print('Alright Funny Man, I\'m a computer. I don\'t really care what happens.')
            User = False
            
def Problem_Type(Problem):
    if Problem == 0 :
        Too_Many_Options() 
    elif Problem == 1 :
        Fifty_Fifty_split()
    elif Problem == 2:
        To_Be_Or_Not_To_Be()

def Fin():
    print('If you aren\'t satisfied with your result, do it again!')
    print('Or realize that you actually know what you want all you have to do is decide it pussy.')


def main():
    Problem = Set_Up()
    Problem_Type(Problem)
    Fin()

main()

        

