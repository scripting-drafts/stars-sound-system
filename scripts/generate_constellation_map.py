import yale_bsc_parser
import sys

stars, n = yale_bsc_parser.get_stars_in_constellation(sys.argv[1])
yale_bsc_parser.generate_stars_map(stars, n)

