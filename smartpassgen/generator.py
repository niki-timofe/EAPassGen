from random import SystemRandom
from smartpassgen import constants

import math


def gen_syllables(length):
    syllables = ''
    while True:
        if len(syllables) == 0:
            syllables += SystemRandom().choice(constants.CONSONANTS + constants.VOWELS)
        elif len(syllables) < length:
            if syllables[::-1] in constants.VOWELS:
                syllables += SystemRandom().choice(constants.CONSONANTS + constants.VOWELS)
            else:
                syllables += SystemRandom().choice(constants.VOWELS)
        else:
            break

    return syllables


def randomize_capitals(pas, syllables_num):
    pas_list = list(pas)
    for _ in range(SystemRandom().randint(1, syllables_num)):
        cur_cap = SystemRandom().randint(0, len(pas) - 1)
        pas_list[cur_cap] = pas[cur_cap].upper()
    return ''.join(pas_list)


def add_some_numbers(pas, syllables_num):
    pas_list = list(pas)

    for _ in range(SystemRandom().randint(1, syllables_num)):
        cur_num = SystemRandom().randint(0, len(pas) - 1)
        if letter_to_number(pas_list[cur_num]):
            pas_list[cur_num] = letter_to_number(pas_list[cur_num])

    # for _ in range(SystemRandom().randint(1, syllables_num / 2) - counter):
    #     cur_num = SystemRandom().randint(0, len(pas) - 1)
    #     pas_list[cur_num] = str(SystemRandom().randint(0, 9))
    return ''.join(pas_list)


def letter_to_number(letter):
    if letter in constants.CONV_LETTERS.keys():
        return constants.CONV_LETTERS[letter]
    else:
        return False


def letter_to_symbols(letter):
    if letter in constants.CONV_LETTERS_TO_SYM.keys():
        return constants.CONV_LETTERS_TO_SYM[letter]
    else:
        return False


def add_some_symbols(pas, syllables_num):
    pas_list = list(pas)

    for _ in range(SystemRandom().randint(1, syllables_num)):
        cur_num = SystemRandom().randint(0, len(pas) - 1)
        if letter_to_symbols(pas_list[cur_num]):
            pas_list[cur_num] = letter_to_symbols(pas_list[cur_num])

    for _ in range(SystemRandom().randint(1, math.ceil(syllables_num / 4))):
        cur_sym = SystemRandom().randint(0, len(pas) - 1)
        pas_list.insert(cur_sym, SystemRandom().choice(constants.SYMBOLS))
    return ''.join(pas_list)


def create_pass(syllables_num, with_caps=False, with_nums=False, with_symbols=False):
    pas = ''
    for _ in range(syllables_num):
        pas += gen_syllables(SystemRandom().randint(1, 3))
    pas = randomize_capitals(pas, syllables_num) if with_caps else pas
    pas = add_some_numbers(pas, syllables_num) if with_nums else pas
    pas = add_some_symbols(pas, syllables_num) if with_symbols else pas
    return pas


passes_number = int(raw_input('Number of passes to generate: '))
syllables_number = int(raw_input('Number of syllables in pass: '))

for _ in range(passes_number):
    print create_pass(int(syllables_number), True, True, True)
