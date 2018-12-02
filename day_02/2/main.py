box_list = open("./2.input", "r").read().splitlines()

for box in box_list:
    for box_to_compare in box_list:
        differences = [i for i in range(len(box)) if box[i] != box_to_compare[i]]
        if len(differences) == 1:
            letter_index = differences[0]
            print(box[:letter_index] + box[letter_index+1:])
            exit()
