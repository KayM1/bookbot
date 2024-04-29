def sort_on(dict):
    return dict[1]

with open("books/frankenstein.txt") as f:
    dict_count = {}
    file_contents = f.read()
    for letters in file_contents:
        if (letters.lower() in dict_count) and (letters.lower().isalpha()):
            dict_count[letters.lower()] += 1
        elif (letters.lower().isalpha()):
            dict_count[letters.lower()] = 1
    # print(dict_count)
    # print("---")
    # print(dict_count.items())
    
    # Sort the dictionary by count
    sorted_dict = []
    sorted_dict = sorted(dict_count.items(), key=sort_on, reverse=True)
    
    # Print the sorted dictionary
    for item in sorted_dict:
        print(f"The letter '{item[0]}' is present {item[1]} times!")