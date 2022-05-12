# Find them all: LITE
You have at your disposal: 
- A valid sentence (in French) without spaces, for example: "Ceciestunephrasevalide".
- A list of words (dictionary), e.g. " Ceci ", " une ", " phrase ", " est ", " valide ".

From these two elements, determine all the possible ways to break down the sentence into 
single words from the word list.
So, we ask you to write a small Python program that uses
a string and a dictionary of words stored in a set.
In this program you need to add spaces to the string to build sentences where each word 
belongs to the set. Each word can be used more than once. Display (on the terminal) all 
possible sentences.That is, the sentences that can be formed by keeping the order of the 
words in the order of the words in the initial sentence (without spaces)

To do this task, we ask you to implement two Python functions:

-  diviser_phrase(string,n,result) This recursive function will build and print (display on the terminal) all the phrases that it is possible to form from the string. We start scanning the sentence from the left. When a valid word (belonging to the set) is found, you should check whether the rest of the sentence can contain valid words or not. Here is what the first call to your function will look like: diviser_phrase (phrase_initiale_sans_espaces,len(phrase_initiale_sans_espaces),””). So, it is in the result parameter that we will build each of the sentences solutions.
-  toutes_les_phrases(phrase) which is a one-line function, this line consists of calling the function diviser_phrase(string,n,result) with the appropriate parameters. The function toutes_les_phrases(phrase) take as parameters the sentence without spaces. These two functions will be implemented in the file trouvez_les_tous_lite.py which contains the function toutes_les_phrases(phrase) of a line and which calls your function diviser_phrase (string,n,result).

Here are a few examples:
Sentence: ”magrandmerepossedeuncoffrefortdanssabassecours ”\
Dictionary of words:
```
{” grand” , ”mere ” , ” grandmere ” , ” possede ” , ”un ” , ” coffre ” , ” fort ,” coffrefort” , ” dans ” , , ” sa ” , ” bassecours” , ” basse ” , ” cours” , ”ma”} 
```
Result:
ma grand mere possede un coffre fort dans sa basse cours
ma grand mere possede un coffre fort dans sa bassecours
ma grand mere possede un coffrefort dans sa basse cours
ma grand mere possede un coffrefort dans sa bassecours
ma grandmere possede un coffre fort dans sa basse cours
ma grandmere possede un coffre fort dans sa bassecours
ma grandmere possede un coffrefort dans sa basse cours
ma grandmere possede un coffrefort dans sa bassecours

---

# Find them all: PRO
The Find Them All game is played with an N × N square grid containing
a set of letters as shown in Figure 1a, and a previously known list of words as
known beforehand as shown in Figure 1b

![Alt text](/images/figure%201.png?raw=true "Title")

The goal of the game is to find all the words in the given list from a
letters in the grid, where a word can be formed by using adjacent letters (top, bottom, 
left, right and diagonal). No letter can be used more than once.
So, a path must be drawn through the adjacent letters. Two letters are considered 
adjacent if they are next to each other horizontally, vertically or diagonally. Each letter
of the grid has at most eight adjacent letters, as shown in Figure 2.

![Alt text](/images/figure%202.png?raw=true "Title") 

So, you can start with any letter, and all letters around it are accepted. Once you move on to 
the next letter, all the letters that are around it are accepted, except for the letters previously used, and so on.\
As an example, in the grid in Figure 3, by following the steps shown, we succeed in finding the word "Algorithme".

![Alt text](/images/figure%203.png?raw=true "Title")

Your mission is to write a program that will simulate this little game. Your
program will first have to build and store the game grid, then it will have to
browse this grid in order to find all the words present in the list of valid words corresponding 
to this grid.
Implementation
In the file trouvez_les_tous_pro.py we ask you to implement a
TLT class that will contain the grid of the game which will be in the form of a 
N ×N MATRIX. The class will also contain the list of possible words to form from 
the grid. For this class, it is required to implement the following methods:
- Two methods retrieve grid (file name) and retrieve possible words (file name) which will read in a the information needed to build a game grid, as well as the list of words that it is possible to the list of words that can be formed from this grid.

This list will allow you to check that each word found in the grid
is among the possible solutions. If it does not appear, then this word
should not be considered. In order to test your program, several
txt files will be provided with the statement. 
The file will be structured as follows:

![Alt text](/images/figure%204.png?raw=true "Title")

- The first line of the file will contain the size (N) of the grid.
- N lines representing the grid of the game, each character being separated by a comma.
- A number M of words representing the list of valid words that your program will have to find.

The methods retrieve grid (file name)
and retrieve possible words(filename) take as parameter a
file name (for example: "grille 1.txt"), place the corresponding file in the same directory as 
your file trouvez_le_ tous_pro.py.
a prefix method (word list) which takes as parameter the list of
valid words (present in the txt file and that returns all prefixes.
For simplification reasons, the prefixes of a word in our case
represents the set of substrings whose size is equal to
two minimum and the size of the word - 1 maximum. For example, the
prefixes of Python are [Py, Pyt, Pyth, Pytho]. This method will allow you to make an 
optimization that will avoid taking long coffee breaks
while the computer futilely searches for words like zxgub, zxaep, etc... although in the French 
language, there is no word beginning with ZX.
- a method trouver_mots_rec which allows to build all the words that it is possible to create starting from a character of the grid. You will use the concept of backtracking: as soon as you realize that you cannot form the word  starting at a position, you move to the next position. Be sure to use the prefix method to abandon searches that have no results.
- a trouver_tous_les_mots method which uses trouver_mots_rec and which will search the whole grid in order to find all the words that can be found on the board. It is of course strongly encouraged to implement other functions/methods to make your life easier

## Find them all PRO test:
To find out if your program is working properly you need to:
- The number of words that your program finds from the grid is equal to the number of words in the given list. We strongly encourage you to implement a method to do this verification.
- the execution time is reasonable
