alphanumeric_list = [
    "A1", "B2", "E3", "C4", "O5", "D6", "I7", "F8", "U9", "G10",   # 4 vowels: A, E, O, I, U
    "H11", "J12", "A13", "K14", "E15", "L16", "I17", "M18", "O19", "N20",  # 4 vowels: A, E, I, O
    "P21", "Q22", "U23", "R24", "A25", "S26", "E27", "T28", "I29", "V30",  # 4 vowels: U, A, E, I
    "W31", "X32", "O33", "Y34", "A35", "Z36", "E37", "B38", "U39", "C40",  # 4 vowels: O, A, E, U
    "D41", "F42", "I43", "G44", "O45", "H46", "U47", "J48", "A49", "K50",  # 4 vowels: I, O, U, A
    "L51", "M52", "E53", "N54", "I55", "P56", "O57", "Q58", "A59", "R60",  # 4 vowels: E, I, O, A
    "S61", "T62", "U63", "V64", "E65", "W66", "I67", "X68", "O69", "Y70",  # 4 vowels: U, E, I, O
    "Z71", "B72", "A73", "C74", "E75", "D76", "I77", "F78", "U79", "G80",  # 4 vowels: A, E, I, U
    "H81", "J82", "O83", "K84", "A85", "L86", "E87", "M88", "I89", "N90",  # 4 vowels: O, A, E, I
    "P91", "Q92", "U93", "R94", "E95", "S96", "I97", "T98", "O99", "V100"  # 4 vowels: U, E, I, O
]

incorrect_ans = 0

user_input = input("Enter your answer (a number): ")
if not user_input.isdigit():
    print("Invalid input. Please enter a number.")
    exit()

number_list = [item[1:] for item in alphanumeric_list[9::-1] if item[0] in 'AEOUI']

answer = ''.join(number_list)


if user_input == answer:
    print("Correct")
else:
    print("Incorrect")


    

