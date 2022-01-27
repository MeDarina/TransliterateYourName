import streamlit as st
import pandas as pd
import numpy as np
from google.transliteration import transliterate_text, transliterate_word
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import datetime as dt
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable
# disable python warnings
import sys
import warnings

import folium
#from folium.features import DivIcon
import folium.plugins
from folium.features import *
from streamlit_folium import folium_static
from aksharamukha import transliterate
from transliterate import translit, get_available_language_codes

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

#google api
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
tigrinya = transliterate_text(user_input, lang_code='ti')
#Aksharamukha
if len(user_input)>0:
    mongolian= transliterate.process('autodetect', 'Mongolian', user_input)
    devanagari = transliterate.process('autodetect', 'Devanagari', user_input)
    khmer= transliterate.process('autodetect', 'Khmer', user_input)
    lao= transliterate.process('autodetect', 'Lao', user_input)
    burmese= transliterate.process('autodetect', 'Burmese', user_input)
    bengali= transliterate.process('autodetect', 'Bengali', user_input)
    tibetan= transliterate.process('autodetect', 'Tibetan', user_input)
    urdu= transliterate.process('autodetect', 'Urdu', user_input)
else:
    mongolian= " "
    devanagari = " "
    khmer= " "
    lao= " "
    burmese= " "
    bengali= " "
    tibetan= " "
    urdu= " "

#transliterate 
georgian = translit(user_input, 'ka')
armenian = translit(user_input, 'hy')

unknown = 'unknown'

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
name_in_scripts.append(['KHM','khmer',True])
name_in_scripts.append(['THA','thai',True])
name_in_scripts.append(['LAO','lao',True])
name_in_scripts.append(['MMR','burmese',True])
name_in_scripts.append(['VNM','latin',False])
#name_in_scripts.append(['PRK','hangul',False])
#name_in_scripts.append(['KOR','hangul',False])
name_in_scripts.append(['MNG','mongolian',True])
name_in_scripts.append(['IND','hindi',True])
name_in_scripts.append(['BGD','bengali',True])
name_in_scripts.append(['BTN','tibetan',True])
name_in_scripts.append(['NPL','devanagari',True])
name_in_scripts.append(['PAK','urdu',True])
name_in_scripts.append(['AFG','arabic',False])
name_in_scripts.append(['TJK','cyrillic',False])
name_in_scripts.append(['KGZ','cyrillic',False])
name_in_scripts.append(['TKM','latin',False])
name_in_scripts.append(['IRN','persian',True])
name_in_scripts.append(['SYR','arabic',False])
name_in_scripts.append(['ARM','armenian',True])
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
name_in_scripts.append(['GEO','georgian',True])
name_in_scripts.append(['PHL','latin',False])
name_in_scripts.append(['MYS','latin',False])
name_in_scripts.append(['BRN','latin',False])
name_in_scripts.append(['SVN','latin',False])
name_in_scripts.append(['FIN','latin',False])
name_in_scripts.append(['SVK','latin',False])
name_in_scripts.append(['CZE','latin',False])
name_in_scripts.append(['ERI','tigrinya',True])
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
name_in_scripts.append(['FRA','latin',False])
name_in_scripts.append(['NOR','latin',False])
name_in_scripts.append(['GL','latin',False])
name_in_scripts.append(['RKS','latin',False])

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
   'amharic': 'palegreen',
   'tigrinya': 'cornflowerblue',
   'armenian': 'springgreen',
   'georgian': 'plum',
   'mongolian': 'deeppink',
   'devanagari': 'olive',
   'khmer': 'silver',
   'lao': 'slateblue',
   'burmese': 'darkmagenta',
   'bengali': 'grey',
   'tibetan': 'rosybrown',
   'urdu': 'darkgreen',
   'unknown': 'black'
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
   'amharic': 'jiret.ttf', #https://www.lexilogos.com/keyboard/amharic.htm,
   'tigrinya': 'NotoSans-Regular.ttf',
   'armenian': 'NotoSans-Regular.ttf',
   'georgian': 'NotoSans-Regular.ttf',
   'mongolian':'NotoSans-Regular.ttf',
   'devanagari': 'NotoSans-Regular.ttf',
   'khmer': 'NotoSans-Regular.ttf',
   'lao': 'NotoSans-Regular.ttf',
   'burmese': 'NotoSans-Regular.ttf',
   'unknown':'NotoSans-Regular.ttf',
   'bengali': 'NotoSans-Regular.ttf',
   'tibetan': 'NotoSans-Regular.ttf',
   'urdu': 'NotoSans-Regular.ttf',
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
   'tigrinya': tigrinya,
   'armenian': armenian,
   'georgian': georgian,
   'mongolian': mongolian,
   'devanagari': devanagari,
   'khmer':khmer,
   'lao': lao,
   'burmese': burmese,
   'bengali': bengali,
   'tibetan': tibetan,
   'urdu': urdu,
   'unknown': unknown
}

df = pd.DataFrame(name_in_scripts, columns=['CODE','Script','ShowTransliteration'])

# Load the world.shp data 
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.loc[world['name'] == 'France', 'iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway', 'iso_a3'] = 'NOR' #added Norway to countries_latitude_longitude.csv
world.loc[world['name'] == 'Greenland', 'iso_a3'] = 'GL' #added Greenland to countries_latitude_longitude.csv
world.loc[world['name'] == 'Somaliland', 'iso_a3'] = 'SOM'
world.loc[world['name'] == 'N. Cyprus','iso_a3'] = 'NCY'
world.loc[world['name'] == 'Kosovo', 'iso_a3'] = 'RKS'
world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']
# merge with world.shp data with confirmed cases data and fatalities data
merge1=pd.merge(world,df,on='CODE')

# merge with country script data

Alphabet_URL = 'https://www.key-shortcut.com/en/writing-systems/world-map-of-alphabets-scripts'
alpha_df = pd.read_html(Alphabet_URL)[2] # set header with row #0
alpha_df.drop(['Official language'], axis=1)

#merge on "Country"

def displayAllScripts(script_list):
    scripts = list(script_list.split(","))
    return scripts

def displayAllTransliterations(script_list):
    scripts = list(script_list.split(", "))
    transliterations = []
    for script in scripts:
        if script.lower() in transliteration_scripts:
            transliterations.append(transliteration_scripts[script.lower()])
    return transliterations

alpha_df['Writing system2'] = alpha_df['Writing system'].apply(displayAllScripts)
alpha_df['Transliteration'] = alpha_df['Writing system'].apply(displayAllTransliterations)


merge = pd.merge(merge1, alpha_df, left_on='name', right_on='Country', how='left')

# merge with data which contains latitude and longitude
merge=merge.merge(pd.read_csv('countries_improved.csv'),on='name')

#Fill possible voids
merge["Script"][merge["Script"] == "none"] = 'unknown'


#Display as folio map



#create map
m = merge.explore(
    legend=False,
    tiles='StamenWatercolor', 
    color=merge['Script'].apply(lambda x: colors_scripts[x]),
    tooltip=['name','Script','Writing system','Transliteration'])
    #max_bounds=True,
    #width=500)
    #height=1000,
    #location=[13.406,170.110],
    #zoom_start=1)

#create elements
class DivIcon(MacroElement):
    def __init__(self, html='', size=(30,30), anchor=(0,0), style=''):
    #def __init__(self, html='', style=''):
        """TODO : docstring here"""
        super(DivIcon, self).__init__()
        self._name = 'DivIcon'
        self.size = size
        self.anchor = anchor
        self.html = html
        self.style = style

        self._template = Template(u"""
            {% macro header(this, kwargs) %}
              <style>
                .{{this.get_name()}} {
                    {{this.style}}
                    }
              </style>
            {% endmacro %}
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.divIcon({
                    className: '{{this.get_name()}}',
                    iconSize: [{{ this.size[0] }},{{ this.size[1] }}],
                    iconAnchor: [{{ this.anchor[0] }},{{ this.anchor[1] }}],
                    html : "{{this.html}}",
                    });
                {{this._parent.get_name()}}.setIcon({{this.get_name()}});
            {% endmacro %}
            """)

#put in Scripts
for i in range(len(merge)):
  fontpath = str('fonts/'+str(fonts_scripts[merge.Script[i]]))
  if merge.ShowTransliteration[i]==True:
      folium.map.Marker([float(merge.latitude[i]), float(merge.longitude[i])],icon=DivIcon(
        size=(150,36),
        anchor=(150,12),
        html=transliteration_scripts[merge.Script[i]].capitalize(),
        style="""
            font-size:14px;
            background-color: transparent;
            border-color: transparent;
            text-align: right;
            """
        )
    ).add_to(m)


      folium.map.Marker(
    [float(merge.latitude[i]), float(merge.longitude[i])],
    icon=DivIcon(
        size=(150,36),
        anchor=(150,0),
        html=merge.Script[i].capitalize(),
        style="""
            font-size:10px;
            background-color: transparent;
            border-color: transparent;
            text-align: right;
            """
        )
    ).add_to(m)

folium_static(m)
