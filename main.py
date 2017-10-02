import csv

def load_letters():
    global letters
    letters = []

    with open("letter.csv", "r") as letter_file:
        file_reader = csv.reader(letter_file, delimiter=',', quotechar='|')
        for row in file_reader:
            letters.append(row[1])

def load_words():
    global word_nums
    word_rd = []
    word_nums = []
    
    with open("words.csv", "r") as word_file:
        file_reader = csv.reader(word_file, delimiter=',', quotechar='|')
        row_count = 0
        for row in file_reader:
            word_rd.append(row[0])
            row_count+=1

        for x in range(row_count):
            words = []
            words.append(str(row[1]))
            for char in word_rd[x]:
                words.append(letters.index(char))
                
            word_nums.append(words)

def check_word_db():
    num_out = []
    
    for char in data:
        num_out.append(letters.index(char))
    find_word = word_nums[0]
    
    if num_out == find_word[1:]:
        if find_word[0] == "1":
            print("greeting")

def main():
    global data
    data = input("Data: ")
    data = data.lower()
    
    load_letters()
    load_words()
    check_word_db()

main()

