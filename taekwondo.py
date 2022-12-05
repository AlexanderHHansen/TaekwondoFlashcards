import requests 
import xmltodict
import vlc

class TaekwondoScaper():

    def convert_encoding(self, dict: dict) -> None:
        """Inplace convert encoding for danish characters

        Args:
            dict (dict): dict of taekwondo theory
        """
        pass 

    def get_taekwondo_data(self) -> dict:
        res = requests.get("https://ahndk.com/teori/DTaF/teori_DTaF.xml")
        dict_data = xmltodict.parse(res.content, encoding="iso-8859-1")
        theory: list = dict_data['teorirod']['grad']
        #print(theory[0].keys())
        return theory

class Sound:
    def __init__(self, sound_url: str) -> None:
        self.sound = self.get_sound_url(sound_url)
    
    def get_sound_url(self, sound_url: str) -> None:
        if sound_url == None:
            return ''
        url = 'https://ahndk.com/teori/DTaF/lyd/'
        sound_name = sound_url.split('/')[-1]
        return url + sound_name

    def play_sound(self) -> None:
        p = vlc.MediaPlayer(self.sound)
        p.play()

class Fact:
    def __init__(self, **kwargs) -> None:
        self.korean_name = kwargs.get('ko', None)
        self.danish_name = kwargs.get('da', None)
        self.sound = Sound(kwargs.get('lyd', None))

class BeltDegree:
    def __init__(self, **kwargs) -> None:
        self.degree = kwargs['@id']
        self.stances = [Fact(**f) for f in kwargs['stande']['ord']]
        # self.kicks
        # self.hand_techniques
        # self.theory
        # self.extra

    def search_technique(technique_name: str) -> None:
        """Search youtube for technique

        Args:
            technique_name (str): name of technique
        """
        pass

class FlashCardEncoder():
    def __init__(self, belt_degrees: list[BeltDegree]) -> None:
        self.flashcards = self.theory_to_flashcards(belt_degrees)

    def theory_to_flashcards(belt_degrees: list[BeltDegree]) -> object:
        """Make flashcards from theory of each belt degree

        Args:
            belt_degrees (list[BeltDegree]): _description_

        Returns:
            object: _description_
        """
        pass

def main():
    tkd_scraper = TaekwondoScaper()
    data = tkd_scraper.get_taekwondo_data()
    print(data[2]['@id'])
    # BeltDegree(**data[0])
    # for d in data:
    #     try:
    #         belt = BeltDegree(**d)
    #         print(belt.degree)
    #     except Exception as e:
    #         print(e)
    #print(degress[0].stances[0].sound.sound)


if __name__ == '__main__':
    main()
