import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username=input('Enter Username: ')
password=input('Enter Paasword:')

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get(r'https://www.instagram.com/')
driver.implicitly_wait(3)

usernameBtn=driver.find_element_by_name('username')
usernameBtn.clear()
usernameBtn.send_keys(username)
# usernameBtn.send_keys('veedu_inka_maaradu')
passwordBtn=driver.find_element_by_name('password')
passwordBtn.clear()
passwordBtn.send_keys(password)
# passwordBtn.send_keys('MuvvalaNavvakala2354')

loginBtn=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
loginBtn.click()
print('Login Successfully')

# notnowBtn=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notnowBtn=driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]')
notnowBtn.click()
print('notnow clicked')
time.sleep(2)

notnowBtn1=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notnowBtn1.click()
print('notnow1 clicked')
time.sleep(1)

# message=driver.find_element(by=By.XPATH,value='')

# find=driver.find_element(by=By.XPATH,value="//input[@placeholder='Search']")
# word="#sunnyleone"
# find.send_keys(word)
# find.send_keys(Keys.ENTER)

print('finded')


# time.sleep(5)
# driver.close()
