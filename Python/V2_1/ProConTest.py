from ProConListBST import Reason
from ProConListBST import PCList

def main():
	a = Reason("Because I'm Batman",100)
	b = Reason("Because Fuck you", -50)
	d = Reason("Because it's cool",200)
	e = Reason("Because it makes me look like a chav", -505)
	c = Reason("Because I'm the goat", 23)
	PCBST = PCList()
	PCBST.insert(a)
	PCBST.insert(b)
	PCBST.insert(c)
	PCBST.insert(d)
	PCBST.insert(e)

	List = PCBST.inorder([])
	for item in List:
		item.printBoth()
   

if __name__ == '__main__':
    main()