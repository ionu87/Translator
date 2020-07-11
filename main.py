from translate import Translator

translator = Translator(to_lang='pt')
translator1 = Translator(to_lang='ja')
#translator2 = Translator(to_lang='en')
translator3 = Translator(to_lang='zh')

try:
    with open('./text.txt', mode='r') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        translation1 = translator1.translate(text)
        #translation2 = translator.translate(text)
        translation3 = translator.translate(text)
        with open('./text_translated.txt', mode='w') as my_file2:
            my_file2.write(translation)
            my_file2.write('\n')
            my_file2.write(translation1)
            my_file2.write('\n')
            #my_file2.write(translation2)
            #my_file2.write('\n')
            my_file2.write(translation3)
            my_file2.write('\n')
except FileNotFoundError as err:
    print('Check your file path.')