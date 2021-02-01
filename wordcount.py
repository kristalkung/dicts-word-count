
def count_words(file):
    word_file = open(file)

    word_counts = {}

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

count_words("test.txt")