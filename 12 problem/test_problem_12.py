import problem_12
def test_encode():
    test = problem_12.morse_machine()
    # problem_12.input = lambda: "1"
    problem_12.input = lambda: """1
A . -
B - . . .
C - . - .
D - . .
E .
F . . - .
G - - .
H . . . .
I . .
J . - - -
K - . -
L . - . .
M - -
N - .
O - - -
P . - - .
Q - - . -
R . - .
S . . .
T -
U . . -
V . . . -
W . - -
X - . . -
Y - . - -
Z - - . .
HELLO WORLD
"""
    test.test_main()
    # assert """. .      . - . .    - - -   . . . -   .    - . - .   - - -    - . .   . I LOVE""" == test.output
    assert test.encoded_morse == "....   .   .-..   .-..   ---          .--   ---   .-.   .-..   -.."
    