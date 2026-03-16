# i know what this does :3
LONGEST_KEY = 1

# phrasing crap I have no idea what I'm doing


INITIAL_WORDS = {
        "m-": "mi",
        }
FINAL_WORDS = {
        "-m": "mi",
        }






# all the stuff I know about
def lookup(outline):
    assert len(outline) == 1

    stroke = outline[0]
    if stroke == "m":
        return "mi"
    else:
        raise KeyError


def reverse_lookup(text):
    return []
