import pandas as pd

col_def = pd.read_fwf('../data/bsc_label.txt', header=None, colspecs=(
    (0,4),
    (5,9),
    (9,17),
    (17,23),
    (23,34)
))

star_col_def = []
column_names = []

for _, (n1, n2, _, _, name) in col_def.iterrows():
    if not pd.isna(n1):
        star_col_def.append((int(n1)-1, int(n2)))
    else:
        star_col_def.append((int(n2)-1, int(n2)))
    column_names.append(name)

star_def = pd.read_fwf('../data/bsc5.dat', header=None, colspecs=star_col_def)
star_def.columns = column_names

col_def = pd.read_fwf('../data/bsc_label.txt', header=None, colspecs=(
    (0,4),
    (5,9),
    (9,17),
    (17,23),
    (23,34)
))

star_def = pd.read_fwf('../data/bsc5.dat', header=None, colspecs=star_col_def)
star_def.columns = column_names

print(star_def.head())
