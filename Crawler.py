from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path='G:\chromedriver.exe')

url_codechef = r'https://www.codechef.com/'
driver.get(url_codechef)
time.sleep(5)
ele = driver.find_element_by_id('upcoming-timer')
link = ele.find_element_by_css_selector('a')
print('For CodeChef - ')
print('Contest Name : '+ link.text)
link = ele.find_element_by_css_selector('a').get_attribute('href')
driver.get(link)
time.sleep(5)
start_time = driver.find_element_by_xpath('//*[@id="rules"]/div/div/div/ul[1]/li[2]')
date_list = start_time.text.split(' ')
print('Date : '+date_list[3]+" "+date_list[4]+" "+date_list[5])
print('Timing : '+date_list[-3]+" "+date_list[-2]+'\n\n')


# url_code_forces = r'https://codeforces.com/'
# driver.get(url_code_forces)
# time.sleep(5)
#
# ele = driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div[4]/div[1]/a[1]')
# ele.click()
# time.sleep(5)
# contest = driver.find_element_by_css_selector("td:nth-child(1)").text
# print('For Codeforces - ')
# print('Contest Name : '+contest)
# start_time = driver.find_element_by_css_selector("td:nth-child(3)").text
# list = start_time.split(' ')
# date = list[0]
# print(date)
# time = list[1]
# print(time+'\n\n')


url_leet_code = r'https://leetcode.com/contest/'
driver.get(url_leet_code)
time.sleep(5)
ele1 = driver.find_element_by_css_selector('div.card-title').text
print('For Leetcode - ')
print('Contest Name : '+ele1)
ele = driver.find_element_by_css_selector('div.time').text
time_list = ele.split('@')
time = time_list[0]
print('Date : '+time)
duration = time_list[1]
print('Duration: '+duration)

driver.quit()
