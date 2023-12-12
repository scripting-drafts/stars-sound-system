import yale_bsc_parser
# import sys
import csv
from notes import get_available_consts


# stars, n = yale_bsc_parser.get_stars_in_constellation(sys.argv[1])
# yale_bsc_parser.generate_stars_map(stars, n)

# TEST
consts = get_available_consts()


consts = list(consts)
consts.sort()
print(consts)

for const in consts:
    print(const)
    stars, _ = yale_bsc_parser.get_stars_in_constellation(const)

    datalist = []

    for star in stars:
        if star.rotation and star.lum:
            data = {}

            data['constellation'] = star.const
            data['star_num'] = star.star_num
            data['name'] = star.name
            data['magnitude'] = star.mag
            data['right ascendance'] = star.ra
            data['declination'] = star.dec
            data['spectral type'] = star.spectral_type
            data['rotation'] = star.rotation
            data['temperature'] = star.temperature
            data['luminosity'] = star.lum

            # data = star.name, star.mag, star.ra, star.dec, star.spectral_type, star.rotation, star.temperature, star.lum
            print(data)
        # else:
        #     print(star.name, star.mag, star.ra, star.dec, star.spectral_type, star.temperature)
            datalist.append(data)



            keys = datalist[0].keys()

            with open(f'../data/consts_catalog.csv', 'w', encoding='ascii', newline='') as f:
                dict_writer = csv.DictWriter(f, keys, dialect='excel', delimiter=';')
                dict_writer.writeheader()
                dict_writer.writerows(datalist)

# keys = datalist[0].keys()

# with open(f'../data/{sys.argv[1]}_catalog.csv', 'w', encoding='ascii', newline='') as f:
#     dict_writer = csv.DictWriter(f, keys, dialect='excel', delimiter=';')
#     dict_writer.writeheader()
#     dict_writer.writerows(datalist)