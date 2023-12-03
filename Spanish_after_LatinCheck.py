from langdetect import detect
import pandas as pd

file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
column_to_read = "Ch'olti & Spanish"
column_to_write = 'Spanish after Latin check'


def process(file_path, column_to_read, column_to_write):
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        spanish_words = []
        other_words = []
        value = row[column_to_read]
        words = str(value).split(" ")
        for word in words:
            word = word.strip()
            if check_spanish(word):
                if str(word) != "nan" or str(word) != "":
                    spanish_words.append(word)
            else:
                if str(word) != "nan" or str(word) != "":
                    other_words.append(word)
        spanish_text = " ".join(spanish_words)
        cholti_text = " ".join(other_words)
        df.at[index,column_to_write] = spanish_text
        df.at[index, "Last Cholti Check"] = cholti_text    

    df.to_excel(file_path, index=False)


def check_spanish(word):
    try:
        # Attempt to detect the language of the word
        language = detect(word)
        # Check if the detected language is Spanish
        return language == 'es'
    except:
        # Handle cases where language detection fails
        return False

def main():
    process(file_path, column_to_read, column_to_write)
if __name__ == "__main__":
    main()
