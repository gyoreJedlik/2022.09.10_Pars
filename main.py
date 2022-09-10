from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def Teszt():
    lista = Select(driver.find_element(By.ID, "versenyek"))
    kep = driver.find_element(By.ID, "erem")
    for i in range(0,5):
        lista.select_by_index(i)
        ertek = int(lista.first_selected_option.get_attribute("value"))
        try:
            if ertek == 1:
                assert "gold" in kep.get_attribute("src")
            elif ertek == 2:
                assert "silver" in kep.get_attribute("src") 
            else:
                assert "bronze" in kep.get_attribute("src") 
            print("okés a teszti")
        except:
            print(" NEM okés a teszti")

        


driver = webdriver.Chrome()
url = "http://localhost/2022.09.10_Pars/pars.html"
driver.get(url)
driver.maximize_window()
Teszt()
