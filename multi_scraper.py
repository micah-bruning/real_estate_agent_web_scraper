from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from general_scraper import GeneralScraper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pandas as pd

class MultiPageScraper(GeneralScraper):
    def __init__(self, contact_section_path, 
                name_path, email_path, phone_path, 
                driver_url, title_path, agent_urls, agent_card):
        
        super().__init__(contact_section_path, 
                name_path, email_path, phone_path, driver_url)
        
        self.title_path = title_path
        self.agent_urls = agent_urls
        self.agent_card = agent_card

    def scrape_data(self):
        self.driver.get(self.driver_url)

        agent_pages = []
        name_list = []
        email_list = []
        phone_list = []

        agents_card = self.driver.find_elements_by_class_name(self.agent_card)

        for agent in agents_card:
            agent_pages.append(agent.find_element_by_xpath(self.agent_urls).get_attribute('href'))

        for page in agent_pages:
            self.driver.get(page)

            #Get section for name and contact info
            contact_section = self.driver.find_element_by_class_name(self.contact_section)
            main_title = self.driver.find_element_by_class_name(self.title_path)     

            #Implement try, except to account for missing data
            try:
                #Name is found from name path relative to where the main title section is
                name_list.append(main_title.find_element_by_xpath(self.name_path).text.title())
            except:
                name_list.append('N/A')
            try:
                phone_list.append(contact_section.find_element_by_xpath(self.phone_path).text)
            except:
                phone_list.append('N/A')
            try:
                email_list.append(contact_section.find_element_by_xpath(self.email_path).text)
            except:
                email_list.append('N/A')

        return name_list, email_list, phone_list

 

# print('Scraping...')
# driver = webdriver.Chrome()
# driver.implicitly_wait(5) 
# driver.get("https://www.bondnewyork.com/index.cfm?page=agents&state=search&term=&office=4")
# search_name = 'Upper East Side'


# agents_card = driver.find_elements_by_class_name('image-caption')

# name_list = []
# email_list = []
# phone_list = []

# for agent in agents_card:
#     agent_pages.append(agent.find_element_by_xpath(".//h3/a").get_attribute('href'))

# #Loop over every agents page to get their info 
# for page in agent_pages:
#     driver.get(page)
#     #Get section for name and contact info
#     contact_section = driver.find_element_by_class_name('agent-contact-links')
#     main_title = driver.find_element_by_class_name('main-title')

#     #There are no missing names on page but there are missing numbrs
#     name_list.append(main_title.find_element_by_xpath('h1').text.title())
#     try:
#         phone_list.append(contact_section.find_element_by_xpath(".//h4").text)
#     except:
#         phone_list.append('N/A')
#     try:
#         email_list.append(contact_section.find_element_by_xpath(".//h4[2]/a").text)
#     except:
#         email_list.append('N/A')


# #Make dataframe to export to excel
# agent_contacts = pd.DataFrame(
#     {'Name': name_list,
#      'Email': email_list,
#      'Cell Number': phone_list
#     })


# agent_contacts.to_csv(search_name + ' Bond Scrape.csv')

# print('Done')
