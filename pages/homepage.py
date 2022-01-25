class Homepage():
    def __init__(self, driver):
        self.driver = driver
        self.search_bar_xpath = '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
        self.featured_topic_xpath = '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]'
        self.latest_news_xpath = '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[2]/div/div/div[4]/div/div/div/div[2]'

    def search_featured_topic(self):
        self.driver.find_element_by_xpath(self.search_bar_xpath).click()

    def goto_featured_topic(self):
        self.driver.find_element_by_xpath(self.featured_topic_xpath).click()

