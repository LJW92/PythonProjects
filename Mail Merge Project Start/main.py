# for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as file_names:
    names = file_names.readlines()

clean_names = []
for name in names:
    clean_names.append(name.strip())
# Replace the [name] placeholder with the actual name.
with open('./Input/Letters/starting_letter.txt') as file_letter:
    letter = file_letter.read()

# Save the letters in the folder "ReadyToSend".
letters = []
for name in clean_names:
    letters.append(letter.replace('[name]', name))

index = 0
for name in clean_names:
    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as file:
        file.write(letters[index])
    index += 1
