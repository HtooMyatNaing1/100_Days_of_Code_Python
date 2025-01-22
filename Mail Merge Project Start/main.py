PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()
    for name in names:
        mail = starting_letter.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
            completed_letter.write(mail)

