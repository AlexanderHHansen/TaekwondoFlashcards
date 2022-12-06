from flashcards import TaekwondoFlashcards
from taekwondo import BeltDegree, TaekwondoScaper
import pickle

def main():
    tkd_scraper = TaekwondoScaper()
    data = tkd_scraper.get_taekwondo_data()
    degrees = [BeltDegree(**d) for d in data]       
    tkd_flash = TaekwondoFlashcards(degrees)
    tkd_flash.run()

if __name__ == '__main__':
    main()