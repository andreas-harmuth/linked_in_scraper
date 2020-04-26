"""

    LinkedIn Scraper can either find information about a person or a company

    # TODO-list:

"""
import platform
import traceback
import sys, os

from selenium import webdriver
import time
import re
from googleapiclient.discovery import build

from lib.Utils import Utils

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

API_KEY = "AIzaSyAKwM9Jvl5dKcNQUPJJD_MrSDqRKeY6_wY"
LINKEDIN_CSE_ID = '009280166250991606564:d24xiqelgt4'


class LinkedIn:

    def __init__(self, email, password, timeout=10, speed=1):
        """
        :param email: user email
        :param password: user password
        :param timeout: if anything fails, this is the timeout (we only try something for x sec)
        :param speed: the higher the slower - ironically
        """

        self.email = email,
        self.password = password
        self.speed = speed
        self.timeout = timeout

        self.data = {
            'profiles': [],
            'errors': []
        }

        # Get the right server
        print(os.path.join(CURRENT_DIR, 'drivers'))
        if platform.system() == "Windows":
            self.driver = webdriver.Firefox(
                executable_path=os.path.join(CURRENT_DIR, 'drivers', 'windows_geckodriver.exe'))
        else:
            self.driver = webdriver.Firefox(executable_path=os.path.join(CURRENT_DIR, 'drivers', 'mac_geckodriver'))

    @staticmethod
    def find_url_from_google(name, profile_terms):
        """
        :param name: Full name of person
        :type name: str
        :param profile_terms: A list of words to help search for the person on google. A term could be CEO or a company name --> Max 6 entries
        :type profile_terms: list of str
        :return: Url if found
        :rtype: str | None
        """
        res = build("customsearch", "v1", developerKey=API_KEY).cse().list(q=name + ' & ('
                                                                                     + (" OR ".join(profile_terms))
                                                                                     + ')',
                                                                                   cx=LINKEDIN_CSE_ID, num=10).execute()

        # We don't "expect" a username
        username = None
        if int(res['searchInformation']['totalResults']) > 0:
            # Try and find the username
            for result in res['items']:

                # Check against link format and name
                if re.match('^https://[a-z]{2,3}\.linkedin\.com/in/.*$', result['link']):
                    # Flag var
                    name_match = True
                    # TODO
                    if "hcard" in result['pagemap'] and "fn" in result['pagemap']["hcard"][-1]:
                        name_match = Utils.name_check(name, result['pagemap']['hcard'][-1]["fn"])

                    if name_match:
                        string_split = re.split('^https://[a-z]{2,3}\.linkedin\.com/in/', result['link'])[1]
                        username = string_split.split('/')[
                            0]  # Removes something like /de (https://dk.linkedin.com/in/andreas-harmuth-a522aa68/de)
                        break
        return "https://www.linkedin.com/in/" + username if username is not None else None

    def __get_class_element_if_exists(self, class_name, sub_ele=None):
        """ Checks if an element of a class exist. If it does then return it otherwise return None. Can be done on a sub
        element.

        :param class_name:
        :param sub_ele:
        :return None or Driver element - of the class:
        """
        driver = self.driver if sub_ele is None else sub_ele

        ele_list = driver.find_elements_by_class_name(class_name)
        if len(ele_list) > 0:
            return ele_list[0]
        return None

    def __get_tag_element_if_exists(self, tag_name, sub_ele=None):
        """Checks if an element of a tag exist. If it does then return it otherwise return None. Can be done on a sub
        element.

        :param tag_name:
        :param sub_ele:
        :return:
        """
        driver = self.driver if sub_ele is None else sub_ele

        ele_list = driver.find_elements_by_tag_name(tag_name)
        if len(ele_list) > 0:
            return ele_list[0]
        return None

    def __does_id_element_exists(self, id_name):
        """ Checks if an element of an id exist. If it does then return it otherwise return None

        :param class_name: 
        :return None or Driver element - of the id: 
        """
        ele_list = self.driver.find_elements_by_id(id_name)
        if len(ele_list) > 0:
            return ele_list[0]
        return None

    def __extract_endorsements(self, skill_ele):
        """ Check if there are any endorsements, if there are, then See X endorsements for Start-ups --> X else return 0

        :param endorsements_string:
        :return number of endorsements (int):
        """
        for ele in skill_ele.find_elements_by_class_name('visually-hidden'):
            if re.match("See [0-9]+ endorsement[s]? for .*", ele.get_attribute('innerHTML')):
                return ele.get_attribute('innerHTML').split("See ")[1].split(" ")[0]
        return 0

    def __scroll_and_load(self, jmp=100, total_scroll=4000, _from=0):
        """ Scrolls down on the page. It scrolls from pixel _from and scrolls a total of total_scroll

        :param jmp:
        :param total_scroll:
        :param _from:
        """

        for i in range(_from, total_scroll + _from, jmp):
            self.driver.execute_script(
                "window.scrollTo(0," + str(i) + ");")  # Get all the links - loads on scroll
            time.sleep((1 / 100) * self.speed)

    def force_login(self):
        """ Logs into LinkedIn on the user specified in the init of the class

        """
        self.driver.get("https://www.linkedin.com/uas/login?_l=en")
        un = None
        pw = None
        start = time.time()
        # Click both elements as soon as the appear
        while time.time() < start + self.timeout:
            try:
                un = self.driver.find_element_by_id('username')
                pw = self.driver.find_element_by_id('password')
                break
            except Exception as e:
                pass

        if pw is not None and un is not None:
            un.send_keys(self.email)
            pw.click()  # As this is a password, you have to click it!
            pw.send_keys(self.password)

            time.sleep(0.2 * self.speed)
            self.driver.find_element_by_class_name('btn__primary--large').click()
        else:

            raise ValueError('Login error. Login elements was not found')

    def __get_connected_links(self, url, get_links=True, ):
        """ Get list of connects (as links)

        :param self.driver:
        :param url:
        :param slower:
        :return list of links:
        """
        connections = []
        connections_no = 0
        page_index = 1
        url_page = url + "%3Fpage&page={0}"
        start_big = time.time()
        while time.time() < start_big + self.timeout:

            self.driver.get(url_page.format(page_index))
            start_big = time.time()
            # Check if user has been logged out
            if "authwall" in self.driver.current_url:
                self.force_login()
                self.driver.get(url_page.format(page_index))
                start_big = time.time()

            if connections_no == 0:
                total_raw = self.driver.find_element_by_class_name('search-results__total').get_attribute('innerHTML')
                connections_no = total_raw.split("Showing ")[1].split("results")[0].strip()
                # If we only want number of connections
                if not get_links:
                    return [], connections_no

            # Load page
            self.__scroll_and_load(total_scroll=3000)

            start = time.time()

            while time.time() < start + self.timeout:
                # Get element of button paginator
                # TODO: Test what if you only have like 2 connections?
                scroll_full = self.driver.find_elements_by_class_name('results-paginator')
                if len(scroll_full) > 0: break

            # Get connections
            for ele in self.driver.find_elements_by_class_name('search-result__wrapper'):
                connections.append("https://www.linkedin.com/" + ele.find_element_by_class_name(
                    'search-result__result-link').get_attribute('href'))

            # Keep going for all pages
            if len(self.driver.find_elements_by_class_name('next')) > 0:
                page_index += 1

            else:
                # If there isn't a next button (anymore)
                break
        return connections, connections_no

    def __extract_work_experience(self, div, single_experience=False):
        """ Extract the work experience from a div

        :param div:
        :param single_experience:
        :return {
            "dateFrom": str,
            "dateTo": str
            "employment": str
            "area": str
            }

        """
        emp = div.find_element_by_tag_name('h3')
        duration_ele = self.__get_class_element_if_exists('pv-entity__date-range')
        if duration_ele is None:
            duration = []
        else:
            duration = div.find_element_by_class_name('pv-entity__date-range').find_elements_by_tag_name('span')[
                1].get_attribute('innerHTML').split("–")  # TODO Replace with \U+2013 (dash unicode)

        return {
            "dateFrom": duration[0].strip() if len(duration) > 0 else None,
            "dateTo": duration[1].strip() if len(duration) > 1 else None,
            "employment": emp.get_attribute('innerHTML') if single_experience else
            emp.find_elements_by_tag_name('span')[1].get_attribute('innerHTML'),
            # Check if this exists by calling all elements of this type; if the length of the list is 0, then it doesn't!
            "area": div.find_element_by_class_name('pv-entity__location').find_elements_by_tag_name('span')[
                1].get_attribute('innerHTML') if len(
                div.find_elements_by_class_name('pv-entity__location')) > 0 else None
        }

    def __show_more_accomplishment(self, accomplishment_ele):
        """ Recursively clicks the "Show more" button in accomplishments if it is present

        :param accomplishment_ele:
        """

        time.sleep(0.5 * self.speed)
        for button in accomplishment_ele.find_elements_by_class_name('pv-profile-section__see-more-inline'):
            if re.match("Show ([0-9]+\s)?more", button.text):
                y = button.location['y']

                self.driver.execute_script("arguments[0].click();", button)
                self.__scroll_and_load(total_scroll=100, _from=y)
                self.__show_more_accomplishment(accomplishment_ele)
            break

    def extract_company_info(self, raw_url):
        """ Todo: add this function as general

        OBS: Changes URL
        :param raw_url:
        :return ObjectId:
        """
        """
        self.driver.get(raw_url)

        # Check if user has been logged out
        if "authwall" in self.driver.current_url:
            self.force_login()
            self.driver.get(raw_url)

        url = self.driver.current_url

        company_dict = {
            'name': None,
            'url': url,
            'about': None,
            'webpage': None,
            'type': None,
            'employeeRange': None,
            'employeeCount': None,
            'industry': None,
            'address': None,
            'averageTenure': None
        }
        try:
            
                start_time = time.time()
                about_ele = None
                while time.time() < start_time + self.timeout:
                    about_ele_list = self.driver.find_elements_by_id('org-about-company-module')
                    if len(about_ele_list) > 0:
                        about_ele = about_ele_list[0]

                if about_ele is not None:
                    industry = self.__get_class_element_if_exists('company-industries')

                    company_dict['industry'] = industry.text if industry is not None else industry

                    company_dict['name'] = Utils.string_trim(
                        self.driver.find_element_by_class_name('org-top-card-module__name')
                        .text)

                    company_about_description = self.__get_class_element_if_exists(
                        'org-about-us-organization-description__text.description',
                        sub_ele=about_ele)

                    company_dict[
                        'about'] = company_about_description.text if company_about_description is not None else None

                    extra_about_ele = about_ele.find_element_by_class_name("org-about-company-module__about-us-extra")

                    webpage_ele = self.__get_class_element_if_exists('org-about-company-module__company-page-url',
                                                                     sub_ele=extra_about_ele)

                    company_dict['webpage'] = Utils.string_trim(webpage_ele.find_element_by_tag_name('a')
                                                                .get_attribute(
                        'innerHTML')) if webpage_ele is not None else None

                    type_ele = self.__get_class_element_if_exists('org-about-company-module__company-type',
                                                                  sub_ele=extra_about_ele)

                    company_dict['type'] = Utils.string_trim(type_ele.get_attribute('innerHTML')) if type_ele is not None else None

                    # Employee range
                    employee_range = self.__get_class_element_if_exists(
                        'org-about-company-module__company-staff-count-range', sub_ele=extra_about_ele)


                    company_dict['employeeRange'] = Utils.string_trim(
                        employee_range.get_attribute('innerHTML')) if employee_range is not None else None

                    address_ele = self.__get_class_element_if_exists('org-location-viewer__container',
                                                                     sub_ele=about_ele)

                    if address_ele is not None:
                        company_dict['address'] = Utils.string_trim(
                            address_ele.find_element_by_class_name('org-location-card')
                            .find_element_by_tag_name('p')
                            .get_attribute('innerHTML'))

                    self.__scroll_and_load(total_scroll=200,
                                           _from=
                                           self.driver.find_element_by_id('org-about-company-module__show-details-btn')
                                           .location['y'])
                    start = time.time()

                    # Premium insights
                    while time.time() < start + self.timeout / 3:
                        if len(self.driver.find_elements_by_class_name('org-insights-module__summary-table')) > 0:
                            company_dict['employeeCount'] = int(self.driver
                                                                .find_element_by_class_name(
                                'org-insights-module__summary-table')
                                                                .find_element_by_tag_name('span')
                                                                .get_attribute('innerHTML')
                                                                .replace(',', ''))

                            average_tenure_ele = self.__get_tag_element_if_exists('strong', sub_ele=self.driver
                                                                                  .find_element_by_class_name(
                                'org-insights-headcount-module')
                                                                                  .find_element_by_class_name(
                                'org-insights-module__facts'))

                            company_dict[
                                'averageTenure'] = average_tenure_ele.text if average_tenure_ele is not None else None

                            break
                        else:
                            for title in self.driver.find_elements_by_class_name('org-premium-container__title'):
                                if title.get_attribute('innerHTML') == "Insights not available":
                                    break
                    # Log error
                    if not self.testing:
                        return self.db.add_company(company_dict)
                    else:
                        return "Test company id"

                else:
                    self.db.error_log(str("about_ele not found"), url, "extract_company_info", "company")

                    # Add whatever was gathered. We are sure there is an URL so it will not be run multiple times!
                    return self.db.add_company(company_dict)

        except Exception as e:

            # Log error
            if not self.testing:
                self.db.error_log(str(e), url, str(traceback.format_exc()), "company")

                # Add whatever was gathered. We are sure there is an URL so it will not be run multiple times!
                return self.db.add_company(company_dict)
            else:
                print("\033[94m", end="")
                print(url, "company")
                print(str(e))
                print(str(traceback.format_exc()))
                print("\033[0m")
                return "Test company id"
        """
        pass

    def get_user_info_by_list(self, urls):
        """ Main class. Gets information about the users specified in the urls

        :param urls: list of linkedin urls
        :type urls: list of str
        :return: Data with List of userinformation and error: {data: {profiles: list, errors: list}}
        :rtype dict:
        """
        SHOW_MORE = "pv-profile-section__text-truncate-toggle"
        URL_SIZE = len(urls)

        # Login
        self.force_login()
        # Iterate over urls
        for index, url in enumerate(urls):
            print("{0}/{1} scraping for {2}...".format(index + 1, URL_SIZE, url), end="")
            sys.stdout.flush()
            try:

                total_run_time = time.time()
                self.driver.get(url)
                # Check if user has been logged out
                if "authwall" in self.driver.current_url:
                    self.force_login()
                    self.driver.get(url)
                # Information for linkedIn person
                employee_info = {
                    # 'acceleraceConnection': 1, # Degree of connection to accelerace
                    'url': url,
                    "name": None,
                    "experience": [],
                    "education": [],
                    "skills": [],
                    "connections": [],
                    "connectionsTotal": 0,
                    "languages": [],
                    "patents": [],
                    "honors": []
                }
                # Get name
                start = time.time()
                while time.time() < start + self.timeout:
                    try:
                        employee_info['name'] = Utils.string_trim(
                            self.driver.find_element_by_class_name('pv-top-card-section__name').get_attribute(
                                'innerHTML'))
                        break
                    except Exception as e:
                        pass

                # Have to load the JS-generated html by scrolling
                self.__scroll_and_load()

                # Expand skills
                try:
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_class_name(
                        'pv-skills-section__additional-skills'))
                    time.sleep(1 * self.speed)
                except:
                    pass

                ###########################################################################
                #                               PICTURE                                   #
                ###########################################################################

                # Get picture
                image_div = self.driver.find_element_by_class_name("pv-top-card-section__photo")
                image_style = image_div.get_attribute("style")
                employee_info['image'] = image_style.split("background-image: url(\"")[1].split("\");")[0] if len(
                    image_style.split("background-image: url(\"")) > 1 else None

                ###########################################################################
                #                          Experience information                         #
                ###########################################################################
                ele_list = self.driver.find_elements_by_id('experience-section')
                if len(ele_list) > 0:
                    ele = ele_list[0]
                    # Show more
                    first_iteration = True
                    if len(ele.find_elements_by_class_name(SHOW_MORE)) > 0:
                        start = time.time()
                        while time.time() < start + self.timeout / 3:
                            show_more_list = ele.find_elements_by_class_name(SHOW_MORE)
                            if len(show_more_list) > 0:
                                start = time.time()
                                for show_more in show_more_list:
                                    if re.match("Show [0-9]+ more experience[s]?",
                                                show_more.get_attribute('innerHTML')):
                                        first_iteration = False
                                        scroll_from = show_more.location['y']
                                        self.driver.execute_script("arguments[0].click();", show_more)
                                        self.__scroll_and_load(total_scroll=100, _from=scroll_from)
                                        time.sleep(1 * self.speed)
                                        break
                                # If is says "Show fewer"
                                else:
                                    found = False
                                    for show_more in show_more_list:

                                        if re.match("Show fewer experiences", show_more.get_attribute('innerHTML')):
                                            found = True
                                    if found or first_iteration:
                                        break

                    for p in (ele.find_elements_by_class_name('pv-entity__position-group-pager')):

                        # Expand "See more roles"

                        start_time = time.time()
                        while time.time() < start_time + (self.timeout * self.speed):

                            show_more_ele = self.__get_class_element_if_exists('pv-profile-section__actions-inline',
                                                                               sub_ele=p)

                            if show_more_ele is not None and re.match('Show [0-9]* more role[s]?', show_more_ele.text):
                                start_time = time.time()

                                # TODO: Improve?
                                try:
                                    show_more_ele.click()

                                except:
                                    self.driver.execute_script("arguments[0].click();", show_more_ele)

                                time.sleep(0.5 * self.speed)
                            else:
                                break
                        # Company info
                        company_experience = {
                            "experience": [],
                            "id": None,
                            "name": None,
                            "url": None
                        }

                        # Get link to company (if exists)
                        company_url = p.find_element_by_tag_name('a').get_attribute('href')
                        company_experience[
                            'url'] = company_url if "https://www.linkedin.com/company/" in company_url else None

                        # Get linked In name
                        extended_experience = p.find_elements_by_class_name('pv-entity__summary-info-v2')
                        if len(extended_experience) > 0:
                            company_experience['name'] = p.find_element_by_class_name(
                                'pv-entity__company-summary-info').find_element_by_tag_name(
                                'h3').find_elements_by_tag_name('span')[1].get_attribute('innerHTML')
                            for work_div in extended_experience:
                                company_experience['experience'].append(self.__extract_work_experience(work_div))

                        else:
                            company_experience['name'] = p.find_element_by_class_name(
                                'pv-entity__secondary-title').get_attribute('innerHTML')
                            company_experience['experience'].append(
                                self.__extract_work_experience(p, single_experience=True))

                        employee_info['experience'].append(company_experience)

                ###########################################################################
                #                               Skills                                    #
                ###########################################################################

                for skill in self.driver.find_elements_by_class_name('pv-skill-category-entity__skill-wrapper'):
                    skill_name_container = skill.find_element_by_class_name('pv-skill-category-entity__name')

                    # I.e. search path for data-control-name and not find it

                    employee_info["skills"].append({
                        "skill": Utils.string_trim(
                            skill_name_container.find_element_by_tag_name('a').find_element_by_tag_name('span')
                                .get_attribute('innerHTML')) if len(
                            skill_name_container.find_elements_by_tag_name('a')) > 0 else Utils.string_trim(
                            skill_name_container.get_attribute('innerHTML')),
                        "endorsements": self.__extract_endorsements(skill)
                    })

                ###########################################################################
                #                          Education information                          #
                ###########################################################################

                ele_list = self.driver.find_elements_by_id('education-section')
                if len(ele_list) > 0:
                    ele = ele_list[0]
                    # Show more
                    if len(ele.find_elements_by_class_name(SHOW_MORE)) > 0:
                        start = time.time()
                        while time.time() < start + self.timeout:
                            show_more_list = ele.find_elements_by_class_name(SHOW_MORE)
                            if len(show_more_list) > 0:
                                start = time.time()
                                for show_more in show_more_list:
                                    if re.match("Show [0-9]+ more education", show_more.get_attribute('innerHTML')):
                                        scroll_from = show_more.location['y']
                                        self.driver.execute_script("arguments[0].click();", show_more)
                                        self.__scroll_and_load(total_scroll=100, _from=scroll_from)
                                        time.sleep(1 * self.speed)
                                        break
                                # If is says "Show fewer"
                                else:

                                    found = False
                                    for show_more in show_more_list:

                                        if re.match("Show fewer education", show_more.get_attribute('innerHTML')):
                                            found = True
                                    if found:
                                        break

                    for main_ele in ele.find_elements_by_class_name('pv-education-entity'):
                        summary_ele = main_ele.find_element_by_class_name("pv-entity__summary-info")
                        duration_ele = self.__get_class_element_if_exists('pv-entity__dates', sub_ele=summary_ele)
                        if duration_ele is not None:
                            duration = duration_ele.find_elements_by_tag_name('span')[
                                1].find_elements_by_tag_name('time')  # TODO Replace with \U+2013 (dash unicode)
                        else:
                            # Will become From None To None later in the code
                            duration = []

                        degree = summary_ele.find_element_by_class_name(
                            'pv-entity__degree-info').find_elements_by_class_name('pv-entity__comma-item')

                        school_url_raw = main_ele.find_element_by_tag_name('a').get_attribute('href')
                        school_url = school_url_raw if "https://www.linkedin.com/school/" in school_url_raw else None

                        employee_info['education'].append({
                            "schoolName": summary_ele.find_element_by_class_name(
                                "pv-entity__school-name").get_attribute('innerHTML'),
                            "url": school_url,
                            "degree": degree[0].get_attribute('innerHTML') if len(degree) > 1 else None,
                            "fields": degree[1].get_attribute('innerHTML') if len(degree) > 1 else None,
                            "dateFrom": duration[0].get_attribute('innerHTML') if len(duration) > 0 else None,
                            "dateTo": duration[1].get_attribute('innerHTML') if len(duration) > 1 else None,
                        })

                ###########################################################################
                #                            Accomplishments                              #
                ###########################################################################

                ele_list = self.driver.find_elements_by_class_name('pv-accomplishments-section')

                if len(ele_list) > 0:

                    ele = ele_list[0]

                    self.__scroll_and_load(total_scroll=300, _from=ele.location['y'])
                    ###############
                    #  Languages  #
                    ###############

                    language_ele = self.__get_class_element_if_exists("pv-accomplishments-block.languages",
                                                                      sub_ele=ele)
                    if language_ele is not None:

                        #  Expand
                        self.driver.execute_script("arguments[0].click();", language_ele.find_element_by_class_name(
                            'pv-accomplishments-block__expand'))
                        time.sleep(0.5 * self.speed)
                        # Show more rec
                        self.__show_more_accomplishment(language_ele)

                        language_skill_list = language_ele.find_elements_by_class_name("pv-accomplishment-entity")
                        language_skill_list_len = len(language_skill_list)
                        for i, language_skill in enumerate(language_skill_list):

                            proficiency = self.__get_class_element_if_exists(
                                'pv-accomplishment-entity__proficiency', sub_ele=language_skill)

                            employee_info['languages'].append({'language': Utils.string_trim(
                                language_skill.find_element_by_class_name('pv-accomplishment-entity__title')
                                    .get_attribute('innerHTML').replace(
                                    "<span class=\"visually-hidden\">Language name</span>", "")),
                                'proficiency': Utils.string_trim(
                                    proficiency.text.replace("proficiency",
                                                             "")) if proficiency is not None else None})

                            # Scroll down on last element
                            if i == language_skill_list_len - 1:
                                self.__scroll_and_load(total_scroll=300, _from=language_skill.location['y'])

                    #############
                    #  Patents  #
                    #############

                    patent_ele = self.__get_class_element_if_exists("pv-accomplishments-block.patents", sub_ele=ele)
                    if patent_ele is not None:

                        # Expand
                        self.driver.execute_script("arguments[0].click();", patent_ele.find_element_by_class_name(
                            'pv-accomplishments-block__expand'))

                        time.sleep(0.5 * self.speed)
                        self.__show_more_accomplishment(patent_ele)

                        patent_list = patent_ele.find_elements_by_class_name("pv-accomplishment-entity")
                        patent_list_len = len(patent_list)
                        for i, patent in enumerate(patent_list):

                            patent_date = self.__get_class_element_if_exists("pv-accomplishment-entity__date",
                                                                             sub_ele=patent)

                            employee_info['patents'].append({
                                'patent': Utils.string_trim(
                                    patent.find_element_by_class_name('pv-accomplishment-entity__title')
                                        .get_attribute('innerHTML')
                                        .replace("<span class=\"visually-hidden\">Patent title</span>", "")),
                                'date': Utils.string_trim(
                                    patent_date.get_attribute('innerHTML').replace(
                                        "<span class=\"visually-hidden\">Patent date</span>", "").replace("Issued",
                                                                                                          ""))
                                if patent_date is not None else patent_date,
                                'patentIssuerAndNumber': Utils.string_trim(
                                    patent.find_element_by_class_name('pv-accomplishment-entity__issuer')
                                        .get_attribute('innerHTML').replace(
                                        "<span class=\"visually-hidden\">Patent issuer and number</span>", ""))
                            })

                            # Scroll down on last element
                            if i == patent_list_len - 1:
                                self.__scroll_and_load(total_scroll=300, _from=patent.location['y'])

                    #######################
                    #  Honors and awards  #
                    #######################

                    honor_ele = self.__get_class_element_if_exists("pv-accomplishments-block.honors", sub_ele=ele)
                    if honor_ele is not None:

                        self.driver.execute_script("arguments[0].click();", honor_ele.find_element_by_class_name(
                            'pv-accomplishments-block__expand'))
                        time.sleep(0.5 * self.speed)
                        self.__show_more_accomplishment(honor_ele)

                        honor_list = honor_ele.find_elements_by_class_name("pv-accomplishment-entity")
                        honor_list_len = len(honor_list)
                        for i, honor in enumerate(honor_list):

                            honor_date = self.__get_class_element_if_exists('pv-accomplishment-entity__date', honor)
                            honor_issuer = self.__get_class_element_if_exists('pv-accomplishment-entity__issuer',
                                                                              honor)

                            employee_info['honors'].append({
                                'honor': Utils.string_trim(
                                    honor.find_element_by_class_name('pv-accomplishment-entity__title')
                                        .get_attribute('innerHTML')
                                        .replace("<span class=\"visually-hidden\">honor title</span>", "")),
                                'date': Utils.string_trim(
                                    honor_date.get_attribute('innerHTML')
                                        .replace("<span class=\"visually-hidden\">honor date</span>",
                                                 "")) if honor_date is not None else None,
                                'issuer': Utils.string_trim(
                                    honor_issuer.get_attribute('innerHTML')
                                        .replace("<span class=\"visually-hidden\">honor issuer</span>",
                                                 "")) if honor_issuer is not None else None
                            })

                            # Scroll down on last element
                            if i == honor_list_len - 1:
                                self.__scroll_and_load(total_scroll=300, _from=honor.location['y'])

                ###########################################################################
                #                              Connections                                #
                ###########################################################################

                # Do this last as it goes to a new page
                if len(self.driver.find_elements_by_class_name('pv-top-card-v2-section__link--connections')) > 0:
                    conn_url = self.driver.find_element_by_class_name(
                        'pv-top-card-v2-section__link--connections').get_attribute('href')
                    if conn_url is None:
                        conn_string = self.driver.find_element_by_class_name(
                            'pv-top-card-v2-section__connections').get_attribute('innerHTML')
                        employee_info['connections'] = []
                        employee_info['connectionsTotal'] = Utils.string_trim(
                            conn_string.split(" connections")[0].split("+")[0])
                    else:

                        # Go to a new page

                        employee_info['connections'], employee_info[
                            'connectionsTotal'] = self.__get_connected_links(conn_url, get_links=False)
                else:
                    employee_info['connections'] = []
                    employee_info['connectionsTotal'] = None

                self.data['profiles'].append(employee_info)
                print("\033[92m Done in {0} sec\033[0m".format(time.time() - total_run_time))

            # Log error
            except Exception as e:
                print("\033[91m Error\033[0m")
                self.data['errors'].append({
                    'error': str(e),
                    'traceback': str(traceback.format_exc()),
                    'url': url
                })

        self.driver.close()  # Terminate the self.driver
        return self.data
