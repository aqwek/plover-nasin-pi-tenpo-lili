import re

# i know what this does :3
LONGEST_KEY = 1

# phrasing crap I have no idea what I'm doing
PARTS_MATCHER = re.compile(
        r'([12]*)'              # Preinitial modifiers
        r'([mstkpnlj]*)'        # Initial word bank
        r'([12\*34]*|-)'        # Middle modifiers
        r'([ljpntkms]*)'        # Final word bank
        r'([12]*)'              # Postfinal modifiers
        )

PREINITIAL_MODIFIERS = {

        }

INITIAL_BANK = {
        "m-": "mi",
        }

MIDDLE_MODIFIERS = {

        }

FINAL_BANK = {
        "-m": "mi",
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

    if init in INITIAL_BANK:
        phrase_parts.append(INITIAL_BANK[init])

    if mid in MIDDLE_MODIFIERS:
        phrase_parts.append(MIDDLE_MODIFIERS[mid])

    if final in FINAL_BANK:
        phrase_parts.append(FINAL_BANK[final])

    if post in POSTFINAL_MODIFIERS:
        phrase_parts.append(POSTFINAL_MODIFIERS[post])

    phrase = "".join(phrase_parts).strip()

    if not phrase:
        raise KeyError

    return phrase

def reverse_lookup(text):
    return []
