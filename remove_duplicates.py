#remove duplicates
import pandas as pd

file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
column_to_check = "Clean Cholti"
column_latin = "Latin"
column_spanish = "Clean Spanish"

df = pd.read_excel(file_path, sheet_name=sheet_name)

for index, row in df.iterrows():
    cholti = row[column_to_check]
    spanish = row[column_spanish]
    latin = row[column_latin]
    
    max_words = 0
    cholti_words = str(cholti).split(",")
    spanish_words = str(spanish).split()
    latin_words = str(latin).split()

    write_back = []

    if len(cholti_words) > len(spanish_words) and len(cholti_words) > len(latin_words):
        max_words = len(cholti_words)
    elif len(spanish_words) > len(latin_words):
        max_words = len(spanish_words)
    
    for cholti in cholti_words:
        for spanish in spanish_words:
            if(str(cholti) != str(spanish)):
                if(write_back.__contains__(cholti) == False):
                    write_back.append(cholti)
        for latin in latin_words:
            if(str(cholti) != str(latin)):
                if(write_back.__contains__(cholti) == False):
                    write_back.append(cholti)
    cholti_text = "".join(write_back)
    df.at[index,column_to_check] = cholti_text
    #print(cholti_text)
df.to_excel(file_path, index=False)


            



