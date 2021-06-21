import pandas as pd
from Levenshtein import distance


def get_distance_words(word: str = "Luca", desired_distance: int = 1) -> list:
    """Get names stored in a dataframe column with specific levenshtein distance to target word

    Function calculates distance between a series of words stored in a pandas dataframe and
    a target word. The distance calculation is based on the levenshtein distance. A definition
    of this metric can be found here: https://en.wikipedia.org/wiki/Levenshtein_distance

    :param word: target word to compare to words in data frame
    :param desired_distance: indicator for length to word
    :returns: list of words with distance
    """
    df = pd.read_csv("./data/dog_data.csv")

    df['levenshtein_distance'] = df.apply(lambda row: distance(row['HUNDENAME'], word), axis=1)

    names_list = df[df['levenshtein_distance'] == desired_distance]['HUNDENAME'].drop_duplicates().to_list()

    return names_list
