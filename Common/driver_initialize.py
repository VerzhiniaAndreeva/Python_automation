import os
from Common import read_json as json
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

class DriverInitialize:

    def initialize(browserType):
        if browserType == "firefox":
            return webdriver.Firefox(executable_path="C:\\Users\\Verzhi\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")

        if browserType == "chrome":
            return webdriver.Chrome(executable_path="C:\\Users\\Verzhi\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def getTestJsonFileSettings(self):
        testDataPath = os.path.abspath("test_settings.json")

        return testDataPath

    def getJsonFileAttributeValue(jsonFile, attribute):
        testDataJsonFile = json.readJson(jsonFile)
        return testDataJsonFile[attribute]
