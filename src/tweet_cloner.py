import os
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TweetCloner:
    def __init__(self, driver, download_dir="downloads"):
        self.driver = driver
        self.download_dir = download_dir
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def search_user(self, username):
        """Search for a user using the search bar."""
        print("Navigating to Twitter homepage...")
        self.driver.get("https://twitter.com/home")
        
        # Wait for the search bar to appear
        print("Waiting for the search bar...")
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]'))
        )
        
        # Find the search bar, click on it, and enter the username
        print(f"Searching for user: {username}")
        search_input = self.driver.find_element(By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')
        search_input.click()
        search_input.clear()
        search_input.send_keys(username)
        search_input.send_keys("\n")  # Press Enter to search
        
        # Wait for the search results to load
        print("Waiting for search results...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//a[contains(@href, "/{username}")]'))
        )
        
        # Click on the user's profile link
        print(f"Opening profile of {username}...")
        user_profile = self.driver.find_element(By.XPATH, f'//a[contains(@href, "/{username}")]')
        user_profile.click()

    def clone_tweets(self, username, count=5):
        """Clone tweets from a user's profile."""
        self.search_user(username)
        
        # Wait for the tweets to load
        print("Waiting for tweets to load...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//article[@data-testid="tweet"]'))
        )
        
        tweets = []
        seen_tweets = set()  # To track duplicates
        scroll_attempts = 0  # To prevent infinite scrolling
        max_scroll_attempts = 10  # Limit the number of scrolls

        while len(tweets) < count and scroll_attempts < max_scroll_attempts:
            # Find all tweet elements
            tweet_elements = self.driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
            print(f"Found {len(tweet_elements)} tweet elements on the page.")

            for tweet in tweet_elements:
                if len(tweets) >= count:
                    break
                
                # Extract tweet text
                try:
                    tweet_text = tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
                    print(f"Extracted tweet text: {tweet_text}")
                except Exception as e:
                    tweet_text = "No text found"
                    print(f"Error extracting tweet text: {e}")

                # Extract image URLs
                try:
                    image_elements = tweet.find_elements(By.XPATH, './/img[contains(@src, "twimg")]')
                    image_urls = []
                    for img in image_elements:
                        img_src = img.get_attribute("src")
                        # Skip profile images by checking for specific patterns
                        if "profile_images" not in img_src:
                            # Check if the image is from a video
                            if "video" in img_src:
                                image_urls.append(f"Image in video: {img_src}")
                            else:
                                image_urls.append(img_src)
                    print(f"Extracted {len(image_urls)} image(s).")
                except Exception as e:
                    image_urls = []
                    print(f"Error extracting images: {e}")

                # Avoid duplicates
                if tweet_text not in seen_tweets:
                    seen_tweets.add(tweet_text)
                    tweets.append({"text": tweet_text, "images": image_urls})
                    print(f"Cloned tweet: {tweet_text}")
            
            # Scroll down to load more tweets if needed
            print("Scrolling down to load more tweets...")
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)  # Allow time for new tweets to load
            scroll_attempts += 1

        if len(tweets) < count:
            print(f"Only {len(tweets)} tweets were found after {scroll_attempts} scroll attempts.")

        # Save tweets and images
        self.save_tweets(username, tweets)
        print(f"Cloned {len(tweets)} tweets from @{username}.")

    def save_tweets(self, username, tweets):
        """Save tweets and images to the local machine."""
        print("Saving tweets and images...")
        # Save tweets to a text file
        with open(os.path.join(self.download_dir, f"{username}_tweets.txt"), "w", encoding="utf-8") as file:
            for i, tweet in enumerate(tweets, 1):
                file.write(f"Tweet {i}:\n{tweet['text']}\n")
                for img_url in tweet['images']:
                    file.write(f"{img_url}\n")
                file.write("\n")