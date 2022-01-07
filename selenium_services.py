 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver


class Selenium_services():

    def __init__(self):
        self.by = By
        self.wait = None
        self.driver = None
        self.extract = None

    def open_driver(self, url):
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            options.add_argument("--disable-browser-side-navigation")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--ignore-ssl-errors")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("lang=pt-br")
            options.add_argument("--start-maximized")


            self.driver = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)
            self.extract = WebDriverWait(self.driver,8)
            self.wait = WebDriverWait(self.driver,40)
            self.driver.get(url)
            return True
        except Exception as chromeException:
            print(str(chromeException))
            return False

    def refresh(self):
        self.driver.refresh()
        time.sleep(3)

    def backpage(self):
        self.driver.back()

    def switch_iframe(self,frame_name):
        try:
            self.driver.switch_to_frame(frame_name)
            return True
        except Exception as frameException:
            print("Erro ao trocar iframes."+str(frameException))
            return False
    
    def close_driver(self):
        try:
            if not self.driver == None:
                self.driver.quit()
                self.driver.close()
                self.driver = None
        except Exception as chromecloseException:
            print(str(chromecloseException))
            return False


    def check_element_exist(self,tipo,element):
        try:
            self.wait.until(EC.visibility_of_element_located((tipo,element)))
            return True
        except Exception as check_element_error:
            print("Elemento "+ element +" nao existe."+str(check_element_error))
            return False

    def click(self,tipo, element):
        try:
            self.wait.until(EC.visibility_of_element_located((tipo,element))).click()
            return True
        except Exception as clickException:
            print("Erro ao clicar no elemento "+element+"."+str(clickException))
            return False

    def click_scroll(self,tipo, element):
        while True:
            try:
                self.wait.until(EC.visibility_of_element_located((tipo,element))).click()
                break
            except:
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body"))).send_keys(Keys.ARROW_DOWN)
                time.sleep(1)


    def extract_value(self,tipo,element):
        try:
            value = self.driver.find_element(tipo,element).text
            if not value == None:
                    return value
            else:
                raise Exception
        except Exception as valueError:
            print("nao foi possivel obter o valor do elemento "+element+"."+str(valueError))
            return None

    def extract_elements(self, tipo, element):
        try:    
            value = self.driver.find_elements(tipo,element)
            return value
        except Exception as error:
            print("Erro ao trazer varios elementos."+str(error))
        return None

    def scroll_page(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body"))).send_keys(Keys.PAGE_DOWN)