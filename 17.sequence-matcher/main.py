from difflib import SequenceMatcher

text1 = input("Enter text 1 : ")
text2 = input("Enter text 2 : ")

sequence_score = SequenceMatcher(None, text1, text2).ratio()

print(f"Both are {sequence_score*100} % similar")
