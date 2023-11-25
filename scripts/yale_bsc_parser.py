import sys
import math

try:
    constellation = sys.argv[1]
except IndexError:
    print('usage:\n'
          'python {:s} <constellation>\n'
          'where <constellation> is the three-letter abbreviation for a'
          ' constellation name (e.g. Ori, Lyr, UMa, ...)'.format(sys.argv[0]))
    sys.exit(1)

class Star():
    """
    A class representing a star, with name, magnitude, right ascension (ra),
    declination (dec) and projected co-ordinates x,y calculated by a class
    method.

    """

    def __init__(self, name, mag, ra, dec):
        """
        Initializes the star object with its name and magnitude, and position
        as right ascension (ra) and declination (dec), both in radians.

        """

        self.name = name
        self.mag = mag
        self.ra = ra
        self.dec = dec

    def project_orthographic(self, ra0, dec0):
        """
        Calculates, stores and returns the projected co-ordinates (x, y) of
        this star's position using an orthographic projection about the
        angular position (ra0, dec0).

        """

        delta_ra = self.ra - ra0
        self.x = math.cos(self.dec) * math.sin(delta_ra)
        self.y = math.sin(self.dec) * math.cos(dec0)\
             - math.cos(self.dec) * math.cos(delta_ra) * math.sin(dec0)
        return self.x, self.y

stars = []
with open(r'..\data\bsc5.dat', 'r') as fi:
    for line in fi.readlines():
        # print(line[11:14])
        # line = line.decode('utf-8')
        if line[11:14] != constellation:
            # We have no interest of stars which do not belong to constellation
            continue
        name = line[4:14]
        try:
            mag = float(line[102:107])
        except ValueError:
            # some stars do not have magnitudes: ignore these entries
            continue
        # Right ascension (hrs, mins, secs), equinox J2000, epoch 2000.0
        ra_hrs, ra_min, ra_sec = [float(x) for x in (line[75:77],
                                                     line[77:79], line[79:83])]
        # Declination (hrs, mins, secs), equinox J2000, epoch 2000.0
        dec_deg, dec_min, dec_sec = [float(x) for x in (line[83:86],
                                                     line[86:88], line[88:90])]
        # Convert both RA and declination to radians
        ra = math.radians((ra_hrs + ra_min/60 + ra_sec/3600) * 15.)
        # NB in the Southern Hemisphere be careful to subtract the minutes and
        # seconds from the (negative) degrees.
        sgn = math.copysign(1, dec_deg)
        dec = math.radians(dec_deg + sgn * dec_min/60 + sgn * dec_sec/3600)

        # Create a new Star object and add it to the list of stars
        stars.append(Star(name, mag, ra, dec))

n = len(stars)
if n==0:
    print('Constellation {:s} not found.'.format(constellation))
    sys.exit(1)
else:
    print('Found {:d} stars in the constellation {:s}'.format(n,constellation))

# Now calculate the projected co-ordinates of each star, (x,y), finding the
# maximum and minimum values and hence the aspect ratio for our image.
# The "centre" of the constellation in RA, dec:
ra0 = sum([star.ra for star in stars]) / n
dec0 = sum([star.dec for star in stars]) / n

x, y = [None]*n, [None]*n

for i, star in enumerate(stars):
    # Orthographic projection (ra, dec) -> (x1, y1)
    x[i], y[i] = star.project_orthographic(ra0, dec0)
xmin, xmax, ymin, ymax = min(x), max(x), min(y), max(y)
aspect_ratio = (xmax-xmin)/(ymax-ymin)

# The stars will be output on a canvas of dimensions width x height, with
# some extra padding around the outside of the "paintable" area.
padding = 50
height = 500
width = int(height * aspect_ratio)

# Write the SVG image file for the constellation
with open('{:s}.svg'.format(constellation), 'w') as f:
    print('<?xml version="1.0" encoding="utf-8"?>', file=f)
    print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
    print('     xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
    print('     width="{:d}" height="{:d}" style="background: #000000">'
            .format(width + 2*padding, height + 2*padding), file=f)
    for star in stars:
        rx = (star.x - xmin) / (xmax - xmin)
        ry = (star.y - ymin) / (ymax - ymin)
        cx = padding + (1-rx) * (width - 2*padding)
        cy = padding + (1-ry) * (height - 2*padding)
        print('<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"'
              ' stroke="none" fill="#ffffff" name="{name:s}"/>'.format(
              cx=cx, cy=cy, r=max(1,5-star.mag), name=star.name), file=f)
    print('</svg>', file=f)