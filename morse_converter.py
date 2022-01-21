from morse_alphabet import morse_dict


def convert_text_to_morse(text: str):
    converted_text = ""
    converted_text_list = [f"{morse_dict[character]} " for character in text.lower() if character in morse_dict]
    for code in converted_text_list:
        converted_text += code
    return converted_text
