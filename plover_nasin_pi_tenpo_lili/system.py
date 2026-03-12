KEYS = (
        'm-', 's-', 't-', 'k-', 'p-', 'n-', 'l-', 'j-',
        'e', '*',
        '-n'
    )

STENO_ORDER = KEYS

IMPLICIT_HYPHEN_KEYS = ('e') 

NUMBER_KEY = None 
NUMBERS = {}

FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = '*'

SUFFIX_KEYS = ()
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
            "Gemini PR": {
                },
            "Keyboard": {
                },
            "Passport": {
                },
            "Plover HID": {
                'S1-': 'm-',
                'T-': 't-',
                'K-': 'k-',
                'P-': 'p-',
                'W-': 'n-',
                'H-': 'l-',
                'R-': 'j-',
                'A-': 'e-',
                'O-': 'e-',
                '*': ('*1', '*2', '*3', '*4'),
                '-E': 'e',
                '-F': 'e',
                '-R': 'e',
                '-P': 'e',
                '-B': 'e',
                '-L': 'e',
                '-G': 'e',
                '-T': 'e',
                '-S': 'e',
                '-D': 'e',
                '-Z': 'e',
                    },
            "Sentura": {
                },
            "TX Bolt": {
                },
            "Treal": {
                },
            }

DICTIONARIES_ROOT = 'asset:plover_nasin_pi_tenpo_lili:dictionaries'
DEFAULT_DICTIONARIES = ('nasin-pi-tenpo-lili-base.json',)
