import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor  
import pickle 

st.write('this is a real app')


st.title("Richter's Predictor")

st.write("## This app is a proto-type of what would be used to input in the system")


geo_level_1_id = st.number_input("geo_level_1_id", min_value=1, max_value=30)

geo_level_2_id = st.number_input("geo_level_2_id", min_value=1, max_value=1050)

land_surface_condition = st.selectbox("land_surface_condition", options=['t' , 'n', 'o'],
                        )

foundation_type = st.selectbox("foundation_type",
                                options=['r' , 'w', 'u', 'i', 'h'])


roof_type = st.selectbox("roof_type",
                       options=['n' , 'q', 'x'])

ground_floor_type = st.selectbox("ground_floor_type ", options=['f' , 'x', 'v', 'z', 'm'])

has_superstructure_adobe_mud = st.selectbox("has_superstructure_adobe_mud ",
                          options= [0,1])

has_superstructure_mud_mortar_stone = st.selectbox("has_superstructure_mud_mortar_stone", options=[0,1])


has_superstructure_stone_flag = st.selectbox("has_superstructure_stone_flag", options=[0,1])


has_superstructure_cement_mortar_stone = st.selectbox("has_superstructure_cement_mortar_stone", options=[0,1])

has_superstructure_mud_mortar_brick = st.selectbox("has_superstructure_mud_mortar_brick?  ", options=[0,1])

has_superstructure_cement_mortar_brick = st.selectbox("has_superstructure_cement_mortar_brick", options=[0,1])

has_superstructure_timber = st.selectbox("has_superstructure_timber", options=[0,1])

has_superstructure_bamboo = st.selectbox("has_superstructure_bamboo", options=[0,1])

has_superstructure_rc_non_engineered = st.selectbox("has_superstructure_rc_non_engineered", options=[0,1])

has_superstructure_rc_engineered = st.selectbox("has_superstructure_rc_engineered", options=[0,1])

has_superstructure_other = st.selectbox("has_superstructure_other", options=[0,1])


f = open('final_model.sav', 'rb')
model = pickle.load(f)
f.close()

#Function here
def information_gather(geo_level_1_id, geo_level_2_id, land_surface_condition,
       foundation_type, roof_type, ground_floor_type,
       has_superstructure_adobe_mud, has_superstructure_mud_mortar_stone,
       has_superstructure_stone_flag,
       has_superstructure_cement_mortar_stone,
       has_superstructure_mud_mortar_brick,
       has_superstructure_cement_mortar_brick, has_superstructure_timber,
       has_superstructure_bamboo, has_superstructure_rc_non_engineered,
       has_superstructure_rc_engineered, has_superstructure_other ):
    info = {'geo_level_1_id': [geo_level_1_id],
            'geo_level_2_id': [ geo_level_2_id],
            'land_surface_condition': [land_surface_condition],
            'foundation_type': [foundation_type],
            'roof_type': [roof_type],
            'ground_floor_type': [ground_floor_type],
            'has_superstructure_adobe_mud': [has_superstructure_adobe_mud],
            'has_superstructure_mud_mortar_stone': [has_superstructure_mud_mortar_stone],
            'has_superstructure_stone_flag': [has_superstructure_stone_flag],
            'has_superstructure_cement_mortar_stone': [has_superstructure_cement_mortar_stone],
            'has_superstructure_mud_mortar_brick': [has_superstructure_mud_mortar_brick],
            'has_superstructure_cement_mortar_brick': [has_superstructure_cement_mortar_brick],
            'has_superstructure_timber': [has_superstructure_timber],
            'has_superstructure_bamboo': [has_superstructure_bamboo],
            'has_superstructure_rc_non_engineered': [has_superstructure_rc_non_engineered],
            'has_superstructure_rc_engineered': [has_superstructure_rc_engineered],
            'has_superstructure_other': [has_superstructure_other]
            }

    df = pd.DataFrame.from_dict(info)
    
    return model.predict(df)


run = st.button("click to run")

if run:
    results = information_gather(geo_level_1_id, geo_level_2_id, land_surface_condition,
       foundation_type, roof_type, ground_floor_type,
       has_superstructure_adobe_mud, has_superstructure_mud_mortar_stone,
       has_superstructure_stone_flag,
       has_superstructure_cement_mortar_stone,
       has_superstructure_mud_mortar_brick,
       has_superstructure_cement_mortar_brick, has_superstructure_timber,
       has_superstructure_bamboo, has_superstructure_rc_non_engineered,
       has_superstructure_rc_engineered, has_superstructure_other)
    st.write(f'Damage Grade {results}')