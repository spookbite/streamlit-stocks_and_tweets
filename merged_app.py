import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sn
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def get_data():
    return pd.read_csv(r"C:\Users\Palkit Lohia\Desktop\JSI stocks and tweets\tweets_and_stocks_left_merged_without_tweets_new.csv")

df = get_data()
st.title("Stocks Variation")
st.markdown("**Input Description**")
st.write("")

st.dataframe(df)
st.write("")
st.write("")

st.sidebar.title("Filter data")

industry = df['Industry'].unique()
industry_choice = st.sidebar.selectbox('Select the Industry:', industry)
df_new = df[df['Industry'] == industry_choice]
company = df_new["Company Name"].unique()
company_choice = st.sidebar.selectbox('Select the Company: ', company)
symbol_df = df_new[df_new['Company Name'] == company_choice]
#symbol = symbol_df['Symbol'].unique()
st.write(f'**Industry chosen :** *{industry_choice}* , **Company chosen :** *{company_choice}*')
st.write("")
st.write("")

df_industry = df[(df['Industry']==(industry_choice))].iloc[:]
df_company = df_industry[(df_industry['Company Name']==(company_choice))]

st.header("Analysis at the Industry Level")
industry_data_is_check = st.checkbox("Display the data of selected industries")
if industry_data_is_check:
	st.write(df_industry)
df_industry_new = df_industry[['Week Number','% Change in Stock Price','% Normal Stock Return','Weekly Positive Score','Weekly Negative Score','Weekly Neutral Score','Weekly Compound Score']]
df_industry_new = df_industry_new.set_index('Week Number')
correlation_industry = df_industry_new['% Change in Stock Price'].corr(df_industry_new['Weekly Compound Score']) 
st.write("")
st.write("")

st.markdown(f'**The correlation between % change in Stock Price and Normal Stock Return for __{industry_choice}__ is : **')
st.write(correlation_industry)
st.write("")
st.write("")
st.header("Analysis at the Company Level")

company_data_is_check = st.checkbox("Display the data of selected companies")
if company_data_is_check:
	st.write(df_company)
df_company_new = df_company[['Week Number','% Change in Stock Price','% Normal Stock Return','Weekly Positive Score','Weekly Negative Score','Weekly Neutral Score','Weekly Compound Score']]
df_company_new = df_company_new.set_index('Week Number')
correlation_company = df_company_new['% Change in Stock Price'].corr(df_company_new['Weekly Compound Score']) 
corrMatrix = df_company_new.corr()
st.write("")
st.write("")

st.markdown('** *The plot of % Change in Stock Price and % Normal Stock Return V/S Week Number, at the Company Level* **')
st.line_chart(df_company_new)
st.write("")
st.write("")
st.write(sn.heatmap(corrMatrix, annot = True))
st.pyplot()
st.write("")
st.write("")
st.markdown(f'**The correlation between % change in Stock Price and Weekly Sentiment Score for __{company_choice}__ is : **')
st.write(correlation_company)

