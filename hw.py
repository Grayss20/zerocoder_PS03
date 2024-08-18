from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests


def get_english_words():
    url = "http://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }

    except Exception as e:
        print("error", e)


def word_game():
    print("Welcome to word game. Provide your answers in Russian")
    while True:
        word_dict = get_english_words()
        translator = GoogleTranslator(source='auto', target='ru')
        word = translator.translate(word_dict.get("english_words"))
        word_def = translator.translate(word_dict.get("word_definition"))
        print(f"Word definition: {word_def}")
        user = input("What is the word?")
        if user == word:
            print("Correct")
        else:
            print(f"Wrong. The word was {word}")

        play_again = input("Do you want to play again? (y/n)")
        if play_again.lower() == "y":
            continue
        else:
            break


word_game()
