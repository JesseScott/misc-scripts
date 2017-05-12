def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []

    vocab = open(vocabulary_file).read()
    text = open(text_file).read()

    tokenized_vocabulary = tokenize(vocab, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for tt in tokenized_text:
        if tt not in tokenized_vocabulary:
            if tt != "":
                misspelled_words.append(tt)

    return misspelled_words


final_misspelled_words = []
final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)
