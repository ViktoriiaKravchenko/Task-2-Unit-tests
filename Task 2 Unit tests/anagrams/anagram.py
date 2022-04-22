def reverse(s):
    if type(s) == int or type(s) == float:
        raise TypeError("text should be a str")

    words = s.split()
    reversed_list = []

    for word in words:
        letters = []
        nonletter = []

        for index, char in enumerate(word):
            if char.isalpha():
                letters.append(char)
            if not char.isalpha():
                nonletter.append((index, char))

        letters = letters[::-1]

        for item in nonletter:
            letters.insert(*item)

        letters_string = "".join(letters)

        reversed_list.append(letters_string)

    reversed_text_string = " ".join(reversed_list)
    return reversed_text_string



