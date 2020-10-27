import os
from Common import read_json as json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverInitialize:

    def initialize(self, browserType):
        if browserType == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())

        if browserType == "chrome":
            return webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def getTestJsonFileSettings(self):
        testDataPath = os.path.abspath("test_settings.json")

        return testDataPath

    def getJsonFileAttributeValue(self, jsonFile, attribute):
        testDataJsonFile = json.readJson(jsonFile)
        return testDataJsonFile[attribute]
