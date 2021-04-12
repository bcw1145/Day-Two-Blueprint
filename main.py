def is_on_list(words, word):
    try:
        if words.index("Sun") >= 0:
            return True
    except ValueError:
        return False


def get_x(words, num):
    return words[num]


def add_x(words, word):
    words.append(word)


def remove_x(words, word):
    words.remove(word)


# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
