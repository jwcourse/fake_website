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
#streamlit.write(df)

color_list = df[0].values.tolist()

option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

query = "SELECT direct_url, price, size_list, upsell_product_desc FROM catalog_for_website WHERE color_or_style = %s;"
my_cur.execute(query, (option,))
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
