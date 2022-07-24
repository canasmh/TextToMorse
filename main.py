from converter import intro_text, convert_to_morse

converting = True

print(intro_text)

while converting:
    text_to_convert = input("Please enter the text you would like to convert: ")

    print(f"\nOriginal Text: {text_to_convert}\n")

    converted_text = convert_to_morse(text_to_convert.upper())

    print(f"Converted Text:\n{converted_text}")

    while True:
        go_again = input("Would you like to convert another text? (y/n): ").lower()
        if go_again == "y":
            break
        elif go_again == "n":
            converting = False
            break
        else:
            print(f"Invalid option: '{go_again}'. Please type 'y' or 'n'\n")

print("Exiting Now... Thank you.")

