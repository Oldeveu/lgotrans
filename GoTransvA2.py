# Local Google Translator Version 0.2 bzw. Alpha 2 by oldeveu under MIT Licenc
from deep_translator import GoogleTranslator

orglang = ""
translang = ""
orgtext = ""
transtext = ""
repeat = True
finish = False
profil = 0
state = 0
usin = ""

def translateauto(translang, orgtext):
    print(GoogleTranslator(target=translang).translate(orgtext))

def translate(orglang, translang, orgtext):
    print(GoogleTranslator(source=orglang, target=translang).translate(orgtext))

print("Translator based on Google Translator")
print("written by oldeveu")
while repeat is True:
    print("Hallo.")
    profil = input(
        "Bitte wählen Sie zwischen dem 1. Profil: Übersetung Deutsch zu Russisch, 2. Profil: Übersetzung Russisch"
        " zu Deutsch oder 3. Individuell: ")
    if profil == "1":
        orgtext = input("Geben Sie den zu übersetzenden Text ein: ")
        translate("de", "ru", str(orgtext))
        finish = True

    elif profil == "2":
        orgtext = input("Geben Sie den zu übersetzenden Text ein: ")
        print(orgtext)
        translate("ru", "de", str(orgtext))
        finish = True
    elif profil != 1 or profil != 2:
        if state == 0:
            orglang = input("Bitte geben Sie die Orginalsprachkennung (de = deutsch, ru = russisch) ein: ")
            if len(orglang) == 2:
                state += 1

        elif state == 1:
            translang = input("Bitte geben Sie die Sprachkennung (de = deutsch, ru = russisch) ein, "
                              "in der der Text übersetzt werden soll: ")
            if len(translang) == 2:
                state += 1

            else:
                print("Fehler: Bitte nur die Spachkennung aus 2 Buchstaben eingeben.")
        elif state == 2:
            orgtext = input("Geben Sie den zu übersetzenden Text ein: ")
            if len(orgtext) > 0:
                if len(orglang) == 2:
                    translate(orglang, translang, str(orgtext))
                else:
                    translateauto(translang, str(orgtext))
                finish = True
    if finish is True:
        usin = input("Wollen Sie noch einen Text übersetzen (j = ja, alles andere = nein)? ")
        if usin == "j":
            finish = False
            repeat = True
        else:
            print("Programm wird beendet.")
            repeat = False
