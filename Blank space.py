sentence = "    This is example  "
len_sentence = len(sentence)
forward_space = 0
backward_space = 0

# Calculation of forward space
i = 0
while i <= len_sentence:
    if sentence[i] != " ":
        forward_space = i
        i = len_sentence+1
    else:
        i += 1

# Calculation of backward space
j = len_sentence
while j > 0:
    if sentence[j-1] == " ":
        j -= 1
    else:
        backward_space = j
        j = -1

# Preparing new sentence
new_sentence = sentence[forward_space:backward_space]
print(new_sentence)
