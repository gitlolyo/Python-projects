#Variables
bin2dec = 0
acc = 0
end_loop = False

#Prompt
binary = input('Enter a binary number (up to 8 digits): ')
num_list = []

while not end_loop:
    if not '0' and '1' in binary:
        print('Error: Your number is not a binary number.')
        end_loop = True
    elif len(binary) > 8:
        print('Error:', len(binary), 'digits. That\'s', len(binary) - 8,
              'too many.')
        end_loop = True
    else:
        #Form it into an array
        for i in binary:
            num_list.append(int(i))

        num_list.reverse()

        #Perform bin2dec using accumulator
        for element in num_list:
            digit = element * (2 ** acc)
            bin2dec += digit
            acc += 1
    end_loop = True

print('Your binary number in decimals (base 10) is', bin2dec)