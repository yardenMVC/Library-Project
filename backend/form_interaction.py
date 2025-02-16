
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time  


def setup_driver():
    chrome_options = Options()  # Create a new Options object for Chrome
    service = Service()  # Create a new Service object to manage ChromeDriver
    # Initialize Chrome with our settings
    return webdriver.Chrome(service=service, options=chrome_options)


def interact_with_form():
    driver = setup_driver()  # Create a new browser instance

    try:
        # Open the website
        # Navigate to the specified URL
        driver.get("http://127.0.0.1:5500/frontend/index.html")
        # time.sleep(2)  # Pause for 2 seconds to let the page load

        # Create a wait object with 10-second timeout
        wait = WebDriverWait(driver, 20)

        # Handle the name field
        name_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )  # Wait until name field is present

        name_field.send_keys("rortheWomen")
        password_find=driver.find_element(By.ID, "password")
        password_find.send_keys("1234")
        button_find=driver.find_element(By.ID,"button")
        button_find.click()
        i=0
        wait = WebDriverWait(driver, 10)
        while i!=len(list):
            game_name=list[i][0]
            game_genre-list[i][1]
            game_price=list[i][2]
            game_quantity=list[i][3]
            game_name = wait.until(
            EC.presence_of_element_located((By.ID, "game-title"))
          ) 
            name_field.send_keys(list[i][0])
            





     

   
       

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Print any errors that occur

    finally:
        driver.quit()  # Close the browser, regardless of success or failure


# Script entry point
# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    interact_with_form()  # Start the form interaction process