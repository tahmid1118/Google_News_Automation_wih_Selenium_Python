class Loginpage():
    def __init__(self, driver):
        self.driver = driver
        self.signin_button_xpath = '//*[@id="gb"]/div[2]/div[3]/div[1]/a'
        self.email_form_xpath = '//*[@id="identifierId"]'
        self.nextbutton_xpath = '//*[@id="identifierNext"]/div/button'
        self.password_form_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
        self.loginbutton_xpath = '//*[@id="passwordNext"]/div/button'


    def signin_button(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_form_xpath).send_keys(email)

    def next_button(self):
        self.driver.find_element_by_xpath(self.nextbutton_xpath).click()

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_form_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.loginbutton_xpath).click()


