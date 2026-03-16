import re

# i know what this does :3
LONGEST_KEY = 1

# phrasing crap I have no idea what I'm doing
PARTS_MATCHER = re.compile(
        r'([AB]*)'              # Preinitial modifiers
        r'([mstkpnlj]*)'        # Initial word bank
        r'([12\*34]*|-)'        # Middle modifiers
        r'([ljpntkms]*)'        # Final word bank
        r'([CD]*)$'              # Postfinal modifiers
        )

PREINITIAL_MODIFIERS = {

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
        "mstkpnlj": "kijetesantakalu",
        }

MIDDLE_MODIFIERS = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
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

POSTFINAL_MODIFIERS = {

        }




# all the stuff I know about
def lookup(outline):
    stroke = "".join(outline)
    match = PARTS_MATCHER.fullmatch(stroke)

    if not match:
        raise KeyError

    pre, init, mid, final, post = match.groups()

    phrase_parts = []

    if pre in PREINITIAL_MODIFIERS:
        phrase_parts.append(PREINITIAL_MODIFIERS[pre])
    elif pre != "":
        raise KeyError

    if init in INITIAL_BANK:
        phrase_parts.append(INITIAL_BANK[init])
    elif init != "":
        raise KeyError

    if mid in MIDDLE_MODIFIERS:
        phrase_parts.append(MIDDLE_MODIFIERS[mid])
    elif mid != "" and mid != "-":
        raise KeyError

    if final in FINAL_BANK:
        phrase_parts.append(FINAL_BANK[final])
    elif final != "":
        raise KeyError

    if post in POSTFINAL_MODIFIERS:
        phrase_parts.append(POSTFINAL_MODIFIERS[post])
    elif post != "":
        raise KeyError

    phrase = " ".join(phrase_parts)

    if not phrase:
        raise KeyError

    return phrase

def reverse_lookup(text):
    return []
