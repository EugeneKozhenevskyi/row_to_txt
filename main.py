def add_row_to_file():
    user_input = input("Enter text: ")

    file = open("text.txt", "w")

    file.write(user_input)

    file.close()

    print("Text has been added.")


add_row_to_file()
