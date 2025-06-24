import unicodedata
import regex

chinese_traditional = """我對這個無法估量的邀請深感榮幸，但我無法接受，我很抱歉。
我在黑暗的掩護下離開了家，背叛了家人的信任。
我做出了我知道會冒著丟臉的風險的選擇。
從那時起……我發誓：忠誠、勇敢、真實。
為了履行這個誓言，我必須回家，為我的家人做出補償。"""

english = """
I'm deeply honored by this immesurable invitation but with humble apologies I cannot accept it.
I left home under cover of darkness and betrayed my family's trust.
I made choices I knew would risk their dishonor.
Since then... I have pledged an oath: to be loyal, brave, and true.
In order to fulfill this oath, I must return home and make amends to my family.
"""

español = """Me siento profundamente honrada por esta inconmensurable invitación pero con humildad me disculpo por no poder aceptarla.
Salí de casa al amparo de la oscuridad y traicioné la confianza de mi familia; tomé decisiones que sabía que arriesgarían su deshonra.
Desde entonces... he hecho un juramento: ser leal, valiente y sincera.
Para cumplir este juramento, debo regresar a casa y hacer las paces con mi familia.
"""

if __name__ == "__main__":
    print(chinese_traditional)
    print(f"Total Chinese characters: {len(chinese_traditional)}")
    print(english)
    print(f"Total English characters: {len(english)}")
    print(español)
    print(f"Total Spanish characters: {len(español)}")
    # replace normalized characters with extended encoding in Spanish
    español_extended = unicodedata.normalize("NFKD", español)
    print(español_extended)
    print(f"Total Spanish characters (extended diacritics): {len(español_extended)}")

    languages = [chinese_traditional, english, español, español_extended]

    word_regex = regex.compile(r"(\p{L}\p{M}*)+")
    for lang in languages:
        for m in regex.finditer(word_regex, lang):
            print(m.group(0))
