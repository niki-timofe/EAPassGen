from random import SystemRandom

import constants


def gen_syll(length):
    syll = ''
    while True:
        if len(syll) == 0:
            syll += SystemRandom().choice(constants.CONSONANTS + constants.VOWELS)
        elif len(syll) < length:
            if syll[::-1] in constants.VOWELS:
                syll += SystemRandom().choice(constants.CONSONANTS + constants.VOWELS)
            else:
                syll += SystemRandom().choice(constants.VOWELS)
        else:
            break

    return syll


def randomize_capitals(pas, sylls_num):
    pas_list = list(pas)
    for _ in range(SystemRandom().randint(1, sylls_num)):
        cur_cap = SystemRandom().randint(0, len(pas) - 1)
        pas_list[cur_cap] = pas[cur_cap].upper()
    return ''.join(pas_list)


def add_some_numbers(pas, sylls_num):
    pas_list = list(pas)
    for _ in range(SystemRandom().randint(1, sylls_num / 2)):
        cur_num = SystemRandom().randint(0, len(pas) - 1)
        pas_list[cur_num] = str(SystemRandom().randint(0, 9))
    return ''.join(pas_list)


def create_pass(sylls_num, with_caps=False, with_nums=False):
    pas = ''
    for _ in range(sylls_num):
        pas += gen_syll(SystemRandom().randint(1, 3))
    pas = randomize_capitals(pas, sylls_num) if with_caps else pas
    pas = add_some_numbers(pas, sylls_num) if with_nums else pas
    return pas


    # passes_number = int(raw_input('Number of passes to generate: '))
    # sylls_number = int(raw_input('Number of syllables in pass: '))

    # for _ in range(passes_number):
    #     print create_pass(int(sylls_number))