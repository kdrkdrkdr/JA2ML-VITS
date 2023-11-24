# -*- coding: utf-8 -*-
from ....hangulize import *


class German(Language):
    """For transcribing German."""

    __iso639__ = {1: 'de', 2: 'ger', 3: 'deu'}
    
    vowels = u'aeiouäöüyAEOU'
    cons = u'bcCdfghjJklmnNpqrsStTvwxzZß'
    notation = Notation([
        (u'y$',           'i'),
        (u'ä',            'A'),
        (u'ö',            'O'),
        (u'ü',            'y'),
        ('{ism|isr|raf}ael', 'aQel'),
        ('{mich|raff|raph}ael', 'aQel'),
        ('chloe',         'kloe'),
        ('^ch{lor|lot|rom|ron}', 'k'),
        ('christ',        'krist'),
        ('{a|A|e}ue',     'uQe'),
        ('{a|u}el$',      'Qel'),
        ('{man|sam}ue{l}', 'uQe'),
        ('oe$',           'oQe'),
        ('ue$',           'u'),
        ('ae',            'A'),
        ('oe',            'O'),
        ('ue',            'y'),
        ('Q',             ''),
        ('berg$',         'bErk'),
        ('burg$',         'burk'),
        ('evelyn',        'ewelin'),
        ('ev{@}',         'ew'),
        ('^xaver',        'xawer'),
        ('xx',            'x'),
        ('x',             'kS'),
        ('b$',            'p'),
        ('d$',            't'),
        ('{@}y',          'i'),
        ('tzsch',         'T'),
        ('sch',           'Z'),
        ('{@}chs',        'kS'),
        ('{a|o|u}ch',     'X'),
        ('ch',            'x'),
        ('eig$',          'eik'),
        ('ig$',           'ix'),
        ('{@|r}g$',       'k'),
        ('{@}h{<cons>}',  None),
        ('{@}h$',         None),
        ('{@}he{im|rr}',  'Qhe'),
        ('{a|e|o|u}he',   'Qe'),
        ('err$',          'eU'),
        ('rr',            'r'),
        ('ll',            'l'),
        ('deus',          'deQus'),
        ('{mathe|mathA}us', 'Qus'),
        ('{matthe|matthA}us', 'Qus'),
        ('Aus$',          'AQus'),
        ('eeuw$',         'eQu'),
        ('eeuws',         'eQus'),
        ('euw$',          'eQu'),
        ('euws',          'eQus'),
        ('euy',           'oi'),
        ('eu',            'oi'),
        ('Au',            'oi'),
        ('{@}ie',         'iQe'),
        ('{amali|emili}e', 'Qe'),
        ('{cA|ce}cilie',  'ciliQe'),
        ('{dan}iel',      'iQel'),
        ('{gabr}iel',     'iQel'),
        ('{lili}en',      'Qen'),
        ('{belgi|itali}en', 'Qen'),
        ('i{etta|ette}',  'iQ'),
        ('{tri}est',      'Qest'),
        ('ie',            'i'),
        ('Q',             ''),
        ('vi{ctor|ktor|ncen|nzen}', 'wi'),
        ('sven',          'swen'),
        ('vlad',          'wlad'),
        ('ei',            'ai'),
        ('nn',            'n'),
        ('{r|l}mm{@}',    'mQm'),
        ('mm',            'm'),
        ('{r|l|n|s}tt{@}', 'tQt'),
        ('tt',            't'),
        ('{r|l|m|s}pp{@}', 'pQp'),
        ('pp',            'p'),
        ('Q',             ''),
        ('aa',            'a'),
        ('ee',            'e'),
        ('ph',            'f'),
        ('ff',            'f'),
        ('pf',            'f'),
        ('th',            't'),
        ('kh',            'k'),
        ('{r|l|n}dt{@|r}', 'tt'),
        ('dt',            't'),
        ('{r|l|n}dd{@|r}', 'td'),
        ('dd',            'd'),
        ('{r}gg{@|l|r}',  'kg'),
        ('gg',            'g'),
        ('bb',            'b'),
        ('ck',            'k'),
        ('c{A|e|i|y}',    'C'),
        ('c',             'k'),
        ('{@|l|n|r|s}kk{@|l|r}', 'kQk'),
        ('kk',            'k'),
        ('Q',             ''),
        ('cques$',        'k'),
        ('cque$',         'k'),
        ('ques$',         'k'),
        ('que$',          'k'),
        ('quet$',         'ke'),
        ('qu{@}',         'kw'),
        ('q',             'k'),
        ('C',             'c'),
        ('tz',            'z'),
        ('zz',            'z'),
        ('ng{@|l}',       'Ng'),
        ('ng',            'N'),
        ('nk',            'Nk'),
        ('ss',            'S'),
        (u'ß',            'S'),
        ('{@}s{p|t|k}',   'S'),
        ('ts',            'c'),
        ('ds$',           'c'),
        ('ds{<cons>}',    'c'),
        ('s$',            'S'),
        ('s{p@|t@|k@}',   'Z'),
        ('s{@}',          'J'),
        ('tZ',            'T'),
        ('Z{@}',          'Sj'),
        ('Z$',            'Sju'),
        ('Z{<cons>}',     'Sju'),
        ('T{@}',          'c'),
        ('T$',            'cj'),
        ('T{<cons>}',     'cj'),
        ('x{<cons>}',     'xi'),
        ('x$',            'xi'),
        ('er$',           'U'),
        ('{@}r$',         'U'),
        ('b{c|d|f|g|h|j|J|k|m|n|p|s|S|t|v|w|z}', 'p'),
        ('d{b|c|f|g|h|j|J|k|l|m|n|p|s|S|v|w|z}', 't'),
        ('g{b|c|d|f|h|j|J|k|m|n|p|s|S|t|v|w|z}', 'k'),
        ('^U$',           (Jungseong(E),Jungseong(EO))),
        ('^{<cons>}U$',   (Jungseong(E),Jungseong(EO))),
        ('X',             (Choseong(H),)), # achlaut
        ('x',             (Choseong(H),)), # ichlaut
        ('b',             (Choseong(B),)),
        ('c',             (Choseong(C),)),
        ('d',             (Choseong(D),)),
        ('f',             (Choseong(P),)),
        ('g',             (Choseong(G),)),
        ('{ai|oi|au}k',   (Choseong(K),)),
        ('{@}k{c|s|S|t}', (Jongseong(G),)),
        ('k',             (Choseong(K),)),
        ('{@}l{m@|n@}',   (Jongseong(L),)),
        ('{@}l{@|m|n}',   (Jongseong(L), Choseong(L))),
        ('^l',            (Choseong(L),)),
        ('l{@}',          (Jongseong(L), Choseong(L))),
        ('l',             (Jongseong(L),)),
        ('m{@}',          (Choseong(M),)),
        ('m',             (Jongseong(M),)),
        ('n{@}',          (Choseong(N),)),
        ('n',             (Jongseong(N),)),
        ('N',             (Jongseong(NG),)),
        ('h',             (Choseong(H),)),
        ('{ai|oi|au}p',   (Choseong(P),)),
        ('{@}p{s|S|t}',   (Jongseong(B),)),
        ('p',             (Choseong(P),)),
        ('r',             (Choseong(L),)),
        ('s',             (Choseong(S),)),
        ('S',             (Choseong(S),)),
        ('J',             (Choseong(J),)),
        ('t',             (Choseong(T),)),
        ('v',             (Choseong(P),)),
        ('w',             (Choseong(B),)),
        ('z',             (Choseong(C),)),
        ('ja',            (Jungseong(YA),)),
        ('je',            (Jungseong(YE),)),
        ('ji',            (Jungseong(I),)),
        ('jo',            (Jungseong(YO),)),
        ('ju',            (Jungseong(YU),)),
        ('jy',            (Jungseong(WI),)),
        ('jO',            (Jungseong(OE),)),
        ('jA',            (Jungseong(YE),)),
        ('jU',            (Jungseong(YEO),)),
        ('U',             (Jungseong(EO),)),
        ('a',             (Jungseong(A),)),
        ('e',             (Jungseong(E),)),
        ('E',             (Jungseong(E),)),
        ('i',             (Jungseong(I),)),
        ('o',             (Jungseong(O),)),
        ('u',             (Jungseong(U),)),
        ('A',             (Jungseong(E),)),
        ('O',             (Jungseong(OE),)),
        ('y',             (Jungseong(WI),)),
        ('j',             (Jungseong(I),)),
    ])

    def normalize(self, string):
        additional = {u'Ä': u'ä', u'Ö': u'ö', u'Ü': u'ü', u'ß': u'ß'}
        return normalize_roman(string, additional)


__lang__ = German