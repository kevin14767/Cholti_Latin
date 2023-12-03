#Pywords integrated

# lookup is the main module
import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias

# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter

# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils
import pandas as pd

#excel sheet 
file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
#columns
column_to_read = "Standardized Ch'olti"
column_to_write = 'More Latin'


#method to process row by row 
def process_words(column_to_read, column_to_write):

    #read the excel
    df = pd.read_excel(file_path)
    #iterate through the rows 
    for index, row in df.iterrows():

        #words that are not latin written to output file
        missed_words = []

        #things written back to excel sheet
        latin_words_to_write = []
        missed_words_to_write = []  
        #data from the cell
        value = row[column_to_read]
        #if str(value).__contains__(";"):
            #value = str(value).replace(";","")

        #seperate through white space
        words = str(value).split(" ")

        #iterate through each word in the collection of words
        for word in words:
            #remove any non alphabetical characters
            s = ''.join(filter(str.isalnum, word))
            #keep a copy
            actual_word = s
            if is_latin(s):
                if str(s) != "nan" or str(s) != "":
                    #counter += 1
                    latin_words_to_write.append(actual_word)
                    #print(actual_word)
            else:
                if str(s) != "nan" or str(s) != "":
                    missed_words_to_write.append(actual_word)
                    missed_words.append(actual_word)
        

        latin_text = " ".join(latin_words_to_write)
        missed_text = " ".join(missed_words_to_write)
        df.at[index,column_to_write] = latin_text
        df.at[index, "Ch'olti & Spanish"] = missed_text
 
    #pwutils.get_missing_word_report(missed_words,"output.txt")
    #print(counter)
    #write to excel sheet
    df.to_excel(file_path, sheet_name=sheet_name, index=False)


#Method to check if a word is latin with the pywords
def is_latin(word):
    if str(word) != "nan" or str(word) != "":
        #get the match
        match = lookup.match_word(word)
        if len(match) != 0 and str(match) != "nan" and len(match) > 1:
            return True
        else:
            return False
    
    return False

def main():
    process_words(column_to_read, column_to_write)
if __name__ == "__main__":
    main()