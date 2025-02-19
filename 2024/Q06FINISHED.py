# Q06

tblWords = [["apple", "banana"],
              ["wrist", "leg"],
              ["blue", "yellow"],
              ["speaker", "keyboard"],
              ["lavender", "tulip"],
              ["pencil", "chalk"],
              ["apartment", "house"],
              ["bottom", "top"],
              ["snow", "fog"],
              ["beach", "mountain"],
              ["", ""]]

word1 = "newspaper"
word2 = "book"

# ----------------------------------------------
# Write your code below this line

# Replace the blank pair with word1 and word2
tblWords[-1][0] = word1
tblWords[-1][1] = word2

count = 0
for row in tblWords:
    count += 1

    # Displsy each pair
    print(count, " ".join(row))

    # Display longer word
    if len(row[0]) > len(row[1]):
        print("\t",row[0])
    else:
        print("\t",row[1])
    
    # Display and reodrer the pair which is not in alphabetical order
    if row[0] > row[1]:
        print("\t", row[1], row[0])