from morse_converter import convert_text_to_morse


def main():
    print("Text to Morse Code converter\n")
    user_text = input("Text:\n>>> ")
    converted_text = convert_text_to_morse(user_text)
    print("Output: ")
    print(converted_text)
    print("Do you want to convert again?")
    convert_again = input("y / n: ")
    if convert_again.lower() == "y":
        return main()
    else:
        exit(0)


main()
