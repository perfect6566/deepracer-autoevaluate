import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



IAM_Username="D09"
IAM_Password='password'
Player_Username='aa@zzz.com'
Player_Password='password'
ACCOUNT_ID=3333333333333


# this is your chrome exe file path, it is only for automation test purpose
#  you can download chrome exe and chrome driver in this page:https://googlechromelabs.github.io/chrome-for-testing/
chromepath = r'D:\Download\chrome-win64\chrome.exe'
# this is your chromedriver path
chromedriverpath = r'D:\Download\chromedriver-win64\chromedriver.exe'

# sleep for 10s to wait page loading
sleeptime=10
# Run every 30 minutes
Run_Period=30


def exceptionforfeedback(driver):
    try:
        submit = driver.find_element('xpath', "//button[starts-with(@title,'Close feedback dialog')]")
        submit.click()
    except Exception as e:
        print(str(e))

def evaluate_deepracer(count):

    iamid = ACCOUNT_ID
    options = Options()
    options.binary_location = chromepath
    options.add_argument("--start-fullscreen")

    driver = webdriver.Chrome(service=Service(chromedriverpath), options=options)

    loginurl = f"https://{iamid}.signin.aws.amazon.com/console"
    driver.get(loginurl)
    time.sleep(2)

    username = driver.find_element(By.ID, 'username')
    username.send_keys(IAM_Username)
    time.sleep(1)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(IAM_Password)
    time.sleep(1)

    loginbutton = driver.find_element(By.ID, "signin_button")
    loginbutton.click()
    time.sleep(1)

    url = 'https://us-east-1.console.aws.amazon.com/deepracer/home?region=us-east-1#welcome'
    driver.get(url)

    time.sleep(sleeptime)
    exceptionforfeedback(driver)

    emailusername = driver.find_element(By.NAME, 'email')
    emailusername.send_keys(Player_Username)
    emailpasssword = driver.find_element(By.NAME, 'password')
    emailpasssword.send_keys(Player_Password)

    submit = driver.find_element('xpath', "//span[text()='Sign in']")
    submit.click()

    time.sleep(sleeptime)
    #your model link in deepracer
    modelpage = 'https://us-east-1.console.aws.amazon.com/deepracer/home?region=us-east-1#model/modelid'
    driver.get(modelpage)

    time.sleep(sleeptime)
    exceptionforfeedback(driver)

    time.sleep(sleeptime)
    exceptionforfeedback(driver)

    evaluatetab = driver.find_element('xpath', "//button[starts-with(@data-testid,'evaluationTab')]")
    evaluatetab.click()
    time.sleep(sleeptime)


    # 向下滚动
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.ID, "PLCHLDR_model_start_evaluation")).perform()
    time.sleep(sleeptime)
    startevaluate = driver.find_element(By.ID, "PLCHLDR_model_start_evaluation")
    startevaluate.click()
    time.sleep(sleeptime)

    evaluateNameinput = driver.find_element('xpath', "//input[starts-with(@aria-labelledby,'EvaluationName_undefined')]")
    modelid=1
    num=count
    modelname=f'Helix-evaluate-{modelid}-{num}'
    evaluateNameinput.send_keys(modelname)
    time.sleep(sleeptime)

    body=driver.find_element(By.CSS_SELECTOR,'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(sleeptime)
    viewMoreTracks = driver.find_element('xpath', "//a[starts-with(@data-analytics,'viewMoreTracks-A')]")

    actions.move_to_element(viewMoreTracks).perform()
    time.sleep(sleeptime)
    viewMoreTracks.click()
    time.sleep(sleeptime)

    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.PAGE_DOWN)

    span2018 = driver.find_element('xpath', "//span[text()='re:Invent 2018']")
    actions.move_to_element(span2018).perform()

    span2018.click()

    time.sleep(sleeptime)

    startevaluatebutton=driver.find_element('xpath', "//span[text()='Start evaluation']")
    actions.move_to_element(startevaluatebutton).perform()
    time.sleep(sleeptime)
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(sleeptime)
    startevaluatebutton.click()
    time.sleep(20)



if __name__ == "__main__":

    for step in range(1,100):
        evaluate_deepracer(step)
        time.sleep(Run_Period * 60)
        current = time.ctime()
        print(f"{current} starting evaluate at {step} times...")





