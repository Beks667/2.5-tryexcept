import random 


names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']

l = len(names)
b = names[random.randint(0,l)]
with open (b,'w') as w:
	w.write('Beksultan')

def func (names):
	for i in names:
		try:
			with open (i,'r')as w:
				print("fail est")
		except FileNotFoundError :
			print('file not found!')

func(names)
