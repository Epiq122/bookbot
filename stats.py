def count_words(full_text):
    words = full_text.split()
    return len(words)


def count_characters(full_text):
    char_inventory = {}

    for char in full_text.lower():
        if char not in char_inventory:
            char_inventory[char] = 1
        else:
            char_inventory[char] += 1

    return char_inventory


def chars_dict_to_list(char_count_dict):
    report_list = []

    for char, count in char_count_dict.items():
        tiny_dict = {"char": char, "num": count}
        report_list.append(tiny_dict)

    report_list.sort(reverse=True, key=lambda item: item["num"])
    return report_list
