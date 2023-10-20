def reverse_word(word):
    word=word.split()

    print(" ".join(reversed(word)))
    
word=str(input())
reverse_word(word)