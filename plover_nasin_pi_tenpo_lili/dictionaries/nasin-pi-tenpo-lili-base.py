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
        "mt": "mute",
        "mk": "moku",
        "mp": "musi",
        "mn": "ma",
        "ml": "wile",
        "mj": "mu",
        "st": "sitelen",
        "sk": "sona",
        "sp": "ale",
        "sn": "sama",
        "sl": "ike",
        "sj": "soweli",
        "tk": "awen",
        "tp": "tenpo",
        "tl": "ilo",
        "tn": "tomo",
        "tj": "tu",
        "kp": "pana",
        "kn": "kepeken",
        "kl": "lukin",
        "kj": "ijo",
        "pn": "tawa",
        "pl": "pilin",
        "pj": "pali",
        "nl": "ante",
        "nj": "ona",
        "lj": "weka",
        "mst": "jo",
        "msk": "kalama",
        "msp": "wan",
        "msn": "wawa",
        "msl": "lape",
        "msj": "sin",
        "mtk": "telo",
        "mtp": "luka",
        "mtl": "pini",
        "mtj": "nanpa",
        "mkp": "suno",
        "mkn": "sewi",
        "mkl": "suwi",
        "mkj": "kon",
        "mpn": "poka",
        "mpl": "olin",
        "mpj": "kasi",
        "mnl": "mama",
        "mnj": "moli",
        "mlj": "waso",
        "stk": "kute",
        "stp": "insa",
        "stn": "utala",
        "stl": "kili",
        "stj": "poki",
        "skp": "len",
        "skn": "n",
        "skl": "open",
        "spn": "kala",
        "spl": "kiwen",
        "spj": "pimeja",
        "snl": "linja",
        "slj": "alasa",
        "tkp": "mani",
        "tkn": "mun",
        "tkl": "ko",
        "tkj": "pipi",
        "tpn": "uta",
        "tpl": "sijelo",
        "tpj": "kule",
        "tnl": "pan",
        "tnj": "anpa",
        "tlj": "meli",
        "kpl": "esun",
        "kpj": "akesi",
        "knl": "monsuta",
        "knj": "loje",
        "klj": "palisa",
        "pnl": "supa",
        "pnj": "lete",
        "plj": "wa",
        "nlj": "mije",
        "mstk": "suli",
        "mstp": "noka",
        "mstn": "tonsi",
        "mstl": "laso",
        "mstj": "walo",
        "mskp": "nena",
        "mskl": "jelo",
        "mskj": "sinpin",
        "mspl": "lupa",
        "mslj": "lipu",
        "mspj": "selo",
        "msnl": "\"",
        "msnj": "leko",
        "mtkp": "namako",
        "mtkn": "kipisi",
        "mtkl": "monsi",
        "mtkj": "soko",
        "mtpl": "nimi",
        "mtpn": "lawa",
        "mtpj": "jaki",
        "mtnj": "pakala",
        "tkpn": "sike",
        "tpnl": "kulupu",
        "sknj": "nasin",
        "pnlj": "lili",
        "stpj": "anu",
        "mknl": "seme",
        "mtkpj": "misikeke",
        "mtpnj": "nimisin",
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
    
    if init != "" and not initial_word:
        raise KeyError

    if mid != "" and mid != "-" and not mod_word:
        raise KeyError

    if final != "" and not final_word:
        raise KeyError

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
