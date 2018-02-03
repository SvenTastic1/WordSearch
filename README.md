# WordSearch
For storing a word search program and it's short manual

This python program can take in a string that represents a NxM grid as used in square word search puzzles.
When the program is ran, it takes a series of user inputs. The first required input specified the number
of rows the word search grid has. The user input should be an integer value like 14. The second required
input specifies the number of columns of the grid and also takes an integer value. An example follows:

a d r i q
b n a a n
b o l k d
a h f l s    (shown as a grid in raw file)

number of rows?: 4
number of columns?: 5

The third user input takes a string that should specify the contents of the word search grid. The entire grid has to
be manually entered, ordering the letters in the grid from the top left to the bottom right, moving through the columns 
horizontally before moving to the next row. The example entry for the example word search grid is as follows:

all letters of the puzzle grid in lower cases?: 'a d r i q b n a a n b o l k d a h f l s'

The program will automatically turn this one-dimensional string into the two dimensional grid using the specified number 
of rows and columns by the user. If there is a mismatch between the expected number of entries (rows x columns) and the entered
number of entries, the program specifies what went wrong and terminates. The space-separated letter entries are automatically
stored as separate values in a list and the length of this list determines the 'amount' of entered letters.

After the grid has been properly defined, the fourth user entry specifies the number of words that will be searched for
in the grid. The example grid will contain six words (Dutch and Memetics, so don't worry if you cannot recognize them yourself).
After entering the number of words as an integer value, a string has to be entered again specifying the exact words. It will
be separated by spaces again, just like the grid defining input. Example:

number of words?: 6
which words?: 'bnaan abba klob hond ralf bof'

After this, all required user input is known and the program returns the locations of the words. It will give the location
of the first letter of a word and then say which direction the word spans into. For example:

The word hond has been found in row 4, column 2 and spans upwards.
The word klob has been found in row 3, column 4 and spans to the left.
etc. 

P.S.
  Entering the entire word search grid can be tiresome, so any standardized procedure could be cool. I will not personally work
  on this.


