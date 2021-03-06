# A lot of this is modified from this blog post:
# http://norvig.com/spell-correct.html

def correction(word, dict): 
    "Return some candidate for correct spelling"
    return candidates(word, dict).pop()

def candidates(word, dict): 
    "Generate possible spelling corrections for word."
    return (known([word], dict) or known(edits1(word), dict) or known(edits2(word), dict) or [word])

def known(words, dict): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in dict)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))