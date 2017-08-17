sentence = "One must have a mind of winter"
sentence_as_list = sentence.split(" ")
max_L = 0
index = 0
for i in range(len(sentence_as_list)-1):
    L = len(sentence_as_list[i]) + len(sentence_as_list[i])
    if L > max_L:
        max_L = L
        index = i
print(sentence_as_list[index] +" " + sentence_as_list[index+1])

