# Catalog Source: ftp://cdsarc.u-strasbg.fr/cats/V/50/
import csv
import re
from tqdm import tqdm

def load():
    file = open(r'..\data\catalog', mode="rb")

    return file

chunk_size = 197
Bright_Star_Number = 4
name = 9
dur_id = 10


def get_info(file):
    info = ''.encode('ascii')

    while True:
        chunk = file.read(180)
        info = info + chunk
        
        if not chunk:
            info = info.decode('ascii')
            info = [each for each in info.split('\n')]
            
            return info


def label_info(data):
    data = [each.split() for each in data]
    # print(data)
    info = {}
    info['hardvard_number'] = []
    info['name'] = []
    info['Durchmusterung ID'] = []
    info['Henry Draper Catalog Number'] = []
    info['SAO Catalog Number'] = []
    info['FK5 Star Number'] = []
    info['Infrared'] = []
    info['Infrared_ref'] = []

    
    for chunk in data:
        if chunk[:1]:
            info['hardvard_number'].append(chunk[0])
            info['name'].append(chunk[1])
            info['Durchmusterung ID'].append(chunk[2])
            info['Henry Draper Catalog Number'].append(chunk[3] if re.match(r'[1-225300]', chunk[3]) else '')
            info['SAO Catalog Number'].append(chunk[4] if re.match(r'[1-258997]', chunk[3]) else '')
            info['FK5 Star Number'].append(chunk[5] if re.match(r'\S+', chunk[5]) else '')
            info['Infrared'].append(chunk[6] if re.match('I', chunk[6]) else '')
            if info['Infrared'][-1] == chunk[6]:
                info['Infrared_ref'].append(chunk[7] if re.match(r'[ \':]', chunk[7]) else '')
            

    return info


# def label_data(info):
#     '''Decodes string lists, removes characters, finds valuable strings'''
#     Harvard_Revised_Number = None
#     last_Harvard_Revised_Number = None
#     for chunk in info[:3]:
#         # chunk = chunk.decode('ascii')
#         chunk = chunk.strip()
#         chunk = re.sub('\n', '', chunk)
#         Harvard_Revised_Number = re.findall(r'^\d+', chunk)
#         print(chunk)
        
#         if '' not in Harvard_Revised_Number and Harvard_Revised_Number[:1]:
#             Harvard_Revised_Number = int(''.join(Harvard_Revised_Number))

#             if last_Harvard_Revised_Number is None:
#                 print(f'\nHarvard_Revised_Number: {Harvard_Revised_Number}\n\n\n')

#             elif Harvard_Revised_Number == last_Harvard_Revised_Number + 1:
#                 print(f'\nHarvard_Revised_Number: {Harvard_Revised_Number}\n\n\n')
            
#             last_Harvard_Revised_Number = Harvard_Revised_Number

        # print('\n\n\n')
    

file = load()
info = get_info(file)
print(info)

info = label_info(info)
# print(len(info['hardvard_number']))
# print(len(info['name']))
# # info = decode_dic(info)
# print(info['hardvard_number'][:3])
# print(info['name'][:3])
# label_data(info)


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
