# Twitter Clone Project

This project is a simple application that uses Selenium to log in to Twitter and clone tweets from Elon Musk's Twitter account.

## Project Structure

```
twitter-clone-project
├── src
│   ├── main.py               # Entry point of the application
│   ├── twitter_login.py      # Handles Twitter login functionality
│   ├── tweet_cloner.py       # Clones tweets from Elon Musk's account
│   └── utils
│       └── cookie_manager.py  # Manages session cookies
├── requirements.txt          # Lists project dependencies
└── README.md                 # Project documentation
```

## Requirements

To run this project, you need to have Python installed along with the following libraries:

- Selenium

You can install the required libraries using pip:

```
pip install -r requirements.txt
```

## Usage

1. **Set Up Your Credentials**: Open `src/twitter_login.py` and replace the placeholder values for `USERNAME` and `PASSWORD` with your Twitter credentials.

2. **Run the Application**: Execute the `main.py` file to start the application. This will log you into Twitter and clone tweets from Elon Musk's account.

```
python src/main.py
```

## Notes

- Ensure that you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Google Chrome).
- The application will save your session cookies to avoid logging in every time you run the script.
- Make sure to comply with Twitter's terms of service when using this application.