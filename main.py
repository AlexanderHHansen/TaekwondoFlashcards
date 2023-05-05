from encoder import FlashCardEncoder
from flashcards import TaekwondoFlashcards
from taekwondo import BeltDegree, TaekwondoScaper
import pickle

def main():
    tkd_scraper = TaekwondoScaper()
    data = tkd_scraper.get_taekwondo_data()
    theory = [BeltDegree(**d).theory for d in data]
    theory = [item for sublist in theory for item in sublist]
    FlashCardEncoder().encode_theory(theory).to_csv('theory.csv')

    #tkd_flash = TaekwondoFlashcards(degrees)
    #tkd_flash.run()

if __name__ == '__main__':
    main()