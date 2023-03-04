def append_to_file(path, text):
    with open(path, 'a') as file:
        file.write(text)

