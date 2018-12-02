box_list = open("./1.input", "r").read().splitlines()
two_letter_boxes_count = 0
three_letter_boxes_count = 0

for box_name in box_list:
    is_two_letter = False
    is_three_letter = False

    letters = list(box_name)
    for letter in letters:
        letter_occurrences = len(box_name) - len(box_name.replace(letter, ""))

        if letter_occurrences == 2:
            is_two_letter = True
        if letter_occurrences == 3:
            is_three_letter = True

    if is_two_letter:
        two_letter_boxes_count += 1
    if is_three_letter:
        three_letter_boxes_count += 1

print(two_letter_boxes_count * three_letter_boxes_count)
