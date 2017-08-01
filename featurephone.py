from itertools import product

phone_feature_map = {
    'M': ('blb', 'nas'),
    'P': ('vls', 'blb', 'stp'),
    'B': ('vcd', 'blb', 'stp'),
    'F': ('vls', 'lbd', 'frc'),
    'V': ('vcd', 'lbd', 'frc'),
    'TH': ('vls', 'dnt', 'frc'),
    'DH': ('vcd', 'dnt', 'frc'),
    'N': ('alv', 'nas'),
    'T': ('vls', 'alv', 'stp'),
    'D': ('vcd', 'alv', 'stp'),
    'S': ('vls', 'alv', 'frc'),
    'Z': ('vcd', 'alv', 'frc'),
    'R': ('alv', 'apr'),
    'L': ('alv', 'lat'),
    'SH': ('vls', 'pla', 'frc'),
    'ZH': ('vcd', 'pla', 'frc'),
    'Y': ('pal', 'apr'),
    'NG': ('vel', 'nas'),
    'K': ('vls', 'vel', 'stp'),
    'G': ('vcd', 'vel', 'stp'),
    'W': ('lbv', 'apr'),
    'HH': ('glt', 'apr'),
    'CH': ('vls', 'alv', 'stp', 'frc'),
    'JH': ('vcd', 'alv', 'stp', 'frc'),
    'AO': ('lmd', 'bck', 'rnd', 'vwl'),
    'AA': ('low', 'bck', 'unr', 'vwl'),
    'IY': ('hgh', 'fnt', 'unr', 'vwl'),
    'UW': ('hgh', 'bck', 'rnd', 'vwl'),
    'EH': ('lmd', 'fnt', 'unr', 'vwl'),
    'IH': ('smh', 'fnt', 'unr', 'vwl'),
    'UH': ('smh', 'bck', 'rnd', 'vwl'),
    'AH': ('mid', 'cnt', 'unr', 'vwl'),
    'AE': ('low', 'fnt', 'unr', 'vwl'),
    'EY': ('lmd', 'smh', 'fnt', 'unr', 'vwl'),
    'AY': ('low', 'smh', 'fnt', 'cnt', 'unr', 'vwl'),
    'OW': ('umd', 'smh', 'bck', 'rnd', 'vwl'),
    'AW': ('low', 'smh', 'bck', 'cnt', 'unr', 'rnd', 'vwl'),
    'OY': ('lmd', 'smh', 'bck', 'fnt', 'rnd', 'unr', 'vwl'),
    'ER': ('umd', 'cnt', 'rzd', 'vwl'),
    '^': ('beg',),
    '$': ('end',)
}

def phone_to_features(ph):
    """Returns a feature tuple for an ARPAbet phone.

    >>> [phone_to_features(p) for p in 'CH IY1 Z'.split()]
    [('vls', 'alv', 'stp', 'frc'), ('hgh', 'fnt', 'unr', 'vwl'), ('vcd', 'alv', 'frc')]

    """
    if ph[-1] in '012':
        ph = ph[:-1]
    return phone_feature_map[ph]

def feature_bigrams(phones_list, include_reverse=True):
    """Takes a list of ARPAbet phones and returns a list of features.

    >>> feature_bigrams("M NG".split())
    ['blb-vel', 'blb-nas', 'nas-vel', 'nas-nas', 'vel-blb', 'vel-nas', 'nas-blb', 'nas-nas']
    >>> feature_bigrams(["OW1"])
    
    """
    # find n-grams of each successive pair
    grams = list()
    phones_list = ["^"] + phones_list + ["$"]
    for ph0, ph1 in zip(phones_list[:-1], phones_list[1:]):
        for item in product(*[phone_to_features(ph0), phone_to_features(ph1)]):
            grams.append('-'.join(item))

    # backwards too
    if include_reverse:
        phones_list = list(reversed(phones_list))
        for ph0, ph1 in zip(phones_list[:-1], phones_list[1:]):
            for item in \
                    product(*[phone_to_features(ph0), phone_to_features(ph1)]):
                grams.append('-'.join(item))

    return grams

if __name__ == '__main__':
    import doctest
    doctest.testmod()
