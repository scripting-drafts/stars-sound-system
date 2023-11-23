# Catalog Source: ftp://cdsarc.u-strasbg.fr/cats/V/50/
import csv
import re
from tqdm import tqdm

file = open(r'..\data\catalog', mode="rb")

chunk_size = 197
Bright_Star_Number = 4
name = 10
dur_id = 11


'''
1-  4  I4     ---     HR       [1/9110]+ Harvard Revised Number
                                    = 
   5- 14  A10    ---     Name     Name, generally Bayer and/or Flamsteed name
  15- 25  A11    ---     DM       Durchmusterung Identification (zone in
                                    bytes 17-19)
  26- 31  I6     ---     HD       [1/225300]? Henry Draper Catalog Number
  32- 37  I6     ---     SAO      [1/258997]? SAO Catalog Number
  38- 41  I4     ---     FK5      ? FK5 star Number
  
      42  A1     ---     IRflag   [I] I if infrared source
      43  A1     ---   r_IRflag  *[ ':] Coded reference for infrared source
      44  A1     ---    Multiple *[AWDIRS] Double or multiple-star code
  45- 49  A5     ---     ADS      Aitken's Double Star Catalog (ADS) designation
  50- 51  A2     ---     ADScomp  ADS number components
  52- 60  A9     ---     VarID    Variable star identification
  61- 62  I2     h       RAh1900  ?Hours RA, equinox B1900, epoch 1900.0 (1)
  63- 64  I2     min     RAm1900  ?Minutes RA, equinox B1900, epoch 1900.0 (1)
  65- 68  F4.1   s       RAs1900  ?Seconds RA, equinox B1900, epoch 1900.0 (1)
      69  A1     ---     DE-1900  ?Sign Dec, equinox B1900, epoch 1900.0 (1)
  70- 71  I2     deg     DEd1900  ?Degrees Dec, equinox B1900, epoch 1900.0 (1)
  72- 73  I2     arcmin  DEm1900  ?Minutes Dec, equinox B1900, epoch 1900.0 (1)
  74- 75  I2     arcsec  DEs1900  ?Seconds Dec, equinox B1900, epoch 1900.0 (1)
  76- 77  I2     h       RAh      ?Hours RA, equinox J2000, epoch 2000.0 (1)
  78- 79  I2     min     RAm      ?Minutes RA, equinox J2000, epoch 2000.0 (1)
  80- 83  F4.1   s       RAs      ?Seconds RA, equinox J2000, epoch 2000.0 (1)
      84  A1     ---     DE-      ?Sign Dec, equinox J2000, epoch 2000.0 (1)
  85- 86  I2     deg     DEd      ?Degrees Dec, equinox J2000, epoch 2000.0 (1)
  87- 88  I2     arcmin  DEm      ?Minutes Dec, equinox J2000, epoch 2000.0 (1)
  89- 90  I2     arcsec  DEs      ?Seconds Dec, equinox J2000, epoch 2000.0 (1)
  91- 96  F6.2   deg     GLON     ?Galactic longitude (1)
  97-102  F6.2   deg     GLAT     ?Galactic latitude (1)
 103-107  F5.2   mag     Vmag     ?Visual magnitude (1)
     108  A1     ---   n_Vmag    *[ HR] Visual magnitude code
     109  A1     ---   u_Vmag     [ :?] Uncertainty flag on V
 110-114  F5.2   mag     B-V      ? B-V color in the UBV system
     115  A1     ---   u_B-V      [ :?] Uncertainty flag on B-V
 116-120  F5.2   mag     U-B      ? U-B color in the UBV system
     121  A1     ---   u_U-B      [ :?] Uncertainty flag on U-B
 122-126  F5.2   mag     R-I      ? R-I   in system specified by n_R-I
     127  A1     ---   n_R-I      [CE:?D] Code for R-I system (Cousin, Eggen)
 128-147  A20    ---     SpType   Spectral type
     148  A1     ---   n_SpType   [evt] Spectral type code
 149-154  F6.3 arcsec/yr pmRA    *?Annual proper motion in RA J2000, FK5 system
 155-160  F6.3 arcsec/yr pmDE     ?Annual proper motion in Dec J2000, FK5 system
     161  A1     ---   n_Parallax [D] D indicates a dynamical parallax,
                                    otherwise a trigonometric parallax
 162-166  F5.3   arcsec  Parallax ? Trigonometric parallax (unless n_Parallax)
 167-170  I4     km/s    RadVel   ? Heliocentric Radial Velocity
 171-174  A4     ---   n_RadVel  *[V?SB123O ] Radial velocity comments
 175-176  A2     ---   l_RotVel   [<=> ] Rotational velocity limit characters
 177-179  I3     km/s    RotVel   ? Rotational velocity, v sin i
     180  A1     ---   u_RotVel   [ :v] uncertainty and variability flag on
                                    RotVel
 181-184  F4.1   mag     Dmag     ? Magnitude difference of double,
                                    or brightest multiple
 185-190  F6.1   arcsec  Sep      ? Separation of components in Dmag
                                    if occultation binary.
 191-194  A4     ---     MultID   Identifications of components in Dmag
 195-196  I2     ---     MultCnt  ? Number of components assigned to a multiple
     197  A1     ---     NoteFlag [*] a star indicates that there is a note
                                    (see file notes)'''

info = []

while True:
    chunk = file.read(197)
    # name = file.read(14)
    # hr_name = file.read(25)
    # discard = file.read(197-25)
    # info.extend([chunk, name, hr_name])
    
    info.append(chunk)
    
    # print(chunk)
    

    if not chunk:
        break



def label_data(info):
    '''Decodes string lists, removes characters, finds valuable strings'''
    Harvard_Revised_Number = None
    last_Harvard_Revised_Number = None
    for chunk in info[:32]:
        chunk = chunk.decode('ascii')
        chunk = chunk.strip()
        chunk = re.sub('\n', '', chunk)
        Harvard_Revised_Number = re.findall(r'^\d+', chunk)
        print(chunk)
        
        if '' not in Harvard_Revised_Number and Harvard_Revised_Number[:1]:
            Harvard_Revised_Number = int(''.join(Harvard_Revised_Number))
            
            if last_Harvard_Revised_Number is None:
                print(f'\nHarvard_Revised_Number: {Harvard_Revised_Number}\n\n\n')

            elif Harvard_Revised_Number == last_Harvard_Revised_Number + 1:
                print(f'\nHarvard_Revised_Number: {Harvard_Revised_Number}\n\n\n')
            
            last_Harvard_Revised_Number = Harvard_Revised_Number
    
    
label_data(info)


# info = [x for x in info if x != '']
# datalist = []

# for chunky in tqdm(info):
#     data = {}
#     chunky = re.sub(r'\s+', '\t', chunky)
#     chunk = chunky.split('\t')
#     chunk = list(filter(None, chunk))
#     data['Harvard Revised Number'] = chunk[0]
#     data['Name'] = chunk[1]
    
#     # ? 
#     # data['Henry Draper Catalog Number'] = chunk[2]
#     # data['SAO Catalog Number'] = chunk[3]
#     # data['FK5 star Number'] = chunk[4]
#     # SAO Catalog Number
    
#     datalist.append(data)
#     print(chunk)

# keys = datalist[0].keys()

# with open('../data/st_catalog.csv', 'w', encoding='ascii', newline='') as f:
#     dict_writer = csv.DictWriter(f, keys, dialect='excel', delimiter=';')
#     dict_writer.writeheader()
#     dict_writer.writerows(datalist)
