import requests 
import xmltodict
import vlc
from typing import Any
import traceback 
import charade
import webbrowser

class TaekwondoScaper():

    def get_taekwondo_data(self):
        data = self.__get_taekwondo_data()
        self.__convert_encoding(data)
        self.__convert_sound_urls(data)
        return data

    def __convert_encoding(self, data: dict) -> None:
        """Inplace convert encoding for danish characters

        Args:
            dict (dict): dict of taekwondo theory
        """
        #print(data[0]['håndteknikker'])
        #print(charade.detect(str(data).encode()))

    def __get_taekwondo_data(self) -> dict:
        res = requests.get("https://ahndk.com/teori/DTaF/teori_DTaF.xml")
        dict_data = xmltodict.parse(res.content, encoding="iso-8859-1")
        theory: list = dict_data['teorirod']['grad']
        #print(theory[0].keys())
        return theory

    def __convert_sound_urls(self, dict: dict):
        pass

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
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self.korean_name = kwargs.get('ko', None)
        self.danish_name = kwargs.get('da', None)
        self.sound = Sound(kwargs.get('lyd', None))
        self.img = None

class BeltDegree:
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self.degree = kwargs['@id']
        self.stances = self.__init_prop(kwargs['stande'], 'ord')
        self.hand_techniques = self.__init_prop(kwargs['håndteknikker'], 'ord')
        self.kicks = self.__init_prop(kwargs['benteknikker'], 'ord')
        self.theory = self.__init_prop(kwargs['teori'], 'ord')
        self.extra = self.__init_prop(kwargs['diverse'], 'ord')

    def __init_prop(self, dict: dict, key: str) -> list[Fact]:
        if 'ord' not in dict:
            return []
        elif isinstance(dict[key], list):
            return [Fact(**f) for f in dict[key]]
        else:
            return [Fact(**dict[key])]


    def search_technique(self, technique_name: str) -> None:
        """Search youtube for technique

        Args:
            technique_name (str): name of technique
        """
        name = technique_name.replace(' ', '+')
        url = f'https://www.youtube.com/results?search_query={name}'
        webbrowser.open(url)

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

if __name__ == '__main__':
    pass
