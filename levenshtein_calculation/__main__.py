from .apply_levenshtein import get_distance_words

if __name__ == "__main__":

    words = get_distance_words("Luca", 1)
    print(f"Words with a levenshtein distance of 1 to the word Luca \n {[words]}")
