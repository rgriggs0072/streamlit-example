import pandas as pd
import streamlit as st

st.header('Welcome to Delta Pacifics Spreadsheet Formatter')

import pandas as pd
import streamlit as st

# Define the function
def transform_data():
    # Read the data from the spreadsheet
    #df = pd.read_excel('C:/Users/rgrig/Desktop/Randy_Spreadsheets/Distribution_Grid/Distribution_Grids/SAVEMART_DISTRIBUTION_GRID_RGSR.xlsx')
    df = pd.read_excel('https://github.com/rgriggs0072/streamlit-example/blob/master/SAVEMART_DISTRIBUTION_GRID_RGSR.csv')
    # Get the store IDs from the first row
    store_ids = [x for x in df.columns[7:]]

    # Melt the data so that store IDs become a separate column
    df_melted = pd.melt(df, id_vars=df.columns[:7], value_vars=store_ids, var_name='store_id', value_name='Yes/No')

    # Replace 1 with a green checkmark and NaN with a red X
    df_melted['Yes/No'] = df_melted['Yes/No'].apply(lambda x: 'Yes' if x == 1 else ('No' if pd.isna(x) else '*'))

    # Write the melted data to a CSV file
    df_melted.to_csv('C:/Users/rgrig/Desktop/Randy_Spreadsheets/Distribution_Grid/Distribution_Grids/TRANSPOSED/SAVEMART_DISTRO_GRID_RGSR.csv', index=False, encoding='utf-8')

    # Display the transformed data in Streamlit
    st.write(df_melted)

# Create a button that runs the function when clicked
if st.button('Transform Data'):
    transform_data()



