word_file = open("twain.txt")

word_counts = {}

# loop through words in word_file
# add the word onto word_counts
    # use .get to see if the word is in there
# print keys and values in word_counts

for line in word_file:
    line_list = line.rstrip().split(" ")
    
    for word in line_list:
        word_counts[word] = word_counts.get(word, 0) + 1

for word, value in word_counts.items():        
    print(f"{word} {word_counts[word]}")



       # def make_letter_counts_dict(phrase):
    #"""Return dict of letters and # of occurrences in phrase."""

    #letter_counts = {}

    #for letter in phrase:
        #letter_counts[letter] = letter_counts.get(letter, 0) + 1

    #return letter_counts

    #for animal, number in animals.items():
...    #print(f'{animal}: {number}')