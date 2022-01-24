"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730387901"

five_ch_word: str = input("Enter a 5-character word: ")
if len(five_ch_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_ch: str = input("Enter a single character: ")
if len(single_ch) != 1:
    print("Error: Character must be a single character.")
    exit()
matches_count: int = 0 

print("Searching for " + single_ch + " in " + five_ch_word)

if single_ch == five_ch_word[0]:
    print(single_ch + " found at index 0")
    matches_count = matches_count + 1 
if single_ch == five_ch_word[1]:
    print(single_ch + " found at index 1")
    matches_count = matches_count + 1
if single_ch == five_ch_word[2]:
    print(single_ch + " found at index 2")
    matches_count = matches_count + 1 
if single_ch == five_ch_word[3]:
    print(single_ch + " found at index 3")
    matches_count = matches_count + 1
if single_ch == five_ch_word[4]:
    print(single_ch + " found at index 4")
    matches_count = matches_count + 1

if matches_count == 0:
    print("No instances of " + single_ch + " found in " + five_ch_word)
else: 
    if matches_count == 1:
        print("1 instance of " + single_ch + " found in " + five_ch_word)
    else:
        if matches_count > 1:
            print(str(matches_count) + " instances of " + single_ch + " found in " + five_ch_word)