# stats.py

def get_book_text(filepath: str) -> str:
    # Reads the whole file and returns the text
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def get_num_words(text: str) -> int:
    # Simple whitespace-based word count
    return len(text.split())

def get_chars_dict(text: str) -> dict:
    # Lowercase + keep letters only
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def _sort_on(item: dict) -> int:
    return item["num"]

def chars_dict_to_sorted_list(char_dict: dict) -> list[dict]:
    # Convert to list of {"char": <letter>, "num": <count>} and sort desc
    items = [{"char": c, "num": n} for c, n in char_dict.items()]
    items.sort(reverse=True, key=_sort_on)
    return items
