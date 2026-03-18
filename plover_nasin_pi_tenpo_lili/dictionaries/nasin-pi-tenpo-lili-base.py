import re

LONGEST_KEY = 1

PARTS_MATCHER = re.compile(
        r'([<]*)'               # Preinitial modifier
        r'([mstkpnlj]*)'        # Initial word bank
        r'([12\*34]*|-)'        # Modifier
        r'([ljpntkms]*)'        # Final word bank
        r'([>]*)$'              # Postfinal modifier
        )
# Defining dictionary
PREINITIAL_MODIFIER = {
        "<": "<",
        }

INITIAL_BANK = {
        "m": "mi",
        "s": "sina",
        "t": "toki",
        "k": "ken",
        "p": "pona",
        "n": "ni",
        "l": "lon",
        "j": "jan",
        "ms": "kama",
        "tk": "awen",
        "pn": "tawa",
        "lj": "weka",
        "sk": "sona",
        "mt": "mute",
        "tp": "tenpo",
        "kn": "wile",
        "pl": "pilin",
        "nj": "ona",
        "mk": "moku",
        "ml": "wile",
        "pj": "pali",
        "mn": "ma",
        "mp": "musi",
        "sl": "ike",
        "st": "sitelen",
        "sp": "ale",
        "kn": "kepeken",
        "tl": "ilo",
        "tn": "tomo",
        "kl": "lukin",
        "nl": "ante",
        "kj": "ijo",
        "mj": "mu",
        "sn": "sama",
        "tj": "tu",
        "kp": "pana",
        "sj": "soweli",
        "skn": "n",
        "mstk": "suli",
        "mtpl": "nimi",
        "sknj": "nasin",
        "pnlj": "lili",
        "mstkpnlj": "kijetesantakalu",
        }

MODIFIER = {
        "1": "li",
        "2": "e",
        "3": "pi",
        "4": "la",
        "12": "a",
        "13": "kin",
        "14": "anu",
        "23": "en",
        "24": "taso",
        "34": "o",
        "123": "lon",
        "124": "CARTOUCHE!",
        "134": "tan",
        "234": "seme",
        "1234": "ala",
        }
# Mirror Final Bank so I don't have to add every entry manually 

def mirror_order(stroke):
    return "".join(sorted(stroke, key=lambda x: "ljpntkms".index(x)))

FINAL_BANK = {mirror_order(k): v for k, v in INITIAL_BANK.items()}

print(FINAL_BANK)


POSTFINAL_MODIFIER = {
        ">": ">",
        }




# all the stuff I know about
def lookup(outline):
    stroke = "".join(outline)
    match = PARTS_MATCHER.fullmatch(stroke)

    if not match:
        raise KeyError

    pre, init, mid, final, post = match.groups()
    
    initial_word = INITIAL_BANK.get(init, "")
    mod_word = MODIFIER.get(mid, "")
    final_word = FINAL_BANK.get(final, "")


    parts = []
    
    if pre == "<" and mod_word:
        parts = [mod_word, initial_word, final_word]
    elif post == ">" and mod_word:
        parts = [initial_word, final_word, mod_word]
    else:
        parts = [initial_word, mod_word, final_word]

    phrase = " ".join(filter(None, parts))

    if not phrase:
        raise KeyError

    return phrase

def reverse_lookup(text):
    return []
