test_cases = int(input())
for _ in range(test_cases):
    codes = {}
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
        elif char == " ":
            print("       ",end="")
    
    morse_code = input()
    typing_morse = ""
    for char in morse_code:
        typing_morse += char
        typing_morse = typing_morse.replace(" ","")
        if typing_morse in codes.values:
            print(typing_morse)
            typing_morse = ""

            