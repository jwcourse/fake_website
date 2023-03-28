import streamlit
import pandas as pd
#import requests
import snowflake.connector
# urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM ZENAS_ATHLEISURE_DB.PRODUCTS.SWEATSUIT_SIZES")
my_catalog = my_cur.fetchall() 


df = pd.DataFrame(my_catalog)
streamlit.write(df)



