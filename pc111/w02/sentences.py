import random

def main():
    quantities = [1, 2]
    tenses = ['past', 'present', 'future']
    for x in range(0, 6):
        verb_quantity = random.choice(quantities)
        verb_tense = random.choice(tenses)
        make_sentence(verb_quantity, verb_tense)

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f'{determiner} {noun} {verb}'
    print(sentence)

def get_determiner(quantity):
    """Return a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb.
    """
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(verbs)

main()
