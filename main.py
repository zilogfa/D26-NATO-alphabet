# Dev: Ali Jafarbeglou Nato_Phonetic_alphabet - Step1: Created list from nato.CSV file in format > {A: alfa,
# B: Big}. Step2: create result list ["alfa","Big"]
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word: ").upper()
result = [nato_dic[letter] for letter in word]
print(result)





