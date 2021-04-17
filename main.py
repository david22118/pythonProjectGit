
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chromeBrowserOptions
from selenium.webdriver.firefox.options import Options as firefoxBrowserOptions
from msedge.selenium_tools import EdgeOptions
from time import sleep

# config

firefox_path = "c:/geckodriver.exe"
chrome_path = "c:/chromedriver.exe"
edge_path = "c:/msedgedriver.exe"
chrome_browser = 'Chrome'
selenium_word = "Selenium"
ynet_url = "https://www.ynet.co.il"
walla_url = "https://www.walla.co.il"
google_translate = "https://translate.google.co.il/"
you_tube = "https://www.youtube.com/"
facebook = "https://www.facebook.com/"
github = "https://github.com/"

facebook_input_email_xpath = "//input[@id='email']"
facebook_input_password_xpath = "//input[@id='pass']"
facebook_log_in_button_xpath = "//button[@name='login']"
facebook_credentials = {"email": "davidy22118@gmail.com", "password": "blblbl"}

github_input_xpath = "//input[contains(@class,'form-control')]"
input_xpath = "//input[@id='search']"
search_button_xpath = "//button[@id='search-icon-legacy']"
target_element_xpath = "//button[contains(@class, 'no-desktop')]"
text_area_xpath = "//textarea[@role='combobox']"
text_area_selector = "textarea[role='combobox']"
text_area_selector_child = "span>div>textarea"
expected_title = "וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון"
video_name = "mortal kombat trailer 2021"
text = "שלום"


# 1
def lunch_browser(path, web_browser=None):
    if web_browser:
        return webdriver.Chrome(executable_path=path)
    else:
        return webdriver.Firefox(executable_path=path)


def open_url(url, browser):
    browser.get(url)


def close_browser(browser):
    browser.close()


def validate_test_flow(url, browser_path, web_browser=None):
    def enter_url(inner_function):
        browser = lunch_browser(browser_path, web_browser)
        open_url(url, browser)

        def wrapper_function(*args):
            inner_function(browser, *args)

            def close():
                close_browser(browser)

            return close()

        return wrapper_function

    return enter_url


2


@validate_test_flow(walla_url, chrome_path, chrome_browser)
def asert_title(browser, expected_website_title):
    title = browser.title
    browser.refresh()
    assert title == expected_website_title


asert_title(expected_title)


# # 3
@validate_test_flow(walla_url, chrome_path, chrome_browser)
def locate_element(browser, element_xpath):
    return browser.find_element_by_xpath(element_xpath)


target_element_from_chrome = locate_element(target_element_xpath)


@validate_test_flow(walla_url, firefox_path)
def locate_element(browser, element_xpath):
    return browser.find_element_by_xpath(element_xpath)


target_element_from_firefox = locate_element(target_element_xpath)

assert target_element_from_chrome == target_element_from_firefox


# # 4
@validate_test_flow(google_translate, chrome_path, chrome_browser)
def write_text_google_translate(browser, text_area, random_text):
    text_box = browser.find_element_by_xpath(text_area)
    text_box.send_keys(random_text)
    sleep(5)


write_text_google_translate(text_area_xpath, text)


# 5
@validate_test_flow(you_tube, chrome_path, chrome_browser)
def search_video_you_tube(browser, search_input_xpath, desirable_video_name, search_button):
    text_box = browser.find_element_by_xpath(search_input_xpath)
    text_box.send_keys(desirable_video_name)
    sleep(2)
    browser.find_element_by_xpath(search_button).click()
    sleep(2)


search_video_you_tube(input_xpath, video_name, search_button_xpath)


# 6
@validate_test_flow(google_translate, chrome_path, chrome_browser)
def print_different_locators(browser, xpath, selector, child_selector):
    text_box_by_xpath = browser.find_element_by_xpath(xpath)
    text_box_by_selector = browser.find_element_by_css_selector(selector)
    text_box_by_selector_child = browser.find_element_by_css_selector(child_selector)
    print(f"WebElement text box by xpath:{text_box_by_xpath}")
    print(f"WebElement text box by selector:{text_box_by_selector}")
    print(f"WebElement text box by child selector:{text_box_by_selector_child}")


print_different_locators(text_area_xpath, text_area_selector, text_area_selector_child)


# 7
@validate_test_flow(facebook, chrome_path, chrome_browser)
def login_into_facebook(browser, email_input_locator, password_input_locator, sign_in_input_locator, credentials):
    email_input = browser.find_element_by_xpath(email_input_locator)
    password_input = browser.find_element_by_xpath(password_input_locator)
    sign_in_button = browser.find_element_by_xpath(sign_in_input_locator)
    email_input.send_keys(credentials["email"])
    password_input.send_keys(credentials["password"])
    sleep(2)
    sign_in_button.click()
    sleep(10)


login_into_facebook(
    facebook_input_email_xpath,
    facebook_input_password_xpath,
    facebook_log_in_button_xpath,
    facebook_credentials
)


# 8
@validate_test_flow(you_tube, chrome_path, chrome_browser)
def delete_all_cookies(browser):
    browser.delete_all_cookies()
    print(browser.get_cookies())


delete_all_cookies()


# 9
@validate_test_flow(github, chrome_path, chrome_browser)
def search_in_github(browser, github_input_locator, type_word):
    github_input = browser.find_element_by_xpath(github_input_locator)
    github_input.send_keys(type_word + Keys.ENTER)
    sleep(5)


search_in_github(github_input_xpath, selenium_word)

# 10
chrome_options = chromeBrowserOptions()
chrome_options.add_argument('--disable-extensions')
browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
open_url(you_tube, browser)
sleep(5)
close_browser(browser)

firefox_options = firefoxBrowserOptions()
firefox_options.add_argument('--disable-extensions')
browser = webdriver.Firefox(executable_path=firefox_path, firefox_options=firefox_options)
open_url(you_tube, browser)
sleep(5)
close_browser(browser)

options = EdgeOptions()
options.use_chromium = True
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path=edge_path, options=options)
open_url(you_tube, browser)
sleep(5)
close_browser(browser)
