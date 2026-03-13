KEYS = (
        'm-', 's-', 't-', 'k-', 'p-', 'n-', 'l-', 'j-',
        '1', '2', '*', '3', '4',
        '-l', '-j', '-p', '-n', '-t', '-k', '-m', '-s',
    )

STENO_ORDER = KEYS
IMPLICIT_HYPHEN_KEYS = (
        '1', '2', '*', '3', '4',
    )

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
                'A-': '1',
                'O-': '2',
                '*': ('*1', '*2', '*3', '*4'),
                '-E': '3',
                '-U': '4',
                '-F': '-m',
                '-R': '-s',
                '-P': '-t',
                '-B': '-k',
                '-L': '-p',
                '-G': '-n',
                '-T': '-l',
                '-S': '-j',
                '-D': '*',
                '-Z': '*',
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
