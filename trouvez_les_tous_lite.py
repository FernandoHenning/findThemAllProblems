
dictionary = {"grand" ,"mere" ,"grandmere" ,"possede" ,"un" ,"coffre" ,"fort" ,"coffrefort" ,"dans" ,"sa" ,"bassecours" ,"basse" ,"cours" ,"ma"}


def toutes_les_phrases(string):
    """Main function. this function consists of calling the function diviser_phrase(string,n,result) with the appropriate parameters.

    Args:
        string (string): The sentence without spaces
    """
    diviser_phrase(string, len(string),"")
 

def diviser_phrase(string, n, result):
    """This recursive function will build and print all the phrases that it is possible to form from the string

    Args:
        string (_type_): The sentence without spaces
        n (_type_): Size of the sentence
        result (string): The final string made of all prefix found
    """
    # Process all prefixes one by one
    for i in range(1, n + 1):
        # Extract substring from 0 to i in prefix
        prefix = string[:i]
        # If dictionary contains this prefix, then
        # we check for remaining string. Otherwise
        # we ignore this prefix (there is no else for
        # this if) and try next
        if prefix in dictionary:
            # If no more elements are there, print it
            if i == n:
                # Add this element to previous prefix
                result += prefix
                print(result)
                return
            diviser_phrase(string[i:], n - i, result+prefix+" ")
 
def main():
    toutes_les_phrases("magrandmerepossedeuncoffrefortdanssabassecours")
if __name__ =="__main__":
    main()

    