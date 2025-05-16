def get_num_words(text):
    content = text.split()
    return len(content)

def get_character_count(text):
    lower_text = text.lower()
    letter_count = {}
    for character in lower_text:
        if(character in letter_count):
            letter_count[character] += 1
            letter_count.update({character:letter_count[character]})
        else:
            letter_count[character] = 1
    
    return letter_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    