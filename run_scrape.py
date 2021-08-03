from general_scraper import GeneralScraper
from multi_scraper import MultiPageScraper

def get_paths(brokerage, dictionary, multi_scraper):
    name_path = dictionary.get(brokerage).get('name_path')
    email_path = dictionary.get(brokerage).get('email_path')
    phone_path = dictionary.get(brokerage).get('phone_path')
    contact_path = dictionary.get(brokerage).get('contact_path')

    if multi_scraper:
        title_path = dictionary.get(brokerage).get('title_path')
        urls_path = dictionary.get(brokerage).get('agents_url_path')
        agent_card = dictionary.get(brokerage).get('agent_card')

        return contact_path, name_path, email_path, phone_path, title_path, urls_path, agent_card

    return contact_path, name_path, email_path, phone_path

if __name__ == '__main__':

    #This dict stores the relative paths for each website. Each agency has a different
    #name, email and phone number path within each sites' html
    xpath_dicts = {
        
        'Compass': {
            'contact_path': 'agentCard', 'name_path' : './/a/div', 
            'email_path': './/div/a', 'phone_path': './/div/a[2]'
            },

        'Nest Seekers': {
            'contact_path': 'agents_by_region__agent', 'name_path': ".//strong/a",
            'email_path': ".//div[1]/a[2]", 'phone_path': ".//div[2]/a"
            },

        'The Agency': {
            'contact_path': 'team-card', 'name_path': ".//a/div[2]/p",
            'email_path': ".//div[2]/p[4]", 'phone_path': ".//div[2]/p[3]"
            },

        'Bond': {
            'agent_card': 'image-caption', 
            'title_path': 'main-title', 'agents_url_path': ".//h3/a",
            'contact_path': 'agent-contact-links', 'name_path': "h1",
            'email_path': ".//h4[2]/a", 'phone_path': ".//h4"
        }

    }

    print('Starting web scraper...')

    #Get inputs on which brokerage and web page to scrape from
    brokerage = input("From the following agencies: " + str(xpath_dicts.keys()) + " -- which would you like to scrape from? ").title()
    url = input("Which webpage would you like to scrape from? Paste the link here: ")
    file_name = input("What do you want the excel file named?: ")

    if brokerage == 'Bond':
        contact_path, name_path, email_path, phone_path, title_path, urls_path, agent_card = get_paths(brokerage, xpath_dicts, multi_scraper=True)
        print('init multi scraper ')
        scraper = MultiPageScraper(contact_path, name_path, 
                    email_path, phone_path, url, title_path, urls_path, agent_card)
    
    else:
        #Get paths according to input using helper function
        contact_path, name_path, email_path, phone_path = get_paths(brokerage, xpath_dicts, multi_scraper=False)
        #Initialize scraper and pass in user inputs
        scraper = GeneralScraper(contact_path, name_path, email_path, phone_path, url)

    #Utilize scraper functions to commence scraping and download data
    name_list, email_list, phone_list = scraper.scrape_data()
    scraper.download_csv(df=scraper.get_dataframe(name_list, email_list, phone_list), file_name=file_name)




    
        
    

