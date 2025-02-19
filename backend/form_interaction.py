import pandas as pd
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time  





def setup_driver():
    chrome_options = Options()  
    service = Service()  
    return webdriver.Chrome(service=service, options=chrome_options)


def interact_with_form():
    driver = setup_driver() 
    file_path = "C:\\Users\\yarde\\OneDrive\\games1.xlsx"
   

    try:
        # Open the website
        # Navigate to the specified URL
        driver.get("http://127.0.0.1:5500/frontend/index.html")
        # time.sleep(2)  # Pause for 2 seconds to let the page load

        # Create a wait object with 10-second timeout
        wait = WebDriverWait(driver, 30)

     
        name_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        name_field.send_keys("rortheWomen")
        password_field.send_keys("1234")
        login_button.click()
        try:
            alert = driver.switch_to.alert
            alert.accept()  # Accept the alert
            print("Alert accepted")
        except:
            print("No alert appeared")
        wait.until(EC.visibility_of_element_located((By.ID, "main-section")))
       
      
        df = pd.read_excel(file_path) 
        wait = WebDriverWait(driver, 30)
        # Wait for the main section to be visible after login
      
    


      
        for index, row in df.iterrows():
            
            game_name = wait.until(
            EC.presence_of_element_located((By.ID, "game-title"))
          ) 
            game_name.send_keys(row['title'])
            game_genre=driver.find_element(By.ID, "game-genre")
            game_genre.send_keys(row['genre'])
            game_price=driver.find_element(By.ID, "game-price")
            game_price.send_keys(row['price'])
            game_quantity=driver.find_element(By.ID, "game-quantity")
            game_quantity.send_keys(row['quantity'])
            add_game_button = driver.find_element(By.XPATH, "//button[text()='Add Game']")
            add_game_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "games-list")))
            time.sleep(1)


    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Print any errors that occur

    finally:
        driver.quit()  # Close the browser, regardless of success or failure


# Script entry point
# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    interact_with_form()  # Start the form interaction process