import random
from pathlib import Path
import math

lists_folder = Path(__file__).parent / 'word-lists'

# Load word lists from files
with open(f"{lists_folder}\\google-10000-english-no-swear-medium.txt", 'r') as medium:
    data = medium.readlines()
    MEDIUM_WORDS = [word.strip("\n") for word in data]

with open(f"{lists_folder}\\google-10000-english-no-swear-short.txt", 'r') as short:
    data = short.readlines()
    SHORT_WORDS = [word.strip("\n") for word in data]

with open(f"{lists_folder}\\google-10000-english-no-swear-long.txt", 'r') as long:
    data = long.readlines()
    LONG_WORDS = [word.strip("\n") for word in data]


def get_words(word_type: str, amount: int) -> list[str]:
    """
    Get a specified amount of random words from the desired word list.

    Args:
        word_type (str): One of the three lists available ('short', 'medium', 'long').
        amount (int): The desired amount of words. If this is larger than the list, it will raise an error.

    Returns:
        list[str]: A list of random words.
    """
    valid_lists = { "short": SHORT_WORDS, "medium": MEDIUM_WORDS, "long": LONG_WORDS }
    
    if word_type not in valid_lists:
        raise ValueError(f"Invalid word type: {word_type}. Choose from 'short', 'medium', or 'long'.")
    
    word_list = valid_lists[word_type]
    
    if amount > len(word_list):
        raise ValueError(f"Requested amount ({amount}) exceeds the size of the list ({len(word_list)}).")
    
    return random.sample(word_list, k=amount)


def mix_word_types(word_types: list[str], amount: int, **kwargs) -> list[str]:
    """
    Get a mix of words of different lenghts, if pref is provided that type of word will take up 70% of the resulting amount of words.

    Args:
        word_types (list[str]): At least 2 of the three lists available ('short', 'medium', 'long').
        amount (int): The total amount of words the function will output. If this is larger than the list, it will raise an error.
        pref (str): (Optional) The type of word that should get priority.
        word_var (int): (Optional) Size of the word sample the code will shuffle through. 

    Returns:
        list[str]: A list of random words.
    """
    
    # VALIDATE LENGTH OF WORD TYPES
    if len(word_types) < 2:
          raise ValueError(f"Length of argument word_types should be at least 2.")
    
    pref=kwargs.get('pref', None)
    word_var=kwargs.get('word_var', None)

    # SPLIT REQUESTED AMOUNT BETWEEN TYPES
    percent_for_pref = 70
    even_split = math.ceil(amount / len(word_types)) # in case no pref is specified
    pref_amount = math.ceil(percent_for_pref * amount / 100)
    amount_remaining = int(amount - pref_amount)
    split_remaining = int(amount_remaining / 2) # devide the remain by 2 when requested wordtypes are three
    
    valid_lists = { "short": SHORT_WORDS, "medium": MEDIUM_WORDS, "long": LONG_WORDS }
    words = []
    
    for item in word_types:
    #   VALIDATE EACH WORD TYPE
      if item not in valid_lists:
        raise ValueError(f"Invalid word type: {item}. Choose from 'short', 'medium', or 'long'.")
  
      word_list = valid_lists[item]
      #filter out words with less than 3 characters and, if requested, get the amount of word variety 
      filtered_list = [w for w in word_list if len(w)>=3][:word_var if word_var else 200]
      
    #  VALIDATE REQ. AMOUNT
      if amount > len(filtered_list):
          raise ValueError(f"Requested amount ({amount}) exceeds the size of the list ({len(filtered_list)}).")
      
    #   SAMPLE WORD LISTS
      if pref:
          if pref == item:
            new_words = random.sample(filtered_list, k=pref_amount)
          else:
            new_words = random.sample(filtered_list, k=split_remaining if len(word_types) == 3 else amount_remaining)
      else:
          new_words = random.sample(filtered_list, k=even_split)
      words += new_words
    
    random.shuffle(words)
    return words

word_list_config = {
  "easy": {
    'word_types': ['short', 'medium'],
    'pref': "short"
    },
  'medium': {
    'word_types': ['short', 'medium', 'long'],
    'pref': 'medium'
     },
  'hard': {
    'word_types': ['medium', 'long'],
    'pref': 'long'
    }
}

def get_new_words(app_settings):
  word_types = word_list_config[app_settings.difficulty]['word_types']
  pref = word_list_config[app_settings.difficulty]['pref']
  word_var = app_settings.word_var

  word_list = mix_word_types(word_types=word_types, 
                             amount=160, 
                             pref=pref, 
                             word_var=word_var)
  return word_list