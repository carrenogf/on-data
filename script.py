from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import streamlit as st
import time
with st.sidebar.form(key='my_form'):
    st.write("""
        ## Descargar data ON
        """)
    symbol = st.text_input('Ingresa el ticker por favor:')
    submit_button = st.form_submit_button(label='Procesar 👈')
    st.write("Creado por Francisco Carreño")

if symbol:

    url = "https://bonds.mercapabbaco.com/bort/bondAnalysis?name="
    timeout = 20

    st.title("Test Selenium")

    firefoxOptions = Options()
    #firefoxOptions.add_argument("--headless")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(
        options=firefoxOptions,
        service=service,
    )
    #abrir la pagina de mae buscando el ticker de la on
    driver.get(url+symbol)
    # detectar si no está logueado
    try:
        mail = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "username")))
        mail.send_keys("francisko.ca93@gmail.com") #ocultar en entorno
        pwd = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "password")))
        pwd.send_keys("Cabina123") #ocultar en entorno
        pwd.send_keys(Keys.ENTER)
        
    except:
        st.write("No se puedo loguear")
    try:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        paneles = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "panel-body")))
        i=0
        for panel in paneles:
            if i==0 or i==3:
                st.markdown(panel.get_attribute('outerHTML'), unsafe_allow_html=True)
            i+=1
    except:
        st.write("No se pudo obtener panel")
    driver.close()
    