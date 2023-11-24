
from text.hangulize import hangulize, langs
import re
from g2pk3 import G2p

g2pK = G2p()

lang_code_lst = {
    'KO', # 한국어
    'JA', # 일본어
    'EN', # 영어
    'ID', # 인도네시아어
    'VI', # 베트남어
    'RU', # 러시아어
    'TR', # 터키어
    'ES', # 스페인어
    'PT', # 포르투갈어
    'IT', # 이탈리아어
    'PO', # 폴란드어
    'DE', # 독일어
    'NL', # 네덜란드어
    'UK', # 우크라이나어
    'SV', # 스웨덴어
    'CS', # 체코어
    'FI', # 핀란드어
    'LA', # 라틴어
    'HU', # 헝가리어
}



def to_korean(text:str, lang_code:str):
    lang_code = lang_code.upper()
    text = text+' '
    if lang_code in ('KO', 'JA'):
        return text
    return hangulize(text, lang_code)



def ml2_jke(text):
    for lc in lang_code_lst:
        lc = lc.upper()

        if not lc in ('JA', 'KO', 'EN'):
            text = re.sub(
                rf'\[{lc}\](.*?)\[{lc}\]', 
                lambda x: to_korean(x.group(1), lc).strip()+' ', 
                text
            )

        else:
            text = re.sub(
                rf'\[{lc}\](.*?)\[{lc}\]', 
                lambda x: x.group(1)+' ', 
                text
            )
    return text