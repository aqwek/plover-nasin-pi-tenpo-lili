import re

# i know what this does :3
LONGEST_KEY = 1

# phrasing crap I have no idea what I'm doing
PARTS_MATCHER = re.compile(
        r'([<]*)'               # Preinitial modifier
        r'([mstkpnlj]*)'        # Initial word bank
        r'([12\*34]*|-)'        # Modifier
        r'([ljpntkms]*)'        # Final word bank
        r'([>]*)$'              # Postfinal modifier
        )

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
        "pl": "pali",
        "nj": "ona",
        "mk": "moku",
        "ml": "wile",
        "mstk": "suli",
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
        "34": "o",
        "123": "lon",
        "124": "CARTOUCHE!",
        "134": "tan",
        "234": "seme",
        "1234": "ala",
        }

FINAL_BANK = {
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
        "ljpntkms": "kijetesantakalu",
        }

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
