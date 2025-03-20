# Python program to count lines, words, and characters in a text file without a function

filename = input("Enter the filename: ")
lines = 0
words = 0
characters = 0

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines += 1  # Count lines
            words += len(line.split())  # Count words in the line
            characters += len(line)  # Count characters in the line
    
    print("Number of lines:", lines)
    print("Number of words:", words)
    print("Number of characters:", characters)
except FileNotFoundError:
    print("File not found! Please check the filename and try again.")