""" Nile intents storage module """

INTENT_STORAGE = []
NEGATED_INTENTS = []


def negate(nile):
    """ negates Nile intent to undo it later """
    negated = nile
    if 'allow' in nile:
        negated = negated.replace('allow', 'block')
    elif 'block' in nile:
        negated = negated.replace('block', 'allow')

    if 'set' in nile:
        negated = negated.replace('set', 'unset')
    elif 'unset' in nile:
        negated = negated.replace('unset', 'set')

    if 'add' in nile:
        negated = negated.replace('add', 'remove')
    elif 'remove' in nile:
        negated = negated.replace('remove', 'add')

    return negated


def insert(nile, merlin):
    """ stores given nile and merlin intent pairs """
    INTENT_STORAGE.append((nile, merlin))
    NEGATED_INTENTS.append((nile, negate(nile)))
