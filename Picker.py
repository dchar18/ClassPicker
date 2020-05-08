from selenium.webdriver.common.keys import Keys
from Login import username, password
from selenium import webdriver
from time import sleep
import sys


class Classes:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # go to main myuic page
        self.driver.get('https://my.uic.edu/uPortal/f/welcome/normal/render.uP')

        sleep(1)
        # click the "login" button on the top right
        self.driver.find_element_by_xpath('//*[@id="portalLoginLink"]').click()

        sleep(1)
        # choose which university
        self.driver.find_element_by_xpath('//*[@id="https://shibboleth.uic.edu/shibboleth"]').click()
        # confirm the choice
        self.driver.find_element_by_xpath('//*[@id="IdPList"]/input[1]').click()

        # enter username
        self.driver.find_element_by_xpath('//*[@id="UserID"]').send_keys(username)
        # enter password
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        # submit
        self.driver.find_element_by_xpath('//*[@id="disable-on-click"]').click()

    def registration_portal(self, term):
        # path = '//*[@id="Pluto_196_u29l1n904_47815_app"]/div/a'
        # choose the registration portal
        # self.driver.find_element_by_xpath(path).click()
        self.driver.get('https://banner.apps.uillinois.edu/StudentRegistrationSSB-FED/?mepCode=2UIC')
        sleep(1)
        # choose "Register for classes" - TODO
        self.driver.find_element_by_xpath('//*[@id="registerLink"]/span[1]').click()
        # confirm university again
        self.driver.find_element_by_xpath('//*[@id="IdPList"]/input[1]').click()

        sleep(1)
        # open drop down menu
        select_term_box = self.driver.find_element_by_xpath('//*[@id="s2id_txt_term"]/a')
        select_term_box.click()
        # type in term
        term_input = self.driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
        term_input.send_keys(term)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input').send_keys(Keys.ENTER)
        sleep(1)
        # continue
        self.driver.find_element_by_xpath('//*[@id="term-go"]').click()
        sleep(1)

    def find_class(self, subject, course):
        # type in subject
        subject_box = self.driver.find_element_by_xpath('//*[@id="s2id_autogen7"]')
        subject_box.send_keys(subject)
        sleep(1)
        subject_box.send_keys(Keys.ENTER)
        # type in course number
        self.driver.find_element_by_xpath('//*[@id="txt_courseNumber"]').send_keys(course)
        sleep(1)
        # search
        self.driver.find_element_by_xpath('//*[@id="search-go"]').click()


# default subject is Computer Science
subject = 'computer science'
# course number specified in as command line argument
course = sys.argv[1]
# check if subject is specified
if len(sys.argv) > 2:
    subject = sys.argv[2]
    # if there is another command line argument (multi-word subject)
    if len(sys.argv) > 3:
        for i in range (3, len(sys.argv)):
            # append it to the subject
            subject += (' ' + sys.argv[i])
# create instance of Classes
picker = Classes()
# start logging into the system
picker.login()
# wait for page to load
sleep(2)
# select the term
picker.registration_portal('fall 2020')
# find the course
picker.find_class(subject, course)
