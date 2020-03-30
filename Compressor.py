### PARAGRAPH SPLITTING ###

# Note: I haven't implemented yet the settings for some characters such as: ?, !, /, ...

#Reading from file

with open("ReadFrom.txt") as file:
    paragraph = file.read()
    print(paragraph)



list_words = []

wbw = ''

c = 0
while c < len(paragraph):
    x = paragraph[c]
    y = paragraph[c-1]
    
    if x == '.':
        list_words.append(wbw)
        wbw = ''
        list_words.append('.')

    elif x == ' ' and y == '.':
        list_words.append(' ')

        
    elif x == ' ':
        list_words.append(wbw)
        wbw = ''
        list_words.append(' ')
        
    else:
        wbw = wbw + x


    c=c+1





### MAKING DICTIONARY { word : number_of_repetitions} ###


pairs = { }

c2 = 0
v = 0
current_word = ''


while c2 < len(list_words):

    current_word = list_words[c2]

    if current_word in pairs.keys():
        pairs[current_word] = pairs[current_word] + 1
    else:
        pairs[current_word] = 1
        


    c2 = c2 + 1






#Switching keys for values and viceversa

r = ''
pairs_nkeys = []

for key, value in pairs.items():
    r = key
    key = value
    value = r
    
    pairs_nkeys.append((key,value))


#print(pairs_nkeys)


### COMPRESSOR ###

# cr == compressed relations

cr = []
x = 0


for key,value in pairs_nkeys:

        if value == ' ':

            key = value
            value = ' '
            cr.append((key,value))
        
        elif value == '.':
            key = value
            value = '.'
            cr.append((key,value))

        else:
            key = value

            value = x

            cr.append((key, '#' +  str(value) + '#'))
        
            x = x + 1


#print(cr)



### CREATING COMPRESSED DATA ###


data  = ''



for tuple in cr:
    
    data = data + str(tuple[0]) +str(tuple[1])


    
k = 0
y = ''
    




while k <= len(list_words) - 1:

    y = list_words[k]

    for tuple in cr:
        if y == str(tuple[0]):
            y = str(tuple[1])
            if y is not ' ' and y is not '.':
                y = y[1:-1]

            data = data + y


    k = k + 1


print(data)  

    
    
### WRITING DATA INTO FILE ###


File = 'Compressed_Text.txt'

with open(File, 'w') as File:
    File.write(data)

