from typing import Self
from taekwondo import Technique
from taekwondo import BeltDegree
import pandas as pd

class FlashCardEncoder():

    def __init__(self) -> None:
        self.danish_to_korean: list[tuple[str, str]] = [] 

    def encode_belt_degrees(self, belt_degrees: list[BeltDegree]) -> Self:
        for belt in belt_degrees:
            if belt.degree == '':
               for s in belt.stances:
                  self.danish_to_korean.append((s.danish_name, s.korean_name))
               for h in belt.hand_techniques:
                  self.danish_to_korean.append((h.danish_name, h.korean_name))
               for k in belt.kicks:
                  self.danish_to_korean.append((k.danish_name, k.korean_name))
               for t in belt.theory:
                  self.danish_to_korean.append((t.danish_name, s.korean_name))
               for e in belt.extra:
                  self.danish_to_korean.append((e.danish_name, e.korean_name))

        return self

    def encode_theory(self, theory: list[Technique]) -> Self:
        for t in theory:
            self.danish_to_korean.append((t.danish_name, t.korean_name))
          
        return self

    def to_csv(self, path: str) -> None:
        df = pd.DataFrame(self.danish_to_korean, columns=['danish', 'korean'])
        df.to_csv(path, header=False, index=False)