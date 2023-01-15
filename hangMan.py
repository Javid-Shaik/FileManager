import random, time
  
def help():
	"""The Hangman game is a word guessing game. The goal is to correctly guess the word chosen by the computer before the hangman is fully drawn.

                        Here are the rules
                       --------------------
1. The computer chooses a word at random from a list of words.

2. The player is given a certain number of chances (typically 6) to correctly guess the word.

3. The player can guess a letter at a time.

4. If the player guesses a letter that is in the word, the letter will be revealed in its correct position(s).

5. If the player guesses a letter that is not in the word, a part of the hangman will be drawn.

6. If the player correctly guesses the word before the hangman is fully drawn, they win.

7. If the hangman is fully drawn before the player correctly guesses the word, they lose.
"""
   
   
def selectCategory():
   wild_animals = ['Lion', 'Tiger', 'Bear', 'Wolf', 'Elephant', 'Gorilla', 'Leopard', 'Puma', 'Crocodile', 'Alligator',
   'Giraffe', 'Cheetah', 'Kangaroo', 'Rhinoceros', 'Zebra', 'Hippopotamus', 'Moose', 'Gazelle', 'Panther', 
   'Cougar', 'Antelope', 'Deer' , 'Wolverine']
   
   
   colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Black", "White",
   "Gray", "Gold", "Silver", "Bronze", "Turquoise", "Cyan", "Crimson", "Indigo", "Khaki", "Lilac",
   "Magenta", "Olive", "Periwinkle", "Raspberry", "Sage", "Tangerine", "Taupe", "Chartreuse", "Scarlet",
   "Slateblue", "Slategray", "Saddlebrown", "Peachpuff", "Plum", "Peach", "Lawngreen", "Mintcream", 
   "Midnightblue", "Seagreen", "Palevioletred", "Papayawhip", "Yellowgreen", "Thistle", "Tomato",
   "Turquoise", "Violet", "Wheat"]
   
   fruits = ['Apple', 'Banana', 'Mango', 'Watermelon', 'Pineapple', 'Grapes', 'Strawberry', 'Orange', 'Lemon', 
   'Kiwi', 'Peach', 'Pear', 'Plum', 'Blueberries', 'Cherries', 'Coconut', 'Cantaloupe', 'Honeydew', 'Raspberries', 
   'Blackberries', 'Pomegranate', 'Dragonfruit', 'Lime', 'Fig', 'Guava', 'Papaya']
   
   string_methods = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
   'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
   'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
   'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
   
   list_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
   
   dict_methods = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
   
   global_methods = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
   'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
   'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input',
   'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next',
   'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set',
   'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 'import']
   
   python_modules=['os', 'sys', 'math', 'random', 'json', 'datetime', 're', 'argparse', 'numpy', 'pandas',
   'urllib', 'requests', 'smtplib', 'sqlite3', 'csv', 'pickle', 'collections', 'itertools', 'logging', 'beautifulsoup4']
   
   mix_up = [colors,wild_animals,fruits,string_methods,list_methods,dict_methods,global_methods,python_modules,]
   cat = random.choice(mix_up)
   variable = [ i for i, j in locals().items() if j == cat][0]
   print("\nThe word belongs to the category : ->",variable)
   return cat
     
def hangman():
    hang = [
    "    _____________    ", 
    "   |             |   ", 
    "   |             0", 
    "   |            \|/", 
    "   |             | ", 
    "   |            / \ ", 
    " __|__     "
    ]
    word = random.choice(selectCategory()).lower()
    temp = word
    wlen = sn = len(word)
    s = ["_ "]*wlen
    print(*s)
    gc=2
    hc=0
    guess = []
    hint = ""
    while gc<8 and sn>0:
    	if hc<2 and gc>2 and wlen>=7:
    		hint = input("\nDo you want a Hint. Then Enter (y/n) : ")
    		if hint=="y":
    			let = random.choice(temp)
    			hc+=1
    	else:
    		hint="n"
    	
    	letter = let if hint=="y" else input("\nGuess a letter : ").strip()    	
    	if letter in guess:
    		print("You have already guessed that letter!\n")
    		continue
    	guess.append(letter)
    	
    	if letter!="" and letter in word:
    		print("\nGood job letter",letter,"is in the word!\n")
    		
    		for i in range(wlen):    			
    			if word[i]!=letter:
    				print(s[i],end=" ")
    			else:
    				s[i] = letter
    				temp=temp.replace(s[i],"")
    				sn-=1
    				print(s[i],end=" ")
    	else :
    		if 7-gc>=2:
    			print("You are",7-gc,"steps closer to get hanged!")
    		
    		elif 7-gc==1:
    			print("You are ",7-gc,"step closer to get hanged!")
    		
    		else:
    			print("You ran out of chances!!")
    		
    		for i in range(gc):
    			time.sleep(0.10)
    			print(hang[i])
    		gc+=1
    
    if gc>=8:
    	time.sleep(0.15)
    	print("\nYou lose! (-:")
    	print("\nThe secret word is : ",word)
    
    else :
    	print("\n\nWell done! You nailed it..!")
  
def main():
		print(help.__doc__)
		ch="p"
		while ch!="x":
			hangman()
			ch=input("\nEnter any key to play, or x to exit (p/x) : ")
		else:
			print("\nThanks for playing! Bye Bye!!")
main()
		
			