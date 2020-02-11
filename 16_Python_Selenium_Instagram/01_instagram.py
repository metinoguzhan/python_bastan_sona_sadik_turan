from instagramUserInfo import userName, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, userName, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en,en_US'})

        self.browser = webdriver.Chrome(
            'chromedriver.exe', chrome_options=self.browserProfile)
        self.userName = userName
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        userNameInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')

        userNameInput.send_keys(self.userName)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)
        # self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        time.sleep(2)

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.userName}/")
        time.sleep(2)

        self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)

        dialog = self.browser.find_element_by_xpath('/html/body/div[4]')
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first Count : {followerCount}")

        action = webdriver.ActionChains(self.browser)
        dialog.click()
        action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        dialog = self.browser.find_element_by_xpath('/html/body/div[4]')
        dialog.click()
        while followerCount < max:
            action.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(2)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")
        followerList = []
        i = 0
        for user in followers:          
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            i+=1
            if i == max:
                break

        with open("followers.txt", "w", encoding='utf-8') as file:
            for item in followerList:
                file.write(item+"\n")
            file.close()

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name('button')
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unfollowUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name('button')
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath(
                '//button[text() = "Unfollow"]').click()
        else:
            print("Zaten takip etmiyorsunuz")


instagram = Instagram(userName, password)

instagram.signIn()

instagram.getFollowers(10)

# lists = ['yazilimoji','kod_evreni']
# for item in lists:
#     instagram.followUser(item)
#     time.sleep(3)


# lists = ['yazilimoji','kod_evreni']
# for item in lists:
#     instagram.unfollowUser(item)
#     time.sleep(3)
