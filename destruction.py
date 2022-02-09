from selenium import webdriver
import time

integer = 0
while integer < 100:

    driver = webdriver.Firefox()
    driver.get('https://plantle.netlify.app/')

    # dread myall botnt
    d = driver.find_element("xpath", "/html/body/div[4]/button[3]")
    r = driver.find_element("xpath", "/html/body/div[3]/button[4]")
    e = driver.find_element("xpath", "/html/body/div[3]/button[3]")
    a = driver.find_element("xpath", "/html/body/div[4]/button[1]")

    m = driver.find_element("xpath", "/html/body/div[5]/button[7]")
    y = driver.find_element("xpath", "/html/body/div[3]/button[6]")
    a = driver.find_element("xpath", "/html/body/div[4]/button[1]")
    l = driver.find_element("xpath", "/html/body/div[4]/button[9]")

    b = driver.find_element("xpath", "/html/body/div[5]/button[5]")
    o = driver.find_element("xpath", "/html/body/div[3]/button[9]")
    t = driver.find_element("xpath", "/html/body/div[3]/button[5]")
    n = driver.find_element("xpath", "/html/body/div[5]/button[6]")

    submit = driver.find_element("xpath", "/html/body/div[6]/button[1]")

    d.click()
    r.click()
    e.click()
    a.click()
    d.click()
    submit.click()
    time.sleep(1)

    m.click()
    y.click()
    a.click()
    l.click()
    l.click()
    submit.click()
    time.sleep(1)

    b.click()
    o.click()
    t.click()
    n.click()
    t.click()
    submit.click()
    time.sleep(1)

    driver.quit()

    integer += 1