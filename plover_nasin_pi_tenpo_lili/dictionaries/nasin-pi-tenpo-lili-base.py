# i know what this does :3
LONGEST_KEY = 1

# phrasing crap I have no idea what I'm doing
PARTS_MATCHER = re.compile(
        r'([12]*)'              # Preinitial modifiers
        r'([mstkpnlj]*)'        # Initial word bank
        r'([12*34]*)'           # Middle modifiers
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
    assert len(outline) == 1

    stroke = "".join(outline)

    return "test"


def reverse_lookup(text):
    return []
