import pdb

word_file = open("twain.txt")

word_counts = {}

# loop through words in word_file
# add the word onto word_counts
    # use .get to see if the word is in there
# print keys and values in word_counts

for line in word_file:
    line_list = line.rstrip().split(" ")
# print(word_counts)

    for word in line_list:
        # print(word)
        if len(word) == 0:
            continue

        if word[-1] in "'\",.!?-#$%^&();:_":
            word = word[:-1]
        
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1

for word, value in word_counts.items():        
    print(f"{word} {word_counts[word]}")

# print(word_counts)

       # define punctuation

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
#        no_punct = no_punct + char

# # display the unpunctuated string
# print(no_punct)