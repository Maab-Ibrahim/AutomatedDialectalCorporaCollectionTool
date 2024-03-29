import re
import string
######################Dialects Names #########################################
acts = [
        "Egyptian","Sudanese","Moroccan","Tunisian","Libyan","Algerian","Mauritanian",
        "Yemeni","Iraqi",
        "Omani", "Saudi", "Emirati", "Qatari", "Kuwaiti", "Bahraini",
        "Syrian", "Palestinian", "Lebanese","Jordanian"
            ]
####################List of Boundry boxes for Every country#####################

##############################Egypt Boundry Boxes################################
LOCATIONS1 = [
    24.9936654321, 21.9759289458, 34.1937819243, 31.7159313619  # Egypt
    ,
    34.1539756186, 22.0119315241, 34.7020122979, 30.4216821925  # Egypt
    ,
    34.176259434, 22.0119315241, 36.6988271627, 25.7973104071  # Egypt
]
##############################Sudan Boundry Boxes################################
LOCATIONS2 = [
    25.2190261589, 17.8656064302, 38.3590371912, 22.0512744406  # Sudan
    ,
    24.0676873044, 13.3250638566, 36.0374627721, 20.1707590993  # Sudan
    ,
    22.9355826705, 9.9636591752, 32.2842460712, 15.6692555633  # Sudan
    ,
    33.3073419643, 11.712553094, 36.2138446338, 16.6624956089  # Sudan
]
##############################Morocco Boundry Boxes################################
LOCATIONS3 = [
    -9.7372751976, 29.533524002, -1.5163004043, 36.5062574776  # Morocco
    ,
    -12.5976889927, 26.91345513, -5.1653615443, 33.8276807869  # Morocco
    ,
    -17.5850552973, 21.903118988, -2.9226678087, 36.3970360674  # Morocco
]
##############################Tunisia Boundry Boxes################################
LOCATIONS4 = [
    8.4227076143, 34.1635009955, 11.4975913472, 37.626758607  # Tunisia
    ,
    7.7659353232, 33.2383695102, 11.5572976085, 34.4347819494  # Tunisia
    ,
    8.6167527928, 32.2402399552, 11.5572976085, 33.1884165161  # Tunisia
    ,
    9.3234429525, 30.4292380317, 10.216975499, 32.5804800284  # Tunisia
    ,
    8.3883483507, 32.4491520597, 11.4559085189, 33.6187766517  # Tunisia
]
##############################Lybia Boundry Boxes################################
LOCATIONS5 = [
    9.8145060211, 22.5221715448, 20.4804842839, 32.6705700127  # Lybia
    ,
    9.2672472821, 28.2999935771, 15.5551877328, 34.1201731138  # Lybia
    ,
    9.7357207798, 24.6785964019, 12.4040051237, 30.4283582698  # Lybia
    ,
    20.1187596162, 21.3421213121, 24.8910486124, 33.0188355741  # Lybia
    ,
    22.3829422685, 20.1094878858, 24.8925542294, 21.3471733769  # Lybia
    ,
    12.8049606367, 22.2039148865, 22.8601106044, 32.7348805645  # Lybia
]
##############################Algeria Boundry Boxes################################
LOCATIONS6 = [
    -2.2545604116, 32.5546708912, 8.2488503914, 37.6262904021  # Algeria
    ,
    -0.9100511404, 22.184044792, 8.679076186, 32.3463724534  # Algeria
    ,
    -8.8029630073, 23.7836207945, -1.1280256647, 29.4990732235  # Algeria
    ,
    -5.5374845481, 26.2154175917, 1.5377007268, 32.2247257685  # Algeria
    ,
    4.2294466825, 20.4619182414, 11.3046319574, 26.7710164264  # Algeria
    ,
    1.2033877429, 18.7176415013, 8.7030680753, 25.5320172829  # Algeria
]
##############################Mauritania Boundry Boxes################################
LOCATIONS7 = [
    -11.9151770346, 15.3151101762, -5.5863225387, 26.1775717  # Mauritania
    ,
    -17.0184493466, 16.4478072234, -11.0456849318, 21.8141057056  # Mauritania
    ,
    -13.2999843842, 15.2981901452, -8.5813819544, 18.2691604519  # Mauritania
    ,
    -11.9116168609, 23.442139546, -8.2480027986, 26.0569502503  # Mauritania
    ,
    -8.7279709491, 24.5826265095, -6.0003705508, 26.9413899567  # Mauritania
]
##############################Yemen Boundry Boxes################################
LOCATIONS8 = [
    47.3603797326, 14.1419106312, 53.3078036317, 18.9546194405  # Yemen
    ,
    42.1175298022, 12.2336374508, 47.0441837523, 17.3415897284  # Yemen
    ,
    44.608770404, 12.9281770423, 49.1954658933, 17.2922705154  # Yemen
]
##############################Iraq Boundry Boxes################################
LOCATIONS9 = [
    41.086337966, 33.5386044324, 46.0977586546, 37.5977147391  # Iraq
    ,
    38.6666206657, 32.0036610937, 42.6552408876, 34.8282857765  # Iraq
    ,
    41.0855964157, 30.1730288108, 46.3106657261, 34.7239521148  # Iraq
    ,
    43.7321652638, 29.0102444876, 48.2669631023, 32.8521677055  # Iraq
]
##############################Oman Boundry Boxes################################
LOCATIONS10 = [
    55.1894456333, 21.1391018162, 60.4531925607, 24.6508727199  # Oman
    ,
    54.9829199994, 18.7608551627, 59.1281020028, 22.3113970998  # Oman
    ,
    52.0678929963, 15.9337646404, 56.3346665853, 20.0593892635  # Oman
    ,
    55.8901751063, 25.688564762, 56.9837791618, 26.7515494983  # Oman
]
##############################Saudi Arabia Boundry Boxes################################
LOCATIONS11 = [
    34.7024190501, 16.522558429, 44.4063755641, 29.8204336129  # Saudi Arabia
    ,
    37.4152183121, 17.4899226686, 48.4108295811, 31.744353864  # Saudi Arabia
    ,
    38.7121943628, 17.0633411047, 49.6123745451, 30.9507550058  # Saudi Arabia
    ,
    38.7121943628, 17.0633411047, 49.6123745451, 30.9507550058  # Saudi Arabia
    ,
    47.5092769528, 18.4801087474, 55.0863273225, 22.7055423461  # Saudi Arabia
    ,
    53.0737131088, 19.9402126466, 55.706791708, 22.9099600535  # Saudi Arabia
]
##############################Emerits Boundry Boxes################################
LOCATIONS12 = [
    52.4245734371, 22.6172352021, 55.3893442352, 24.1333764032  # UAE
    ,
    54.1622268534, 23.9073356526, 55.9532739664, 25.4674448008  # UAE
    ,
    54.9224018097, 24.9680511838, 56.4902798513, 25.7467762069  # UAE
    ,
    51.5915269326, 23.259810889, 53.2114910839, 24.6462248324  # UAE
]
##############################Qatar Boundry Boxes################################
LOCATIONS13 = [
    50.6344698716, 24.5517428864, 51.8753132352, 26.2424252801  # Qatar
]
##############################Kuwait Boundry Boxes################################
LOCATIONS14 = [
    46.833120391, 28.8497997895, 48.2067664104, 30.171415496  # Kuwait
    ,
    47.7275879065, 28.6297883759, 48.3744788868, 29.9531280395  # Kuwait
]
##############################Bahrain Boundry Boxes################################
LOCATIONS15 = [
    50.3446728295, 25.7213758311, 50.9529714349, 26.5246572491  # Bahrain
]
##############################Syria Boundry Boxes################################
LOCATIONS16 = [
    36.9246812279, 34.8966743551, 41.029711016, 36.678576559  # Syria
    ,
    35.7861793729, 34.5804234751, 36.9567498004, 35.838130338  # Syria
    ,
    35.9756332789, 32.32106964, 41.0276009176, 35.7309197727  # Syria
    ,
    35.7322564952, 34.1077071757, 38.7976482821, 36.7239893756  # Syria
]
##############################Palestine Boundry Boxes################################
LOCATIONS17 = [
    34.1224457636, 31.2651473189, 35.7135327589, 33.1398060272  # Palestine
    ,
    34.1506760177, 30.6056372324, 35.3698697051, 31.8846199889  # Palestine
]
##############################Lebanon Boundry Boxes################################
LOCATIONS18 = [
    35.4435072531, 33.9181764993, 36.3315866172, 34.6352631167  # Lebanon
    ,
    34.7500678947, 33.0547342504, 36.1502030817, 34.3365581152  # Lebanon
]
##############################Jordan Boundry Boxes################################
LOCATIONS19 = [
    35.0945739047, 29.28340831, 37.1243748324, 32.371796049  # Jordan
    ,
    35.2731660323, 29.965961917, 37.7669315614, 32.5864634272  # Jordan
    ,
    35.5759228132, 30.9367600743, 39.1216228655, 32.9885175052  # Jordan
]
