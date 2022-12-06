import pickle
from taekwondo import BeltDegree

class TaekwondoFlashcards:

    def __init__(self, degrees: list[BeltDegree]) -> None:
        if not degrees:
            with open('tkd.pkl', 'rb') as f:
                self.degrees = pickle.load(f)
        else:
            self.degrees = degrees

    def run(self) -> None:
        for i in self.degrees[0].stances:
            print(i.korean_name)
            inp = input()
            if inp == 'open':
                self.degrees[0].search_technique(i.korean_name)
            print(i.danish_name)

    def runner(self):
        self.__start_gui()
        self.__handle_input()

if __name__ == '__main__':
    pass