

alphabet = list("abcdefghijklmnopqrstuvwxyz1234567890 ")
morse_characters = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. " \
                   "--- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. " \
                   ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- / ".split(" ")
morse_dict = {letter: code for (letter, code) in zip(alphabet, morse_characters)}
