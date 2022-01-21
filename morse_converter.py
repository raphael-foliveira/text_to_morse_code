from morse_alphabet import morse_dict, decode_dict


def convert_text_to_morse(text: str):
    converted_text = ""
    if "-" not in text and "." not in text:
        converted_text_list = [f"{morse_dict[character]} " for character in text.lower() if character in morse_dict]
        for code in converted_text_list:
            converted_text += code
    else:
        code_list = text.split(" ")
        for code in code_list:
            if len(code) > 0:
                converted_text += decode_dict[code]
    return converted_text
