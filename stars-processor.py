import re
from scripts.custom_arange import *

taurus = {'aldebaran': 'K5III'}

class stars_processor:
    def __init__(self):
        self.rotations = {
            'O0': 190,
            'B0': 200,
            'B5': 210,
            'A0': 190,
            'A5': 160,
            'F0': 95,
            'F5': 25,
            'G0': 12
        }

    def get_rotation(self, spectral_type=None):
        stellar_class_let = ''.join(re.findall(r'^\D', spectral_type))
        print(stellar_class_let)
        stellar_class_num = int(''.join(re.findall(r'\d', spectral_type)))
        print(stellar_class_num)

        if f'{stellar_class_let}{stellar_class_num}' in self.rotations.keys():
            rotation = self.rotations[f'{stellar_class_let}{stellar_class_num}']

        else:   # F9
            possibles = [x for x in self.rotations.keys() if x.startswith(stellar_class_let)]
            possibles_nums = [x[1] for x in possibles]

            # if not possibles_nums[1:]:  # If contains only one
            #     possible_num = possibles_nums[0]

            stclass_num_interval = range(min(possibles_nums), max(possibles_nums) + 1, 1)

            if stellar_class_num in stclass_num_interval:
                rotations_range = np_arange_inclusive(float(self.rotations[possibles[0]]), float(self.rotations[possibles[1]]), 6.)
                rotation = rotations_range[rotations_range.index(stellar_class_num)]

            #     asd = [x for x in possibles]
            # def get_interval(st_class1, st_class2):
            #     return

        return rotation
    
    def get_temperature(self):
        return
    
    def get_luminosity(self):
        return
    

sp = stars_processor()
r = sp.get_rotation(taurus['aldebaran'])
print(r)