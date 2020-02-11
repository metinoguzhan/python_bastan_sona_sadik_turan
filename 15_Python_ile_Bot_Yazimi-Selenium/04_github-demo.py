from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followings = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element_by_xpath('//*[@id="login_field"]')
        password = self.browser.find_element_by_xpath('//*[@id="password"]')

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[3]/input[8]').click()
    def loadFollowings(self):
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')
        for item in items:
           self.followings.append(item.find_element_by_css_selector(".link-gray.pl-1").text)

    def getFollowings(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(1)
       
        self.loadFollowings()
        
        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    
                    self.loadFollowings()
                else:
                    break   
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        
                        self.loadFollowings()

                    else:
                        continue

github = Github(username,password)
github.signIn()
github.getFollowings()
print(f"Followings Count : {len(github.followings)}")
print(github.followings)