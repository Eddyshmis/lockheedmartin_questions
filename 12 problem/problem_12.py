
class morse_machine:
    def __init__(self) -> None:
        pass
    def test_main(self):
        test_cases = int(input())

        for _ in range(test_cases):
            codes = {}
            self.encoded_morse = ""
            self.decoded_morse = ""
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
                    self.encoded_morse += codes[char]
                    self.encoded_morse += "   "
                elif char == " ":
                    print("       ",end="")
                    self.encoded_morse += "       "
            print("\n")
            print(self.encoded_morse)
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
            self.output = current_word
