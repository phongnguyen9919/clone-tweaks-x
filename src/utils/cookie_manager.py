def save_cookies(driver, filepath):
    """Lưu cookie vào file"""
    import pickle
    with open(filepath, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, filepath):
    """Tải cookie từ file"""
    import pickle
    with open(filepath, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)