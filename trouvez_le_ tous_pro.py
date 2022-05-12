import time

class TLT:
    
    def __init__(self, file_name = "grille_3.txt") -> None:
        
        self.grid_size = 0
        self.list_of_posibles_word = []
        self.game_grid = []
        self.retrieve_grid(file_name)
        self.retrieve_posible_words(file_name)
        
        self.prefix_list = self.prefix_method(self.list_of_posibles_word)
        
        # variables to make life easier 
        self.rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.colNum = [-1, 0, 1, -1, 1, -1, 0, 1]

    def retrieve_grid(self, file_name:str):
        """Retrieve grid function. Read the data of the grid from the given .txt file.

        Args:
            file_name (str): The name of the .txt file from which the data will be extracted.
        """
        with open(f'{file_name}') as f:
            self.grid_size = int(f.readline()) # The first line is always going to be the size of the N x N grid
            f.readline() # Remove the new line character (\n) in the next line.
            for _ in range(self.grid_size):
                row = f.readline().removesuffix('\n').split(',')  # Remove the new line character of the end of the line and split by ","" to create a list.
                self.game_grid.append(row)
            
             
    def retrieve_posible_words(self, file_name:str):
        """Retrieve posible words function. Read all the posibles words from the given .txt file.

        Args:
            file_name (str): The name of the .txt file from which the data will be extracted.
        """
        with open(f'{file_name}') as f:
            content = f.readlines() # Read all the lines from the .txt file
            words = content[3 + self.grid_size:] # Get only the lines of the words list. 3 (size of grid + 2 blank spaces) + size of the grid. = first words of the list.
            for i,word in enumerate(words):
                self.list_of_posibles_word.append(words[i].removesuffix('\n')) # remove the new line character at the end of the line and add the word to the list.
                
    def prefix_method (self ,words_list):
        """Prefix method fuction: Create all prefix form each word on the list. Prefix are a set of substrings whose size is equal to two minimum and the size of the word - 1 maximum

        Args:
            words_list (List): List of all the posibles words.

        Returns:
            List: List of all prefix of each word.
        """
        prefix_list = []
        for word in words_list: # Iterates for each word
            for i in range(2, len(word)): # Iterates each character of the word starting from the second to the size of te word - 1 character
                prefix_list.append(word[:i]) # Save each prefix
        return prefix_list
    
    
    def valid_positon(self, row, col, prevRow, prevCol):
        """Valid position. Function to check that the current position is within the grid boundaries.

        Args:
            row (int): Actual row value.
            col (int): Actual col value.
            prevRow (int): Previous row value.
            prevCol (int): Previous col value.

        Returns:
            bool: return the true value of the condition.
        """
        return (row >= 0) and (row < self.grid_size) and (col >= 0) and \
           (col < self.grid_size) and not (row== prevRow and col == prevCol)
    
    
    def trouver_mots_rec(self, row, col,prevRow, prevCol, word, formed_word,path, index, n):
        """_summary_

        Args:
            row (int): Current row value.
            col (int): Current col value.
            prevRow (int): Previous row value.
            prevCol (int): Previous col value.
            word (string): Word to be found
            formed_word (string): Current word formed. This is the one that is look in the prefix list
            path (string): Path of the word formed
            index (int): This value is to control the algorithm. Help to know when it started and when it is going to finish
            n (int): Size of the word to be found minus one.

        Returns:
            bool: Return True if the word have been found.
        """
    
        formed_word += self.game_grid[row][col] # add current character to the word
        if (formed_word == word): # if formed_word is equal to the word to search the algorithm ends.
            path += self.game_grid[row][col] + "(" + str(row)+ ", " + str(col) + ") " # add last character to the path
            print(f"Found : {formed_word} | Path : {path}") 
            return True
        if (formed_word  not in self.prefix_list and index > 0): # If formed_word not in the prefix list the algorithm ends. Index most be greater than zero 
                                                                 # because prefix start from the second character
            return False
        if (index > n ): # if index is greater that the word size the algorithm eds.
            return False
        
        
        path += self.game_grid[row][col] + "(" + str(row)+ ", " + str(col) + ") " # Update path with the new character
    
        output = []
        # Performs 8 iterations to check every possible movement in the grid and save the result.
        for k in range(8):
            if (self.valid_positon(row + self.rowNum[k], col + self.colNum[k],prevRow, prevCol)):
                output.append(self.trouver_mots_rec( row + self.rowNum[k], col + self.colNum[k],row, col, word, formed_word,path, index + 1, n)   )
        # The any() function returns True if any item in an iterable are true, otherwise it returns False.
        return any(output)

                
    def trouver_tous_les_mots(self):
        words_found = 0
        for word in self.list_of_posibles_word: # Iterates for each posible word
            found = []
            # iterates through the entire grid looking to see if the character at that position corresponds to the first character of the word to be searched for.
            for i in range(self.grid_size):                
                for j in range(self.grid_size):
                    if (self.game_grid[i][j] == word[0]): # if the current value is equals to the first character of the word it start searching for the word
                            found.append(self.trouver_mots_rec(i, j , -1, -1, word,"","", 0, len(word) - 1)) # save the results
                            
                 # The any() function returns True if any item in an iterable are true, otherwise it returns False.
                if any(found):
                    words_found+=1
                    break

        if words_found == len(self.list_of_posibles_word):
            print(f"All words have been found. Total found = {words_found} \t Total words in list = {len(self.list_of_posibles_word)}")
        else:
            print(f"Not all words have been found. Total found = {words_found} \t Total words in list = {len(self.list_of_posibles_word)}")

def main():
    
    file_name = "inputs/grille_3.txt"                 
    game = TLT(file_name)

    tic = time.perf_counter()
    game.trouver_tous_les_mots()
    toc = time.perf_counter()
    
    print(f"[{file_name}] words found in  {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()