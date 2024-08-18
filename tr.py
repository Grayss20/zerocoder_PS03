from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='ru')
word = translator.translate("dog")
print(word)
