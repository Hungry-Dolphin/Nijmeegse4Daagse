from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import uniform
from time import sleep
import threading
import json


class Worker(threading.Thread):
    def __init__(self, identity:int, url, tickets):
        super().__init__()

        self.identity = identity
        self.url = url
        self.tickets = tickets

        with open('config.json', 'r') as f:
            config = json.load(f)

        options = Options()
        options.add_argument(f"--proxy-server={config['HOSTNAME']}:{int(config['PORT'])+identity}")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument(f'user-agent={user_agent}')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def found_tickets(self):
        self.tickets.set()
        input()

    def sanity_check(self):
        # Sanity check for as long as im not sure that the ticket click function works
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # The amount of tickets available is in a <span class="sc-gEvEer cbueMy">0 tickets available</span>
        tickets_free = soup.find('span', {'class': 'sc-gEvEer cbueMy'}).get_text()

        return True if tickets_free == "0 tickets available" else False

    def run(self):
        print(f"Thread {self.identity} starting")
        # Open the page
        self.driver.get(f'{self.url}')

        while not self.tickets.is_set():

            try:
                # Wait for the page to load in
                WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'ticket')]")))

                # Click on the "Tickets kopen" button if it is there. The wait is a bit random about it so we kinda hide the fact we are automated
                free_tickets = WebDriverWait(self.driver, uniform(5.5, 6)).until(
                    ec.element_to_be_clickable((By.XPATH, "//*[self::a or self::button][contains(text(), 'Ticket')]")))

                # We found tickets lets quickly press the button
                free_tickets.click()
                self.found_tickets()

            except TimeoutException:
                # This means no tickets but just to be sure we run the sanity check
                if not self.sanity_check():
                    self.found_tickets()

                # There are really no tickets, lets refresh and try again
                sleep(3.5)  # A bit of hardcoded sleep since I was getting throttled in the long run
                self.driver.refresh()

        # Some other thread found the tickets, close this one to reduce confusion
        self.driver.close()

