import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title = 'Car Price Pridiction')
st.title('CAR PRICE PRIDICTION')
brand_dic = {'Audi': 0,
 'BMW': 1,
 'Mercedes-Benz': 2,
 'Mitsubishi': 3,
 'Renault': 4,
 'Toyota': 5,
 'Volkswagen': 6}

body_dic = {'crossover': 0, 'hatch': 1, 'other': 2, 'sedan': 3, 'vagon': 4, 'van': 5}

engine_type_dic = {'Diesel': 0, 'Gas': 1, 'Other': 2, 'Petrol': 3}

registration_dic = {'no': 0, 'yes': 1}

model_dic = {'1 Series': 0,
 '100': 1,
 '11': 2,
 '116': 3,
 '118': 4,
 '120': 5,
 '19': 6,
 '190': 7,
 '200': 8,
 '210': 9,
 '220': 10,
 '230': 11,
 '25': 12,
 '250': 13,
 '300': 14,
 '316': 15,
 '318': 16,
 '320': 17,
 '323': 18,
 '325': 19,
 '328': 20,
 '330': 21,
 '335': 22,
 '4 Series Gran Coupe': 23,
 '428': 24,
 '4Runner': 25,
 '5 Series': 26,
 '5 Series GT': 27,
 '520': 28,
 '523': 29,
 '524': 30,
 '525': 31,
 '528': 32,
 '530': 33,
 '535': 34,
 '540': 35,
 '545': 36,
 '550': 37,
 '6 Series Gran Coupe': 38,
 '630': 39,
 '640': 40,
 '645': 41,
 '650': 42,
 '730': 43,
 '735': 44,
 '740': 45,
 '745': 46,
 '750': 47,
 '760': 48,
 '80': 49,
 '9': 50,
 '90': 51,
 'A 140': 52,
 'A 150': 53,
 'A 170': 54,
 'A 180': 55,
 'A1': 56,
 'A3': 57,
 'A4': 58,
 'A4 Allroad': 59,
 'A5': 60,
 'A6': 61,
 'A6 Allroad': 62,
 'A7': 63,
 'A8': 64,
 'ASX': 65,
 'Amarok': 66,
 'Auris': 67,
 'Avalon': 68,
 'Avensis': 69,
 'Aygo': 70,
 'B 170': 71,
 'B 180': 72,
 'B 200': 73,
 'Beetle': 74,
 'Bora': 75,
 'C-Class': 76,
 'CL 180': 77,
 'CL 500': 78,
 'CL 55 AMG': 79,
 'CL 550': 80,
 'CL 63 AMG': 81,
 'CLA 200': 82,
 'CLA 220': 83,
 'CLA-Class': 84,
 'CLC 180': 85,
 'CLC 200': 86,
 'CLK 200': 87,
 'CLK 220': 88,
 'CLK 230': 89,
 'CLK 240': 90,
 'CLK 280': 91,
 'CLK 320': 92,
 'CLK 430': 93,
 'CLS 350': 94,
 'CLS 400': 95,
 'CLS 500': 96,
 'CLS 63 AMG': 97,
 'Caddy': 98,
 'Camry': 99,
 'Captur': 100,
 'Caravelle': 101,
 'Carina': 102,
 'Carisma': 103,
 'Celica': 104,
 'Clio': 105,
 'Colt': 106,
 'Corolla': 107,
 'Corolla Verso': 108,
 'Cross Touran': 109,
 'Dokker': 110,
 'Duster': 111,
 'E-Class': 112,
 'Eclipse': 113,
 'Eos': 114,
 'Espace': 115,
 'FJ Cruiser': 116,
 'Fluence': 117,
 'Fortuner': 118,
 'G 320': 119,
 'G 350': 120,
 'G 500': 121,
 'G 55 AMG': 122,
 'G 63 AMG': 123,
 'GL 320': 124,
 'GL 350': 125,
 'GL 420': 126,
 'GL 450': 127,
 'GL 500': 128,
 'GL 550': 129,
 'GLC-Class': 130,
 'GLE-Class': 131,
 'GLK 220': 132,
 'GLK 300': 133,
 'GLS 350': 134,
 'GLS 400': 135,
 'Galant': 136,
 'Golf GTI': 137,
 'Golf II': 138,
 'Golf III': 139,
 'Golf IV': 140,
 'Golf Plus': 141,
 'Golf V': 142,
 'Golf VI': 143,
 'Golf VII': 144,
 'Golf Variant': 145,
 'Grand Scenic': 146,
 'Grandis': 147,
 'Hiace': 148,
 'Highlander': 149,
 'Hilux': 150,
 'I3': 151,
 'IQ': 152,
 'Jetta': 153,
 'Kangoo': 154,
 'Koleos': 155,
 'L 200': 156,
 'LT': 157,
 'Laguna': 158,
 'Lancer': 159,
 'Lancer Evolution': 160,
 'Lancer X': 161,
 'Lancer X Sportback': 162,
 'Land Cruiser 100': 163,
 'Land Cruiser 105': 164,
 'Land Cruiser 200': 165,
 'Land Cruiser 76': 166,
 'Land Cruiser 80': 167,
 'Land Cruiser Prado': 168,
 'Latitude': 169,
 'Logan': 170,
 'Lupo': 171,
 'M5': 172,
 'M6': 173,
 'MB': 174,
 'ML 250': 175,
 'ML 270': 176,
 'ML 280': 177,
 'ML 320': 178,
 'ML 350': 179,
 'ML 400': 180,
 'ML 430': 181,
 'ML 500': 182,
 'ML 550': 183,
 'ML 63 AMG': 184,
 'Master': 185,
 'Matrix': 186,
 'Megane': 187,
 'Modus': 188,
 'Multivan': 189,
 'New Beetle': 190,
 'Outlander': 191,
 'Outlander XL': 192,
 'Pajero': 193,
 'Pajero Pinin': 194,
 'Pajero Sport': 195,
 'Pajero Wagon': 196,
 'Passat B3': 197,
 'Passat B4': 198,
 'Passat B5': 199,
 'Passat B6': 200,
 'Passat B7': 201,
 'Passat B8': 202,
 'Passat CC': 203,
 'Phaeton': 204,
 'Pointer': 205,
 'Polo': 206,
 'Previa': 207,
 'Prius': 208,
 'Q3': 209,
 'Q5': 210,
 'Q7': 211,
 'R 320': 212,
 'R8': 213,
 'Rav 4': 214,
 'S 140': 215,
 'S 250': 216,
 'S 300': 217,
 'S 320': 218,
 'S 350': 219,
 'S 400': 220,
 'S 430': 221,
 'S 500': 222,
 'S 550': 223,
 'S 600': 224,
 'S 63 AMG': 225,
 'S 65 AMG': 226,
 'S4': 227,
 'S5': 228,
 'S8': 229,
 'SL 500 (550)': 230,
 'SL 55 AMG': 231,
 'SLK 200': 232,
 'SLK 350': 233,
 'Sandero': 234,
 'Sandero StepWay': 235,
 'Scenic': 236,
 'Scion': 237,
 'Scirocco': 238,
 'Sequoia': 239,
 'Sharan': 240,
 'Sienna': 241,
 'Smart': 242,
 'Space Star': 243,
 'Space Wagon': 244,
 'Sprinter 208': 245,
 'Sprinter 210': 246,
 'Sprinter 211': 247,
 'Sprinter 212': 248,
 'Sprinter 213': 249,
 'Sprinter 311': 250,
 'Sprinter 312': 251,
 'Sprinter 313': 252,
 'Sprinter 315': 253,
 'Sprinter 316': 254,
 'Sprinter 318': 255,
 'Sprinter 319': 256,
 'Symbol': 257,
 'Syncro': 258,
 'T3 (Transporter)': 259,
 'T4 (Transporter)': 260,
 'T4 (Transporter) ': 261,
 'T5 (Transporter)': 262,
 'T5 (Transporter) ': 263,
 'T6 (Transporter)': 264,
 'T6 (Transporter) ': 265,
 'TT': 266,
 'Tacoma': 267,
 'Tiguan': 268,
 'Touareg': 269,
 'Touran': 270,
 'Trafic': 271,
 'Tundra': 272,
 'Up': 273,
 'V 250': 274,
 'Vaneo': 275,
 'Vento': 276,
 'Venza': 277,
 'Viano': 278,
 'Virage': 279,
 'Vista': 280,
 'Vito': 281,
 'X1': 282,
 'X3': 283,
 'X5': 284,
 'X5 M': 285,
 'X6': 286,
 'X6 M': 287,
 'Yaris': 288,
 'Z3': 289,
 'Z4': 290}

brand_list = ['Volkswagen',
 'Mercedes-Benz',
 'BMW',
 'Toyota',
 'Renault',
 'Audi',
 'Mitsubishi']
body_list = ['crossover', 'hatch', 'other', 'sedan', 'vagon', 'van']
engine_type_list = ['Diesel', 'Gas', 'Other', 'Petrol']
registration_list = ['no', 'yes']

car=pd.read_csv('Car_cleaned_with_Model.csv')

def find_model(brand):
	model = car[car['Brand'] == brand]['Model'].unique()
	return list(model)

model_forest = joblib.load('rf1_base_rf.pkl')


col1, col2 = st.columns(2)

mileage = col1.number_input(label='Enter the how the car has driven, e.g: 200 mile', help='how much the cas driven?')

year =  col1.slider('Enter the year when the car was manufactured', 1980,2022,2005,help='The year when the car is manufactured.')

brand_inp = col1.selectbox(label='Enter the Brand of the car', options=brand_list, help='From which brand the car is belongs?') # passing the brand list
brand = brand_dic[brand_inp] 

engine_type = col1.selectbox(label='Enter the Engine type(fuel)', options=engine_type_list, help='In which gas the car is run?')
engine_type = engine_type_dic[engine_type]

engineV = col2.number_input(label='Enter the volume of the car engine. [e.g: 2.3]', max_value=6.5, help='Enter the volume of the engine.')
engineV = float(engineV)

body_type = col2.selectbox(label='Enter the body type of the car', options=body_list, help='select the body type of the car')
body_type = body_dic[body_type]

col2.text("")

if brand_inp == 'Audi':
    model_inp = col2.selectbox('Enter the Model for the Audi', options=find_model('Audi'))
    model = model_dic[model_inp]

elif brand_inp == 'Mitsubishi':
    model_inp = col2.selectbox('Enter the model for Misubishi', options=find_model('Mitsubishi'))
    model = model_dic[model_inp] 

elif brand_inp == 'Renault':   
    model_inp = col2.selectbox('Enter the model Renault', options=find_model('Renault'))
    model = model_dic[model_inp]

elif brand_inp == 'Toyota':
    model_inp = col2.selectbox('Enter the model for Toyota', options=find_model('Toyota'))
    model = model_dic[model_inp] 

elif brand_inp == 'BMW':
    model_inp = col2.selectbox('Enter the model for BWM', options=find_model('BMW'))
    model = model_dic[model_inp] 
    
elif brand_inp == 'Mercedes-Benz':
    model_inp = col2.selectbox('Enter the model for Mercedes Benz', options=find_model('Mercedes-Benz'))
    model = model_dic[model_inp] 

elif brand_inp == 'Volkswagen':
    model_inp = col2.selectbox('Enter the model for Volkswagen', options=find_model('Volkswagen'))
    model = model_dic[model_inp]



regis = col2.selectbox(label='The car have registration?', options=registration_list, help='the car have registration or not?')
regis = registration_dic[regis]

inp_array = np.array([[mileage, engineV, year, brand, body_type, engine_type, regis, model]])

predict = col1.button('Predict')


if predict: 
        pred = model_forest.predict(inp_array)
        if pred < 0:
            st.error('The input values must be irrelevant, try again by giving relevent information.')
        pred = round(float(pred),3)
        pred = pred*85
        write = 'The predicted price of the car is Rupees '+ str(pred)
        st.success(write)