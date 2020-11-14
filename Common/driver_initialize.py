import os
from Common import read_json as json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverInitialize:

    def initialize(self, browserType):
        global driver
        if browserType == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        if browserType == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        return driver

    def getTestJsonFileSettings(self):
        testDataPath = os.path.abspath("test_settings.json")

        return testDataPath

    def getJsonFileAttributeValue(self, jsonFile, attribute):
        testDataJsonFile = json.readJson(jsonFile)
        return testDataJsonFile[attribute]

    def getDriver(self):
        return driver