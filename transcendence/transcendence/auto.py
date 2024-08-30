import re

def wrap_text_in_gettext(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define a regular expression to find 'text': 'some text'
    text_pattern = re.compile(r"('text'\s*:\s*)'([^']+)'")

    # Use a substitution to wrap found text in _()
    modified_content = text_pattern.sub(r"\1_('\2')", content)

    # Write the modified content back to the file
    with open("menus1.py", 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print("The 'text' fields have been wrapped in _()")

# Provide the path to your Python file
file_path = 'menus.py'
wrap_text_in_gettext(file_path)
