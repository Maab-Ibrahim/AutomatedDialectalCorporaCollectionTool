import re
import string


##############################Emoticons List################################
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                            u'\U00010000-\U0010ffff'
                            u"\u200d"
                            u"\u2640-\u2642"
                            u"\u2600-\u2B55"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\u3030"
                            u"\ufe0f"
                           u"\u2060-\u2069"
                           "]+", flags=re.UNICODE)


##############################Punctuations List################################
arabic_punctuations = '''\—`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations


##############################Arabic Numbers List###############################
arabic_numbers='٠‎١‎٢‎٣‎٤‎٥‎٦‎٧‎٨‎٩'

##############################Arabic Diacritics List#############################
arabic_diacritics = re.compile("""
                             ّ    | # Shadda
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)


                #####-----------Corpora Folders List-------------######

##############################Dialects Dataset Folders#############################
train_dir="C:\\Users\\maab_\\PycharmProjects\\AutomatedDialectalCorporaCollection\\venv\\Corpora\\Dialects_datasets\\RawData\\"
train_arff_dir="C:\\Users\\maab_\\PycharmProjects\\AutomatedDialectalCorporaCollection\\venv\\Corpora\\Dialects_datasets\\Cleaned\\ARFF_Format\\"
train_no_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Dialects_datasets/Cleaned/ARFF_Format/NO_SW/"
train_w_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Dialects_datasets/Cleaned/ARFF_Format/With_SW/"
train_csv_no_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Dialects_datasets/Cleaned/CSV_Format/NO_SW/"
train_csv_w_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Dialects_datasets/Cleaned/CSV_Format/With_SW/"

####################################Testset Folders################################
test_dir="C:\\Users\\maab_\\PycharmProjects\\AutomatedDialectalCorporaCollection\\venv\\Corpora\\Testset\\RawData\\"
test_arff_dir="C:\\Users\\maab_\\PycharmProjects\\AutomatedDialectalCorporaCollection\\venv\\Corpora\\Testset\\Cleaned\\ARFF_Format\\"
test_no_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Testset/Cleaned/ARFF_Format/NO_SW/"
test_w_SW = "C:/Users/maab_/PycharmProjectsvenv/Corpora/Testset/Cleaned/ARFF_Format/With_SW/"
test_csv_no_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Testset/Cleaned/CSV_Format/NO_SW/"
test_csv_w_SW = "C:/Users/maab_/PycharmProjects/AutomatedDialectalCorporaCollection/venv/Corpora/Testset/Cleaned/CSV_Format/With_SW/"

