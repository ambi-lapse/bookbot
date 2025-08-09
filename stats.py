

def get_num_words(book):
    words = []
    num_words = 0
    
    words = book.split()
    for word in words:
        num_words += 1
    return num_words


def char_dict(book):
    char_dict = {}

    for char in book:
        lower = char.lower()
        if lower in char_dict:
            char_dict[lower] += 1
        else:
            char_dict[lower] = 1
    
    return char_dict





def sort_data(data):
    def sort_on(items):
        return items["num"]
    
    sorted_list = []
    
    for d in data:
        char_dict = {"char": d, "num": data[d]}
        sorted_list.append(char_dict)
        
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list
        
