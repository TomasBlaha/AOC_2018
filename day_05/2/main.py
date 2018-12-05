import string

input_characters = open("./2.input", "r").read()
character_list = list(input_characters)

all_characters = string.ascii_lowercase

smallest_amount = None
for small_character in all_characters:
    improved_list = [x for x in character_list if x != small_character and x != small_character.upper()]
    is_clear = False
    while not is_clear:
        current_index = 0
        has_removed = False
        for current_character in improved_list:
            try:
                next_character = improved_list[current_index + 1]
                if current_character.lower() == next_character.lower() and next_character != current_character:
                    del (improved_list[current_index + 1])
                    del (improved_list[current_index])
                    has_removed = True
            except IndexError:
                pass
            current_index += 1

        if not has_removed:
            is_clear = True

    if smallest_amount is None:
        smallest_amount = len(improved_list)
    else:
        if len(improved_list) < smallest_amount:
            smallest_amount = len(improved_list)


print(smallest_amount)