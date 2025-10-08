def sort_on(items):
    return items["num"]

def get_num_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

def get_letter_count(text):
    letters = {}
    for char in text:
        lowerd = char.lower()
        if lowerd in letters:
            letters[lowerd] += 1
        else:
            letters[lowerd] = 1
    return letters
            
def sort_letter_count(letters):
    sorted_letters = []
    for letter, num in letters.items():
        if letter.isalpha():
            sorted_letters.append({"char":letter, "num":num})
    sorted_letters.sort(key=sort_on, reverse=True)
    return sorted_letters