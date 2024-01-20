from random import randint

def Set_Up():
    Problems= ['Too Many Options', '50/50 Split', 'Should I or Shouldn\'t I?', 'Pros and Cons List']
    for x , y in enumerate(Problems):
        print(f"{x} : {y}")
    try:
        Problem = int(input('Please State Your Type of Problem: '))
    except:
        print('Te Crees. Okay, go off hunny. Ignore me.')
        print('I\'m just trying to help you but nooooooooooooooooooooo.')
        print('Pikachu no listen.')
        print('Ugly ass.')
        Problem = int(input('Enter a Number Pendejo: '))
    return Problem

def Too_Many_Options():
	Option_List = []
	Option = int(input('Please Enter How Many Options There are: '))
	Counter = 0
	while Counter < Option:
		Options = input('Please insert an option: ')
		Option_List.append(Options)
		Counter += 1
	Choice = randint(0,Option-1)
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
				Print('Don\'t Do it hun. You don\'t have anything to prove.')
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
					Print('You were doing so well until you wanted to be the funny man... smh')
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

def Reasoning(Weight, Pro_Flag):
    if Pro_Flag:
        Pro_Reasoning_List = []
        while Weight <  100 :
            Reasoning = input("Input Reasoning: ")
            Weight_Given = int(input("How significant is this reasoning? "))
            if Weight + Weight_Given > 100:
                print("REACHING CRITICAL MASS, EXPECT CONCLUSION SOON")
                Weight_Given = 100 - Weight
                Weight += Weight_Given
            elif Weight + Weight_Given == 100:
                print("Perfect, 100 Percent Download complete")
                Weight += Weight_Given
            Pro_Reasoning_List.append((Reasoning,Weight_Given))
            Weight += Weight_Given
        return Pro_Reasoning_List
    else:
        Con_Reasoning_List = []
        while Weight <  100 :
            Reasoning = input("Input Reasoning: ")
            Weight_Given = int(input("How significant is this reasoning? "))
            if Weight + Weight_Given > 100:
                print("REACHING CRITICAL MASS, EXPECT CONCLUSION SOON")
                Weight_Given = 100 - Weight
                Weight += Weight_Given
            elif Weight + Weight_Given == 100:
                print("Perfect, 100 Percent Download complete")
                Weight += Weight_Given
            Con_Reasoning_List.append((Reasoning,Weight_Given))
            Weight += Weight_Given
        return Con_Reasoning_List

def Pros_And_Cons():
    Highest_Reason_List = []
    Problem = input("Please input the tough choice: ")
    print("Now write your reasonings and how important they are in their respective columns.")
    print("Side note: all weights are in percentages so they should add to 100 percent.")
    print("Pros-")
    Pro_Reasoning_List = Reasoning(0,True)
    print("Cons-")
    Con_Reasoning_List = Reasoning(0, False)
    Highest_Pro_Reason = max(Pro_Reasoning_List)
    Highest_Con_Reason = max(Con_Reasoning_List)
    if Highest_Pro_Reason[1] > Highest_Con_Reason[1] :
        Verdict = 'all for doing what you have to do'
        print("Given all the data, The Gods have Come to a conclusion")
        print(f"Because {Highest_Pro_Reason[0]}, I am {Verdict}.")
    elif  Highest_Pro_Reason[1] == Highest_Con_Reason[1] :
        print("You really are torn up.")
        print("I would suggest trying a Should I Shouldn't I.")
    else:
        Verdict = 'against whatever your petty problems are'
        print("Given all the data, The Gods have Come to a conclusion")
        print(f"Because {Highest_Con_Reason[0]}, I am {Verdict}.")

def Problem_Type(Problem):
    if Problem ==   0:
        Too_Many_Options()
    elif Problem == 1:
        Fifty_Fifty_split()
    elif Problem == 2:
        To_Be_Or_Not_To_Be()
    elif Problem == 3:
        Pros_And_Cons()

def Fin():
	print('If you aren\'t satisfied with your result, do it again!')
	print('Or realize that you actually know what you want all you have to do is decide it pussy.')

def main():
    Problem = Set_Up()
    Problem_Type(Problem)
    Fin()

if __name__ == '__main__':
    main()
