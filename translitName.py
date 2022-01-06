import streamlit as st
import pandas as pd
import numpy as np
from google.transliteration import transliterate_text, transliterate_word
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
sns.set()
import datetime as dt
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable
# disable python warnings
import sys
import warnings


if not sys.warnoptions:
    warnings.simplefilter("ignore")


st.title('Script your name')
user_input = st.text_input("Put your name here in latin script")
#st.write('Echo', user_input)

def japanese_rewrite(text):   
    if text.endswith(('t','d')):
        text = text + 'o' 
    if text.endswith(('b','c','f','g','h','j','k','l','m','p','q','r','s','v','w','x','z')):
        text = text + 'u'
    japanese_rewrite0 = re.sub( r'[c][h]', r'k', text)
    japanese_rewrite1 = re.sub( r"(([t|d])([bcdfghjklmnpqrstvwxz]))", r'\2o\3', japanese_rewrite0)
    japanese_rewrite2 = re.sub( r"(([b|c|f|g|h|j|k|l|m|n|p|q|r|s|v|w|x|z])([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z]))", r'\2u\3', japanese_rewrite1)
    if japanese_rewrite2.__eq__(text):
        return text
    else:
        return japanese_rewrite(japanese_rewrite2)

        
#from polyglot.text import Text
#Text(user_input).transliterate("ar")


arabic = transliterate_text(user_input, lang_code='ar')
#chinese = transliterate_text(user_input, lang_code='zh')
chinese = transliterate_text(user_input, lang_code='zh-hant')
hebrew = transliterate_text(user_input, lang_code='he')
hindi = transliterate_text(user_input, lang_code='hi')
japanese = transliterate_text(japanese_rewrite(user_input.lower()), lang_code='ja')
russian =  transliterate_text(user_input, lang_code='ru')
tamil =  transliterate_text(user_input, lang_code='ta')
thai = transliterate_text(japanese_rewrite(user_input.lower()), lang_code='th')
persian =  transliterate_text(user_input, lang_code='fa')
greek = transliterate_text(user_input, lang_code='el')
sinhala = transliterate_text(user_input, lang_code='si')
amharic = transliterate_text(user_input, lang_code='am')

latin = user_input





name_in_scripts = []

name_in_scripts.append(['FJI','hindi',True])
name_in_scripts.append(['TZA','arabic',False])
name_in_scripts.append(['ESH','arabic',False])
name_in_scripts.append(['CAN','latin',False])
name_in_scripts.append(['USA','latin',False])
name_in_scripts.append(['KAZ','cyrillic',False])
name_in_scripts.append(['UZB','latin',False])
name_in_scripts.append(['PNG','latin',False])
name_in_scripts.append(['IDN','latin',False])
name_in_scripts.append(['ARG','latin',False])
name_in_scripts.append(['CHL','latin',False])
name_in_scripts.append(['COD','latin',True])
name_in_scripts.append(['SOM','latin',False])
name_in_scripts.append(['KEN','latin',False])
name_in_scripts.append(['SDN','arabic',False])
name_in_scripts.append(['TCD','arabic',False])
name_in_scripts.append(['HTI','latin',False])
name_in_scripts.append(['DOM','latin',False])
name_in_scripts.append(['RUS','cyrillic',True])
name_in_scripts.append(['BHS','latin',False])
name_in_scripts.append(['FLK','latin',False])
name_in_scripts.append(['GRL','latin',False])
name_in_scripts.append(['ATF','none',False])
name_in_scripts.append(['TLS','latin',False])
name_in_scripts.append(['ZAF','latin',False])
name_in_scripts.append(['LSO','latin',False])
name_in_scripts.append(['MEX','latin',True])
name_in_scripts.append(['URY','latin',False])
name_in_scripts.append(['BRA','latin',False])
name_in_scripts.append(['BOL','latin',False])
name_in_scripts.append(['PER','latin',False])
name_in_scripts.append(['COL','latin',False])
name_in_scripts.append(['PAN','latin',False])
name_in_scripts.append(['CRI','latin',False])
name_in_scripts.append(['NIC','latin',False])
name_in_scripts.append(['HND','latin',False])
name_in_scripts.append(['SLV','latin',False])
name_in_scripts.append(['GTM','latin',False])
name_in_scripts.append(['BLZ','latin',False])
name_in_scripts.append(['VEN','latin',False])
name_in_scripts.append(['GUY','latin',False])
name_in_scripts.append(['SUR','latin',False])
name_in_scripts.append(['ECU','latin',False])
name_in_scripts.append(['PRI','latin',False])
name_in_scripts.append(['JAM','latin',False])
name_in_scripts.append(['CUB','latin',False])
name_in_scripts.append(['ZWE','latin',False])
name_in_scripts.append(['BWA','latin',False])
name_in_scripts.append(['NAM','latin',False])
name_in_scripts.append(['SEN','latin',False])
name_in_scripts.append(['MLI','latin',False])
name_in_scripts.append(['MRT','arabic',False])
name_in_scripts.append(['BEN','latin',False])
name_in_scripts.append(['NER','latin',False])
name_in_scripts.append(['NGA','latin',False])
name_in_scripts.append(['CMR','latin',False])
name_in_scripts.append(['TGO','latin',False])
name_in_scripts.append(['GHA','latin',False])
name_in_scripts.append(['CIV','latin',False])
name_in_scripts.append(['GIN','latin',False])
name_in_scripts.append(['GNB','latin',False])
name_in_scripts.append(['LBR','latin',False])
name_in_scripts.append(['SLE','latin',False])
name_in_scripts.append(['BFA','latin',False])
name_in_scripts.append(['CAF','latin',False])
name_in_scripts.append(['COG','latin',False])
name_in_scripts.append(['GAB','latin',False])
name_in_scripts.append(['GNQ','latin',False])
name_in_scripts.append(['ZMB','latin',False])
name_in_scripts.append(['MWI','latin',False])
name_in_scripts.append(['MOZ','latin',False])
name_in_scripts.append(['SWZ','latin',False])
name_in_scripts.append(['AGO','latin',False])
name_in_scripts.append(['BDI','latin',False])
name_in_scripts.append(['ISR','hebrew',True])
name_in_scripts.append(['LBN','arabic',False])
name_in_scripts.append(['MDG','latin',False])
name_in_scripts.append(['PSE','arabic',False])
name_in_scripts.append(['GMB','latin',False])
name_in_scripts.append(['TUN','latin',False])
name_in_scripts.append(['DZA','arabic',False])
name_in_scripts.append(['JOR','arabic',False])
name_in_scripts.append(['ARE','arabic',False])
name_in_scripts.append(['QAT','latin',False])
name_in_scripts.append(['KWT','arabic',False])
name_in_scripts.append(['IRQ','arabic',False])
name_in_scripts.append(['OMN','arabic',False])
name_in_scripts.append(['VUT','latin',False])
#name_in_scripts.append(['KHM','khmer',False])
name_in_scripts.append(['THA','thai',True])
#name_in_scripts.append(['LAO','lao',False])
#name_in_scripts.append(['MMR','burmese',False])
name_in_scripts.append(['VNM','latin',False])
#name_in_scripts.append(['PRK','hangul',False])
#name_in_scripts.append(['KOR','hangul',False])
#name_in_scripts.append(['MNG','mongolian',False])
name_in_scripts.append(['IND','hindi',True])
#name_in_scripts.append(['BGD','bengali',False])
#name_in_scripts.append(['BTN','tibetan',False])
#name_in_scripts.append(['NPL','devanagari',False])
#name_in_scripts.append(['PAK','urdu',False])
name_in_scripts.append(['AFG','arabic',False])
name_in_scripts.append(['TJK','cyrillic',False])
name_in_scripts.append(['KGZ','cyrillic',False])
name_in_scripts.append(['TKM','latin',False])
name_in_scripts.append(['IRN','persian',True])
name_in_scripts.append(['SYR','arabic',False])
#name_in_scripts.append(['ARM','armenian',False])
name_in_scripts.append(['SWE','latin',False])
name_in_scripts.append(['BLR','cyrillic',False])
name_in_scripts.append(['UKR','cyrillic',False])
name_in_scripts.append(['POL','latin',False])
name_in_scripts.append(['AUT','latin',False])
name_in_scripts.append(['HUN','latin',False])
name_in_scripts.append(['MDA','latin',False])
name_in_scripts.append(['ROU','latin',False])
name_in_scripts.append(['LTU','latin',False])
name_in_scripts.append(['LVA','latin',False])
name_in_scripts.append(['EST','latin',False])
name_in_scripts.append(['DEU','latin',True])
name_in_scripts.append(['BGR','cyrillic',False])
name_in_scripts.append(['GRC','greek',True])
name_in_scripts.append(['TUR','latin',False])
name_in_scripts.append(['ALB','latin',False])
name_in_scripts.append(['HRV','latin',False])
name_in_scripts.append(['CHE','latin',False])
name_in_scripts.append(['LUX','latin',False])
name_in_scripts.append(['BEL','latin',False])
name_in_scripts.append(['NLD','latin',False])
name_in_scripts.append(['PRT','latin',False])
name_in_scripts.append(['ESP','latin',False])
name_in_scripts.append(['IRL','latin',False])
name_in_scripts.append(['NCL','latin',False])
name_in_scripts.append(['SLB','latin',False])
name_in_scripts.append(['NZL','latin',False])
name_in_scripts.append(['AUS','latin',True])
name_in_scripts.append(['LKA','sinhala',True])
name_in_scripts.append(['CHN','chinese',True])
name_in_scripts.append(['TWN','chinese',False])
name_in_scripts.append(['ITA','latin',False])
name_in_scripts.append(['DNK','latin',False])
name_in_scripts.append(['GBR','latin',False])
name_in_scripts.append(['ISL','latin',False])
name_in_scripts.append(['AZE','latin',False])
#name_in_scripts.append(['GEO','georgian',False])
name_in_scripts.append(['PHL','latin',False])
name_in_scripts.append(['MYS','latin',False])
name_in_scripts.append(['BRN','latin',False])
name_in_scripts.append(['SVN','latin',False])
name_in_scripts.append(['FIN','latin',False])
name_in_scripts.append(['SVK','latin',False])
name_in_scripts.append(['CZE','latin',False])
#name_in_scripts.append(['ERI','geez',False])
name_in_scripts.append(['JPN','japanese',True])
name_in_scripts.append(['PRY','latin',False])
name_in_scripts.append(['YEM','arabic',False])
name_in_scripts.append(['SAU','arabic',False])
name_in_scripts.append(['ATA','none',False])
name_in_scripts.append(['CYP','greek',False])
name_in_scripts.append(['MAR','arabic',False])
name_in_scripts.append(['EGY','arabic',False])
name_in_scripts.append(['LBY','arabic',True])
name_in_scripts.append(['ETH','amharic',True])
name_in_scripts.append(['DJI','arabic',False])
name_in_scripts.append(['UGA','latin',False])
name_in_scripts.append(['RWA','latin',False])
name_in_scripts.append(['BIH','cyrillic',False])
name_in_scripts.append(['MKD','cyrillic',False])
name_in_scripts.append(['SRB','cyrillic',False])
name_in_scripts.append(['MNE','cyrillic',False])
name_in_scripts.append(['TTO','latin',False])
name_in_scripts.append(['SSD','latin',False])

colors_scripts = {
   'latin': 'red',
   'cyrillic': 'green',
   'chinese': 'yellow',
   'hebrew': 'blue',
   'arabic': 'orange',
   'japanese': 'purple',
   'tamil':'turquoise',
   'hindi': 'magenta',
   'thai': 'darkorchid',
   'persian': 'azure',
   'greek': 'salmon',
   'sinhala': 'teal',
   'amharic': 'palegreen'
}

fonts_scripts = {
   'latin': 'NotoSans-Regular.ttf',
   'cyrillic': 'NotoSans-Regular.ttf',
   'chinese': 'NotoSansTC-Regular.otf',
   'hebrew': 'NotoSansHebrew-Regular.ttf',
   'arabic': 'NotoSansArabic-Regular.ttf',
   'japanese': 'NotoSansJP-Regular.otf',
   'tamil': 'NotoSansTamil-VariableFont_wdth,wght.ttf',
   'thai': 'NotoSansThai-VariableFont_wdth,wght.ttf',
   'hindi': 'NotoSans-Regular.ttf',
   'persian': 'Yas.ttf', #https://fontlibrary.org/en/font/yas
   'greek': 'NotoSans-Regular.ttf',
   'sinhala': 'NotoSansSinhala-VariableFont_wdth,wght.ttf',
   'amharic': 'jiret.ttf', #https://www.lexilogos.com/keyboard/amharic.htm
   'none':'NotoSans-Regular.ttf'
}

transliteration_scripts = {
   'latin': latin,
   'cyrillic': russian,
   'chinese': chinese,
   'hebrew': hebrew,
   'arabic': arabic,
   'japanese': japanese,
   'tamil': tamil,
   'hindi': hindi,
   'thai' : thai,
   'persian': persian,
   'greek' : greek,
   'sinhala': sinhala,
   'amharic': amharic,
   'none': ''
}


df = pd.DataFrame(name_in_scripts, columns=['CODE','Script','ShowTransliteration'])

# Load the world.shp data 
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']
# merge with world.shp data with confirmed cases data and fatalities data
merge=pd.merge(world,df,on='CODE')

# merge with data which contains latitude and longitude
merge=merge.merge(pd.read_csv('countries_latitude_longitude.csv'),on='name')

merge.plot(scheme="quantiles",
           figsize=(25, 20),
           legend=True,color=merge['Script'].apply(lambda x: colors_scripts[x]))
plt.title('Your name all over the world',fontsize=25)

# add script names and transliterated script  

for i in range(len(merge)):
  fontpath = str('fonts/'+str(fonts_scripts[merge.Script[i]]))
  if merge.ShowTransliteration[i]==True:
    plt.text(float(merge.longitude[i]),float(merge.latitude[i]),"{}".format(merge.Script[i]).capitalize(),size=10,fontproperties=fm.FontProperties(fname='fonts/NotoSans-Regular.ttf'))
    plt.text(float(merge.longitude[i]),float(merge.latitude[i]+2),"{}".format(transliteration_scripts[merge.Script[i]]).capitalize(),size=15,fontproperties=fm.FontProperties(fname=fontpath))


plt.show()

st.pyplot(plt)