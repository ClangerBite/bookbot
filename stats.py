def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def sort_list_of_dicts(char_dict):
    dict_list = []
    
    for key in char_dict:
        dict = {"char": key,
                "num": char_dict[key]}       
        dict_list.append(dict)
        
    dict_list.sort(reverse=True,key=sort_on)
    
    return dict_list

def count_chars(text):
    lower_case_text = text.lower()
    
    character_count = {}
    
    for char in lower_case_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    return character_count
