import streamlit
#import pandas as pd
#import requests
import snowflake.connector
# urllib.error import URLError

def run_a_query(Query):
  with my_cnx.cursor() as my_cur:
   my_cur.execute(Query)
   return my_cur.fetchall()

Beta = run_a_query("select color_or_style from catalog_for_website")
df = pandas.DataFrame(Beta)
streamlit.write(df)



