letter_cost = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
word = input()
total = sum([key for letter in word for key, value in letter_cost.items() if letter in value])



print(total)

