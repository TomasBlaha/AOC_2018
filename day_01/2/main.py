def loopArray(changes, states, current):
    for change in changes:
        current += int(change)
        print(current)

        if current in states:
            return

        states.append(current)

    loopArray(changes, states, current)


frequency_changes = open("./2.input", "r").read().splitlines()
loopArray(frequency_changes, [], 0)
