import time

class Selenium:
def init(self, browser="chrome"):
self.browser = browser
def open_browser(self):
    print(f"Opening {self.browser} browser...")
    time.sleep(2)
    
def close_browser(self):
    print("Closing browser...")
    time.sleep(2)
    
def execute_test(self, test_case):
    print(f"Executing test case: {test_case}...")
    time.sleep(2)
