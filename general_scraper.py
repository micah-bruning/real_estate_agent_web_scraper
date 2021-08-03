from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os

class GeneralScraper:

    def __init__(self, contact_section_path, 
                name_path, email_path, phone_path, driver_url):

        self.contact_section = contact_section_path
        self.name_path = name_path
        self.email_path = email_path
        self.phone_path = phone_path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver_url = driver_url

    def scrape_data(self):
        self.driver.get(self.driver_url)
        #Get main section for their contact info 
        agents_list = self.driver.find_elements_by_class_name(self.contact_section)

        #Lists to return data for
        name_list = []
        email_list = []
        phone_list = []
        #Loop over section and accces name, email and phone by relative xpath
        for agent in agents_list:
            try:
                name = agent.find_element_by_xpath(self.name_path).text
                name_list.append(name)
            except:
                name_list.append('N/A')
            try:
                email = agent.find_element_by_xpath(self.email_path).text
                email_list.append(email)
            except:
                email_list.append('N/A')
            try:
                number = agent.find_element_by_xpath(self.phone_path).text
                phone_list.append(number)
            except:
                phone_list.append('N/A')

        return name_list, email_list, phone_list

    def get_dataframe(self, name_list, email_list, phone_list):
        return pd.DataFrame({
                'Name': name_list,
                'Email': email_list, 
                'Cell Number': phone_list})

    def download_csv(self, df, file_name):
        cwd = os.getcwd()
        print('downloading excel file within this directory: ' + cwd)
        df.to_csv(file_name + '.csv')

    





    

         
        

