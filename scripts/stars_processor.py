import re
from math import floor
import numpy as np

class stars_processor():
    def __init__(self):
        '''Spectral type: O-A, 0-5
        TODO:
         - No rotation desginated for M and K class Spectral Types
          - Clarify what .5 means
        
        Additional Information:
        Class L dwarfs get their designation because they are cooler than M stars and L is the remaining letter alphabetically closest to M. 
        Class T dwarfs are cool brown dwarfs with surface temperatures between approximately 550 and 1,300 K (277 and 1,027 °C; 530 and 1,880 °F).
        Class Y brown dwarfs are cooler than those of spectral class T and have qualitatively different spectra from them.
        Class C were originally classified as R and N stars, these are also known as carbon stars.
        Class S stars have excess amounts of zirconium and other elements produced by the s-process (slow neutron capture process), and have more similar carbon and oxygen abundances than class M or carbon stars'''
        
    def get_rotation_velocity(self, spectral_type):
        letter = ''.join(re.findall(r'^(O|B|A|F|G)', spectral_type))    # |K|M
        num = int(''.join(re.findall(r'\d', spectral_type)))    # Gets only int

        r_scale = {
            'O0': 190,
            'B0': 200,
            'B5': 210,
            'A0': 190,
            'A5': 160,
            'F0': 95,
            'F5': 25,
            'G0': 12,
            'G9': 1

        }

        if type(num) is int:
            logarythmic_rotations_for_int = {
                f'O{num}': np.linspace(r_scale['O0'], r_scale['B0'], 9)[num-1],
                f'B{num}': np.linspace(r_scale['B0'], r_scale['A0'], 9)[num-1],
                f'A{num}': np.linspace(r_scale['A0'], r_scale['F0'], 9)[num-1],
                f'F{num}': np.linspace(r_scale['F0'], r_scale['G0'], 9)[num-1],
                f'G{num}': np.linspace(r_scale['G0'], r_scale['G9'], 9)[num-1]
            }
            
            logarythmic_rotations = logarythmic_rotations_for_int

        else:
            logarythmic_rotations_for_float = {
                f'O{num}': np.linspace(r_scale['O0'], r_scale['B0'], 9)[int(floor(num))],
                f'B{num}': np.linspace(r_scale['B0'], r_scale['A0'], 9)[int(floor(num))],
                f'A{num}': np.linspace(r_scale['A0'], r_scale['F0'], 9)[int(floor(num))],
                f'F{num}': np.linspace(r_scale['F0'], r_scale['G0'], 9)[int(floor(num))],
                f'G{num}': np.linspace(r_scale['G0'], r_scale['G9'], 9)[int(floor(num))]
            }

            logarythmic_rotations = logarythmic_rotations_for_float

        try:
            rotation = logarythmic_rotations[f'{letter}{num}']
            return rotation

        except Exception:
             return None