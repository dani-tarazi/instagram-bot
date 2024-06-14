import undetected_chromebrowser as webdriver
import time

options = webdriver.ChromeOptions()
profile = "C:\\Users\\harry\\appdata\\local\\Google\\Chrome\\User Data\\Default\\Default "
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options,use_subprocess=True)
driver.get("https://www.instagram.com/accounts/emailsignup/")

time.sleep(100000)



from instabot import Bot
bot = Bot()


