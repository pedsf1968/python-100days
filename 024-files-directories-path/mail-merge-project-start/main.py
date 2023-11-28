# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

INVITED_NAMES = "./Input/Names/invited_names.txt"
LETTER_TEMPLATE = "./Input/Letters/starting_letter.txt"
OUTPUT_FOLDER = "./Output/ReadyToSend"
REPLACE_BY_NAME = "[name]"


def read_invited_names(file_name):
    """Read a file that contain names and return the list of the names"""
    invited_names = []
    with open(file_name) as file:
        for line in file:
            invited_names.append(line.rstrip())
    return invited_names


def read_letter_template(file_name):
    """Read letter template from a file and returne the content"""
    with open(file_name) as letter_template:
        return letter_template.read()


def write_letter(folder, letter_template, name):
    """Write a letter from a template and replace name by specified text"""
    new_content = letter_template.replace(REPLACE_BY_NAME, name)
    with open(f"{folder}/letter_for_{name}.txt", "w") as file:
        file.write(new_content)


def write_letters(folder, letter_template, names_list):
    """Call write_letter function for each names of a list"""
    for name in names_list:
        write_letter(OUTPUT_FOLDER, letter_template, name)


def main():
    names = read_invited_names(INVITED_NAMES)
    content = read_letter_template(LETTER_TEMPLATE)
    write_letters(OUTPUT_FOLDER, content, names)


if __name__ == "__main__":
    main()
