#Opening compressed file

with open('Compressed_Text.txt') as file:
    compressed = file.read()



#print('Compressed text:', compressed)



#Looking for first element before the spaces (0)

first_word = ''
c = 0
while True:

    if compressed[c] == '#':

        break

    else:

        first_word = first_word + compressed[c]
    
    
    c = c + 1

#Adding the easy ones into the dictionary already

values = {}
values[first_word] = '0'
values[' '] = ' '




#Creating dictionary with the rest of the values


word = ''
word_number= ''


counter = 0
counter = (len(first_word)-1)+6






while counter<= len(compressed)-1:

    if compressed[counter] == '.':
        values['.'] = '.'
        break


    
    if compressed [counter]  == '#':
        counter = counter + 1
        

        while True:
            if compressed[counter] == '#':
                counter = counter + 1
                values[word] = word_number
                word = ''
                word_number = ''
                break

            else:
                word_number = word_number + compressed[counter]
                counter = counter + 1
                

                
        

    else:
        word = word + compressed[counter]
        counter = counter + 1

        





#Changing order dictionary to be able to compare with compressed text

r = ''
pairs_nkeys = []

for key, value in values.items():
    r = key
    key = value
    value = r
    
    pairs_nkeys.append((key,value))

values = pairs_nkeys


checking = {}

for x in values:
    checking[x[0]] = x[1]

values = checking

print(compressed)
print(values)

### DECOMPRESSING ###


length_want_skip = 0
hashtags = 0

for key, value in values.items():
     length_want_skip = length_want_skip + len(key) + len(value)
     hashtags = hashtags + 2
    
length_want_skip = length_want_skip + hashtags -4 #-4 because there are two keys that don't have hashtags, so that would be 4 hashtags less

length_want_skip = length_want_skip


compressed = compressed[(length_want_skip):]



#creating a list out of compressed message to be able to distinguish numbers
position = 0
new_compressed = []
big_number = ''

while position <= len(compressed)-2:
    
    if compressed[position+1] == ' ':
        new_compressed.append(compressed[position])
        new_compressed.append(compressed[position+1])
        position = position + 2

    elif compressed[position+1] == '.':
        new_compressed.append(compressed[position])
        new_compressed.append(compressed[position+1])
        position = position + 2

    elif compressed[position] == ' ':
        new_compressed.append(' ')
        position = position + 1


    else:
        while True:

            if compressed[position + 1] is  ' ':
                break

            elif compressed[position + 1] is  '.':
                break
 
            big_number = big_number + compressed[position]
            position = position + 1

            if position  > len(compressed):
                break

            

        big_number = big_number + compressed[position]
        new_compressed.append(big_number)
        big_number = ''
        position = position + 1
            
            


#new_compressed.append(compressed[len(compressed)-1])


print(new_compressed)






new_counter = 0
decompressed = ''

for x in new_compressed:
    if x in values:
        decompressed = decompressed + values[x]

print(decompressed)










with open('Decompressed_Text.txt', 'w') as file:
    file = file.write(decompressed)

    
