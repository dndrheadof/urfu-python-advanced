phone_keys = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

with open("words.txt", "r") as F:
    words = F.read().split("\n")


def my_t9(input_numbers: str):
    filtered_by_len = [word for word in words if len(word) == len(input_numbers)]
    result = []

    for word in filtered_by_len:
        word_fits = True
        for index, letter in enumerate(word):
            if letter not in phone_keys[input_numbers[index]]:
                word_fits = False
                break
        if word_fits:
            result.append(word)
    return result


print(my_t9("22736368"))
