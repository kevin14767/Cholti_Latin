#printing latin definitions
import pywords.lookup as lookup
from pywords.matchfilter import MatchFilter
import pywords.utils as pwutils
import pandas as pd

file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
column_to_read = "Latin"
column_to_write = 'Latin Definition/Stems'

df = pd.read_excel(file_path)
for index, row in df.iterrows():
    value = row[column_to_read]
    definitions = []
    if str(value) != "nan" and str(value) != "idem":
        matches = lookup.match_word(value)
        for match in matches:
            definitions.append(lookup.get_dictionary_string(match,full_info=False))
    text_combined = "|".join(definitions)
    print(text_combined)
    df.at[index,column_to_write] = text_combined

df.to_excel(file_path, sheet_name=sheet_name, index=False)