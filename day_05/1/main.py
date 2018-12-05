input_characters = open("./1.input", "r").read()
character_list = list(input_characters)

is_clear = False
while not is_clear:
    current_index = 0
    has_removed = False
    for current_character in character_list:
        try:
            next_character = character_list[current_index + 1]
            if current_character.lower() == next_character.lower() and next_character != current_character:
                del(character_list[current_index + 1])
                del(character_list[current_index])
                has_removed = True
                print(len(character_list))
        except IndexError:
            pass
        current_index += 1

    if not has_removed:
        is_clear = True

print("Result: " + str(len(character_list)))
