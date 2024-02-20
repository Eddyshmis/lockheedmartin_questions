test_cases = int(input())
for _ in range(test_cases):
    codes = {}
    encoded_morse = ""
    decoded_morse = ""
    for _ in range(26):
        line = input()
        new_line = ""
        letter = ""
        for char in line:
            if char.isalpha():
                letter += char
            else:
                new_line += char
                
        codes[letter] = new_line.replace(" ","")

    encode_line = input()
    for char in encode_line:
        if char in codes.keys():
            print(codes[char],"   ",end="")
            encoded_morse += codes[char]
            encoded_morse += "   "
        elif char == " ":
            print("       ",end="")
            encoded_morse += "       "
    print("\n")
    print(encoded_morse)
    print("\n")

    morse_code = input()

    morse_code = [x for x in morse_code]
    index = 0
    current_word = ""
    for char in morse_code:
        try:
            if morse_code[index + 1] != " " or morse_code[(index + 2)] != " ":
                current_word += morse_code[index]
                if current_word.replace(" ","") in codes.values:
                    print(current_word)
                
            elif morse_code[index] != " ":
                current_word += morse_code[index]
                
            elif morse_code[(index + 1)] == " " and morse_code[(index + 2)] == " ":
                current_word += "   "
        except Exception as e:
            print(e,index)
            if morse_code[index] != " ":
                current_word += morse_code[index]
                
            pass
        index += 1
        
    print(current_word,index)

            