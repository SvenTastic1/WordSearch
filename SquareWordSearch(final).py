puzrow = int(input('Please enter the amount of rows the puzzle has as an integer (3 not three): '))
puzcol = int(input('Please enter the amount of colums the puzzle has as an integer (7 not seven): '))
puzlayout = input('Please enter as a string (start and end with quotation marks)' '\n' 'in order from top left to bottom right' '\n' 'horizontally all letters of the puzzle grid in lower cases: ')
search1d = puzlayout.split(' ', puzrow*puzcol-1)

#Check to see if the parsing from space-separation went okay: it will return the final element if it contains
#spaces which means too little values were created compared to the entered letters in puzlayout. The program
#should create entered row*column entries. If more letters were entered this error will trigger. 
if ' ' in search1d[-1]:  #Checks to see if the last element is 
	print 'You specified the grid should countain',puzrow*puzcol,'elements, but you typed in more'
	print 'The final mined entry looks like this: ',search1d[-1]
	exit()
#if too little variables were entered this error will trigger
elif puzrow*puzcol != len(search1d):
	print 'You specified the grid should contain',puzrow*puzcol,'elements, but you specified',len(search1d),'elements.'
	exit()
else: 
	pass

#Turns the one-dimensional list of letters into the two-dimensional grid for the word search.
#First a list with the right dimensions but only 0 as entries is created;
#Then the lists contained in this list (the 'rows') are filled iteratively with the first:last entries
#of the search1d list. The first entry of a row starts at 0 and increases as follows: if there are 5
#columns, we would expect the first row to have as many entries as columns -> this means the first entry
#of the second row is 0+puzcol (the amount of columns) and this generalizes nicely: the first entry of the
#third row is 0+2*puzcol etc. -> since i keeps track of the row number, it can be multiplied with the amount
#of columns to create the first positon of that row (the first row has value 0 in Python). Similar logic applies to the
#last entry of a row. 
search2d = [[0 for i in range(puzcol)] for n in range(puzrow)]
for i in range(len(search2d)):
	search2d[i] = search1d[0+i*puzcol:puzcol+i*puzcol]
print(search2d)

#Enter the words that should be present in the word search grid
nwords = input('Specify how many words to seek as an integer value: ')
nwords = int(nwords)
wordsearch = input('Please enter the words that should be present as one string, separating the words by spaces: ')
wordlist = wordsearch.split(' ', nwords-1)

#Define the function that does an extensive search through the whole two-dimensional word grid
#It starts with the first letter of a word and then searches if the string exists in any direction:
#Right, Left, Upwards 
def find_words_puzzle(puzrow, puzcol, workword, search2d):
	for i in range(0,puzrow):
		nw = 0
		for j in range(0,puzcol):
			if workword[nw] in search2d[i][j]:	#If the first letter of the word is in an exact location
				#To the right ->
				colright = j+1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[i][colright]:
						colright += 1
						nextlet += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned to the right.'
							return 'right'	#The word has been identified and the function can be exited			
				except Exception:
					pass #Skip over index errors since there is no point in writing verbose code to prevent it from happening: it is easier to pass over the error
				#To the left <-
				colleft = j-1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[i][colleft]:
						nextlet += 1
						colleft -= 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned to the left.'
							return 'left'
				except Exception:
					pass #Skip
				#Upwards
				rowup = i-1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowup][j]:
						nextlet += 1
						rowup -= 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned upwards.'
							return 'up'
				except Exception:
					pass #Skip	
				#Downwards
				rowdown = i+1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowdown][j] and rowdown>=0 and rowdown<puzrow:
						nextlet += 1
						rowdown += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned downwards.'
							return 'down'
				except Exception:
					pass #Skip			
				#Diagonal: up right
				rowup = i-1
				colright = j+1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowup][colright] and rowup>=0 and colright>=0 and rowup<puzrow and colright<puzcol:
						rowup -= 1
						colright += 1
						nextlet += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned diagonally up to the right.'
							return 'diagonal up right'
				except Exception:
					pass #Skip			
				#Diagonal: up left
				rowup = i-1
				colleft = j-1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowup][colleft] and rowup>=0 and colleft>=0 and rowup<puzrow and colleft<puzcol:
						rowup -= 1
						colleft -= 1
						nextlet += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned diagonally up to the left.'
							return 'diagonal up left'
				except Exception:
					pass #Skip		
				#Diagonal: down right
				rowdown = i+1
				colright = j+1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowdown][colright] and rowdown>=0 and colright>=0 and rowdown<puzrow and colright<puzcol:
						rowdown += 1
						colright += 1
						nextlet += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned diagonally down to the right.'
							return 'diagonal down right'
				except Exception:
					pass #Skip		
				#Diagonal: down left
				rowdown = i+1
				colleft = j-1
				nextlet = nw+1
				try:
					while workword[nextlet] in search2d[rowdown][colleft] and rowdown>=0 and colleft>=0 and rowdown<puzrow and colleft<puzcol:
						rowdown += 1
						colleft -= 1
						nextlet += 1
						if nextlet is len(workword):
							print 'the word',workword,'has been found in row',i+1,'column',j+1,'and is spanned diagonally down to the left.'
							return 'diagonal down left'
				except Exception:
					pass #Skip

#Execute for all specified words
for word in wordlist:
	find_words_puzzle(puzrow, puzcol, word, search2d)







