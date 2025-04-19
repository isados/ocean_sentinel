# %%
import pandas as pd
import streamlit as st
import plotly.express as px

# %%
st.set_page_config(page_title='Ocean Sentinel',
                page_icon=':bar_chart:',
                layout='wide')

st.title(':bar_chart: Ocean Sentinel')
st.markdown('##')
# %%

# --- SIDEBARD --- #
spots = ['Tubli', 'Hidd', 'Amwaj']
st.sidebar.header('Please filter here:')
city = st.sidebar.multiselect('High Impact Spots:',
                            options=spots,
                            default=spots)





# TOP KPIs
# total_sales = int(df_selection['Total'].sum())
average_rating = 7
# average_sales = int(df_selection['Total'].mean())


left_column, right_column = st.columns(2)

with left_column:
    st.subheader('Average NDVI')
    st.subheader(f'0.2')

with right_column:
    st.subheader('Aquatic Health')
    st.subheader(':star:' * int(average_rating) + str(average_rating))

# with right_column:
#     st.subheader('Average Sales for Transaction')
#     st.subheader(f'US $ {average_sales}')

# --- SALES BY PRODUCT LINE [BAR] --- #




# --- COMBINING ALL CHARTS ABOVE --- #
left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_product_sales, use_container_width=True)
# right_column.plotly_chart(fig_hourly_sales, use_container_width=True)
with left_column:
    st.image('original.png', width=400)

with right_column:
    st.image('ndvi.png', width=400)

# --- HIDE STREAMLIT STYLE --- #
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

