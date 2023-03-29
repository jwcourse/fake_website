import streamlit
import pandas as pd
#import requests
import snowflake.connector
# urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select color_or_style FROM ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
my_catalog = my_cur.fetchall() 


df = pd.DataFrame(my_catalog)


color_list = df[0].values.tolist()

option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'


my_cur.execute("select direct_url, price, size_list, upsell_product_desc from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website where color_or_style = '" + option + "';")

df2 = my_cur.fetchone()

#streamlit.write(df2)
streamlit.image(
df2[0],
width=400,
caption= product_caption)
