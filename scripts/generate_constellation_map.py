import yale_bsc_parser
import sys
from pprint import pprint

stars, n = yale_bsc_parser.get_stars_in_constellation(sys.argv[1])
yale_bsc_parser.generate_stars_map(stars, n)

for star in stars:
    if star.rotation and star.lum:
        pprint(vars(star))
        print(star.lum)
        # print(star.name, star.mag, star.ra, star.dec, star.spectral_type, star.rotation, star.temperature)
    # else:
    #     print(star.name, star.mag, star.ra, star.dec, star.spectral_type, star.temperature)
