import streamlit as st
import sqlite3
import re
import os


st.set_page_config(layout="wide")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)





#path = "C:/Users/jr/OneDrive - EMD International A S/Python Projects/jr_projects/energygame/"
# path = "c:/Users/sba/OneDrive - EMD International A S/energygame - Jonathan Refsgaards filer/"
# conn = sqlite3.connect(path + "forslag.db")
# conn.execute("DROP TABLE IF EXISTS SETTINGS")
# conn.execute("CREATE TABLE SETTINGS (NAME CHAR(50), EMAIL CHAR(50), VARMEPUMPE, ELKEDEL, AKKU)")
# conn.commit()
# conn.close()

vp = st.slider("Varmepumpe", min_value=0.0, max_value=5.0, step=0.01)
ek = st.slider("Elkedel", min_value=0.0, max_value=5.0, step=0.01)
ak = st.slider("Akkumuleringstank", min_value=0.0, max_value=5.0, step=0.01)

cost = vp * 1_000_000 + ek * 200_000 + ak * 40_000

# email checker
def is_valid_email(em):
    # Regular expression for a valid email address
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match function to match the email pattern
    if re.match(email_pattern, em):
        return True
    else:
        return False


if cost > 2_000_000:
    st.markdown("Investering må ikke være større end 2.000.000 DKK")
else:
    st.markdown(str(cost))
    navn = st.text_input("Navn")
    email = st.text_input("E-mail")
    if  navn != "" and email != "":
        if is_valid_email(email):
            send = st.button("Send forslag")
            if send:
                conn = sqlite3.connect("forslag.db")
                # Define the SQL query with placeholders for data
                query = "INSERT INTO SETTINGS (NAME, EMAIL, VARMEPUMPE, ELKEDEL, AKKU) VALUES (?, ?, ?, ?, ?)"
                conn.execute(query, (navn, email, vp, ek, ak))
                conn.commit()
                conn.close()
                st.markdown("Forslag indsendt")
        else:
            st.markdown("E-mail ser ikke ud til at være skrevet korrekt?")







