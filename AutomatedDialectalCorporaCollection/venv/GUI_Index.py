from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import tweepy
from scipy.io import arff
import pandas as pd
import csv
from vocabulary import *
from locations import *
from credentials import *
from functions import *
from tkinter import filedialog
access = True
dir=""
arff_dir=""
no_SW=""
w_SW=""
csv_no_SW=""
csv_w_SW=""

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 3000
        self.count_words = 0


    def on_status(self, status):
        if self.counter < self.limit:

            #keep geotagged tweets only
            loc =  status.user.location
            filtered=FALSE
            ####################LOCATION FROM GEO-TAG INFORMATION ######################
            if loc:
                loc=loc.lower()
                if (streaming_country=="Egyptian") and ("egypt" in loc or "مصر" in loc or "القاهرة" in loc
                                                     or "cairo" in loc or "assiot" in loc or "alexandria" in loc
                                                     or "mansoura" in loc):
                    filtered=TRUE
                elif (streaming_country == "Sudanese") and ("sudan" in loc or "khartoum" in loc or "السودان" in loc
                                                         or "الخرطوم" in loc or "madani" in loc or "مدني" in loc):
                    filtered=TRUE
                elif (streaming_country == "Moroccan")and ("morocco" in loc or "marakish" in loc
                                                        or "المغرب"in loc or "marrakech"in loc):
                    filtered = TRUE
                elif (streaming_country == "Libyan") and ("tripoli" in loc or "طرابلس" in loc or
                                        "ليبيا" in loc or "benghazi" in loc or "libya" in loc
                                                          or "بنغازي" in loc):
                    filtered = TRUE
                elif (streaming_country == "Algerian")and ("الجزائر" in loc or "algerie" in loc or "algeria" in loc):
                    filtered = TRUE
                elif (streaming_country == "Tunisian") and ("tunisia" in loc or "tunisie" in loc or "تونس" in loc):
                    filtered = TRUE
                elif (streaming_country == "Mauritanian")and ("nouakchott" in loc or "mauritania" in loc
                                                            or "موريتانيا" in loc or "نواكشوط" in loc):
                    filtered = TRUE
                elif (streaming_country == "Yemeni")and ("yemen" in loc or "sanaa" in loc or "اليمن" in loc
                                                        or "صنعاء" in loc or  "عدن" in loc):

                    filtered = TRUE
                elif (streaming_country == "Iraqi")and ("العراق" in loc or "iraq" in loc or "دجلة" in loc
                                                         or "baghdad" in loc or "كربلاء" in loc
                                                         or "عراق" in loc or "بغداد" in loc
                                                         or  "البصرة" in loc or "basrah" in loc ) :

                    filtered = TRUE
                elif (streaming_country == "Jordanian")and ("jordan" in loc or "amman" in loc or "عمان" in loc
                                                          or "الأردن" in loc or "الأردنية" in loc or "الاردن" in loc):
                    filtered = TRUE
                elif (streaming_country == "Omani")and ("عمان" in loc or "مسقط" in loc or "صلالة" in loc or
                                                        "oman" in loc or "muscat" in loc or "salalah" in loc or "sohar" in loc):
                    filtered=TRUE
                elif (streaming_country == "Saudi") and ("السعودية" in loc or "جدة" in loc or "ينبع" in loc
                                                                or "مكه" in loc or "الرياض" in loc or "الطائف" in loc or
                                                                "Saudi Arabia" in loc or "riyadh" in loc or "jeddah" in loc
                                                                or "dhahran" in loc):
                    filtered = TRUE
                elif (streaming_country == "Emirati")and("uae" in loc or "الإمارات" in loc or "دبي" in loc or
                                                     "abu dhabi" in loc or "dubai" in loc or "ابوظبي" in loc):
                    filtered = TRUE
                elif (streaming_country == "Qatari")and("qatar" in loc or "الدوحة" in loc or
                                                       "قطر" in loc or "doha" in loc):
                    filtered = TRUE
                elif (streaming_country == "Kuwaiti")and ("kuwait" in loc or
                                                         "الديرة" in loc or
                                                         "الكويت" in loc):
                    filtered = TRUE
                elif (streaming_country == "Bahraini")and ( "manamah" in loc or "bahrain" in loc or
                                                           "المنامه" in loc or "البحرين" in loc):
                    filtered = TRUE
                elif (streaming_country == "Syrian")and ("damascus" in loc or "syria" in loc or "دمشق" in loc
                                                         or  "سوريا" in loc or "aleppo" in loc or "حلب" in loc
                                                         or "حمص" in loc):
                    filtered = TRUE
                elif (streaming_country == "Palestinian")and ("gaza" in loc or "palestine" in loc or
                                                            "فلسطين" in loc or "غزه" in loc or "الضفة" in loc):
                    filtered = TRUE
                elif (streaming_country == "Lebanese")and ("lebanon" in loc or "beirut" in loc or "baalbak" in loc
                                                          or "بيروت" in loc or "لبنان" in loc or  "صيدا" in loc):
                    filtered = TRUE
                ####################WRITE ON OUTPUT FILE ######################
                if filtered:
                    self.counter+=1
                    mystr = status.text
                    mystr= stream(mystr)
                    mystr = re.sub('@[^\s]+', '@USERNAME', mystr)
                    #store row tweets
                    colorLog.insert(INSERT,  " %d, " %self.counter)
                    if(access==False):
                        writeTest(str(self.counter), mystr, streaming_country)
                    else:
                        write(str(self.counter),mystr ,streaming_country)
                    text=str(self.counter)+". "+mystr
                    print(text+"\n")
        else:
            return False

    ####################ERROR HANDELLING ######################
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

if __name__ == "__main__":
    ####################WRITE ON DATASET FILE ######################
    def write( tweet_id, tweet, cntr):
        tf = open("Corpora/Dialects_datasets/RawData/" + streaming_country + ".csv", 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(tf)
        tf.write(tweet_id+" ,"+tweet+" ," + cntr+"\n")

    ####################WRITE ON TESTSET FILE ######################
    def writeTest( tweet_id, tweet, cntr):
        tf = open("Corpora/Testset/RawData/" + streaming_country + ".csv", 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(tf)
        tf.write(tweet_id+" ,"+tweet+" ," + cntr+"\n")


    ####################ACCESS TWITTER API ######################
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    root = Tk() #Makes the window
    root.wm_title("Dialects corpora") #Makes the title that will appear in the top left
    root.config(background = "#FFFFFF")

    #LEFT GRID (DIALECTS LIST)
    leftFrame = Frame(root, width=200, height = 600)
    leftFrame.grid(row=0, column=0, padx=10, pady=2)
    lb = Listbox(leftFrame, bd=1, height=20, selectmode=MULTIPLE)
    for i in acts:
        lb.insert(END, i)
    lb.bind("<<ListboxSelect>>")
    lb.grid(row=0, column=2, padx=10, pady=2)


    #Right GRID (TEXT AREAS AND BOTTONS)
    rightFrame = Frame(root, width=200, height = 600)
    rightFrame.grid(row=0, column=1, padx=10, pady=2)

    scrollbar = Scrollbar(rightFrame, orient=VERTICAL)

    circleCanvas = Text(rightFrame, width=70, height=2, bg='white')
    circleCanvas.grid(row=0, column=0, padx=10, pady=2)

    btnFrame = Frame(rightFrame, width=200, height = 200)
    btnFrame.grid(row=1, column=0, padx=10, pady=2)

    colorLog = Text(rightFrame, width = 70, height = 10, takefocus=0)
    colorLog.grid(row=2, column=0, padx=10, pady=2)

    scrollb = Scrollbar(rightFrame, command=colorLog.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')
    colorLog['yscrollcommand'] = scrollb.set

    # streaming function
    def tweets(LOCATION, lexicon):
        # countries with low streams
        tweets=myStream.filter(languages=["ar"], track=lexicon, locations=LOCATION)


    #BROWES FILES FOR swr SWD PROCCESSING
    def browsefunc_SWR():
        selection()
        filename = filedialog.askopenfilenames(initialdir = dir,title = "Select file",filetypes = (('Excel Documents', '*.csv'),("all files","*.*")))
        files = root.tk.splitlist(filename)
        lst = list(files)
        N = []
        for file in lst:
            file = file.replace(dir+'/', '')
            i = fun(file, True, csv_no_SW, no_SW)
            colorLog.insert(INSERT, "Total number of records left after cleaning " + file + " : %d \n" % i)

    #BROWES FILES FOR PROCESSING
    def browsefunc_N_SWR():
        selection()
        filename = filedialog.askopenfilenames(initialdir = dir,title = "Select file",filetypes = (('Excel Documents', '*.csv'),("all files","*.*")))
        files = root.tk.splitlist(filename)
        lst = list(files)
        N = []
        for file in lst:
            file=file.replace(dir+'/','')
            i = fun(file, False, csv_w_SW, w_SW)
            colorLog.insert(INSERT, "Total number of records left after cleaning "+file+" : %d \n" %i)


    #BROWES FILES FOR MERGINING
    def browsefunc_merge():
        selection()
        filename = filedialog.askopenfilenames(initialdir = arff_dir,title = "Select file",filetypes = (('ARFF Documents', '*.arff'),("all files","*.*")))
        files = root.tk.splitlist(filename)
        lst = list(files)
        N=[]
        for l in lst:
            if(no_SW in l):
                status="No_SW"
                k = l.replace(no_SW,'')
            elif(w_SW):
                status="With_SW"
                k = l.replace(w_SW, '')
            k = k.replace('.arff', '')
            N.append(k)
        print(N)
        n=mergeFiles(lst,N, status,arff_dir)
        colorLog.insert(INSERT, "Total number of records im merged file : %d \n" %n)

    #SETTING THE DIALRECTRIES VARIALBLES

    def selection():
        global access, dir, arff_dir, no_SW, w_SW, csv_no_SW, csv_w_SW
        if (radio.get() == 1):
            access = True
            dir = train_dir
            arff_dir = train_arff_dir
            #arff directries
            no_SW = train_no_SW
            w_SW = train_w_SW
            #csv directories
            csv_no_SW = train_csv_no_SW
            csv_w_SW = train_csv_w_SW
        else:
            access = False
            dir = test_dir
            arff_dir = test_arff_dir
            no_SW = test_no_SW
            w_SW = test_w_SW

            csv_no_SW = test_csv_no_SW
            csv_w_SW = test_csv_w_SW

        # STREAMING TWEETS
    def start_streaming():
        selection()
        global streaming_country
        global tf
        i=0
        x=lb.curselection()
        for n in x:
            streaming_country = acts[n]
            circleCanvas.insert(0.0, 'Streaming %s tweets  ...\n ' % acts[n])
            colorLog.insert(INSERT, "tweets from %s ....\n" % acts[n])
            if n == 0:
                public_tweets = tweets(LOCATIONS1, Egy_lex)
            elif n == 1:
                public_tweets = tweets(LOCATIONS2, Sud_lex)
            elif n == 2:
                public_tweets = tweets(LOCATIONS3, Moro_lex)
            elif n == 3:
                public_tweets = tweets(LOCATIONS4, Tun_lex)
            elif n == 4:
                public_tweets = tweets(LOCATIONS5, Lib_lex)
            elif n == 5:
                public_tweets = tweets(LOCATIONS6, Alg_lex)
            elif n ==6:
                public_tweets = tweets(LOCATIONS7, Mauri_lex)
            elif n ==7:
                public_tweets = tweets(LOCATIONS8, Yem_lex)
            elif n == 8:
                public_tweets = tweets(LOCATIONS9, Irq_lex)
            elif n == 9:
                public_tweets = tweets(LOCATIONS10, Omn_lex)
            elif n == 10:
                public_tweets = tweets(LOCATIONS11, KSA_lex)
            elif n == 11:
                public_tweets = tweets(LOCATIONS12, UAE_lex)
            elif n == 12:
                public_tweets = tweets(LOCATIONS13, Qtr_lex)
            elif n == 13:
                public_tweets = tweets(LOCATIONS14, Kuw_lex)
            elif n == 14:
                public_tweets = tweets(LOCATIONS15, Bah_lex)
            elif n == 15:
                public_tweets = tweets(LOCATIONS16, Syr_lex)
            elif n ==16:
                public_tweets = tweets(LOCATIONS17, Pls_lex)
            elif n ==17:
                public_tweets = tweets(LOCATIONS18, Leb_lex)
            elif n ==18:
                public_tweets = tweets(LOCATIONS19, Jord_lex)

    #BOTTONS COLLECTION
    redBtn = Button(btnFrame, text="Collect", command=start_streaming)
    redBtn.grid(row=0, column=0, padx=10, pady=2)

    blueBtn = Button(btnFrame, text="pre-processing (SWR)", command=browsefunc_SWR)
    blueBtn.grid(row=0, column=1, padx=10, pady=2)

    greenBtn = Button(btnFrame, text="pre-processing", command=browsefunc_N_SWR)
    greenBtn.grid(row=0, column=2, padx=10, pady=2)

    greenBtn = Button(btnFrame, text="merge .arff files", command=browsefunc_merge)
    greenBtn.grid(row=0, column=3, padx=10, pady=2)

    yellowBtn = Button(btnFrame, text="Quit", command=root.quit)
    yellowBtn.grid(row=0, column=4, padx=10, pady=2)

    chk_state = BooleanVar()
    radio = IntVar()
    #TYPE OF CORPUS RADIO BOTTONS CHOICE
    chk = Radiobutton(btnFrame, text='Corpus', variable=radio, value=1, command=selection)
    chk2 = Radiobutton(btnFrame, text='Testset', variable=radio, value=2, command=selection)
    chk.grid(column=1, row=1)
    chk2.grid(column=2, row=1)

    root.mainloop() #start monitoring and updating the GUI
