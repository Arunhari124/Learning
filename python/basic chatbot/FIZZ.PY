import difflib

def get_similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

score = get_similarity("HALLO", "HI") # Returns ~0.88
if score > 0.1:
    print("Close enough!")