def is_pangram(sentence):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    letter_count= {}
    for char in alphabet :
        letter_count[char] = 0
    for char in sentence.lower():
        if char in alphabet:
            letter_count[char] += 1
    for count in letter_count.values():
     if count == 0:
       return False 
    return True

sentence = "How vexingly quick daft zebras jump!"
print(is_pangram(sentence))
