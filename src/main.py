from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twitter_login import TwitterLogin
from tweet_cloner import TweetCloner

# Replace with your credentials and cookie file path
USERNAME = "phongnguyen9919"
PASSWORD = "Phong789123"
COOKIE_FILE = "twitter_cookies.pkl"

def main():
    # Set up Chrome options to open in full-screen mode
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open browser in full-screen mode

    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome(options=chrome_options)  # Ensure ChromeDriver is installed and matches your Chrome version
    try:
        # Create an instance of TwitterLogin
        twitter_login = TwitterLogin(driver, USERNAME, PASSWORD, COOKIE_FILE)
    
        # Attempt to log in to Twitter
        twitter_login.login()

        # Create an instance of TweetCloner
        tweet_cloner = TweetCloner(driver)

        # Clone tweets from Elon Musk's account
        tweet_cloner.clone_tweets("elonmusk", count=5)
    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()