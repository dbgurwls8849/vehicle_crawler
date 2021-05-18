from selenium import webdriver

chromedriver = 'C:/Users/lge/PycharmProjects/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://auto.naver.com/bike/mainList.nhn')


print(driver.title)
print(driver.current_url)
print("바이크 브랜드 크롤링")

bikeCompanyAllBtn = driver.find_element_by_css_selector("#container > div.spot_main > div.spot_aside > div.tit > a")
bikeCompanyAllBtn.click()

allBikeCompanyElement = driver.find_elements_by_css_selector("#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

for item in allBikeCompanyElement:
    bikeComName = item.find_element_by_tag_name("span").text
    if (bikeComName != ''):
        print("바이크 회사명:" + bikeComName)
        ahref = item.find_element_by_tag_name("a").get_attribute("href")
        print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
        imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
        print('바이크 회사 엠블럼:', imgUrl)


nextBtn = driver.find_element_by_css_selector("#_vendor_select_layer > div > div.maker_group > div.rolling_btn > button.next")


for i in range(1):
    print("다음 페이지 존재함=======================================>")
    nextBtn.click()
    allBikeCompanyElement = driver.find_elements_by_css_selector("#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")
    for item in allBikeCompanyElement:
        bikeComName = item.find_element_by_tag_name("span").text
        if (bikeComName != ''):
            print("바이크 회사명:" + bikeComName)
            ahref = item.find_element_by_tag_name("a").get_attribute("href")
            print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
            imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
            print('바이크 회사 엠블럼:', imgUrl)

def crawlingpage():
    allCarCompanyElement = driver.find_elements_by_css_selector("#_vendor_select_layer > div > div.maker_group > div.emblem_area > ul > li")
    for item in allCarCompanyElement:
        carComName = item.find_element_by_tag_name("span").text
        if (carComName != ''):
            print("자동차 회사명:" + carComName)
            ahref = item.find_element_by_tag_name("a").get_attribute("href")
            print('네이버 자동차 자동차제조사 홈 sub url:', ahref)
            imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
            print('자동차 회사 엠블럼:', imgUrl)

chromedriver = 'D:/Users/Master/PycharmProjects/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://auto.naver.com/car/mainList.nhn')

print(driver.title)
print(driver.current_url)

carCompanyAll = driver.find_element_by_css_selector("#container > div.spot_main > div.spot_aside > div.tit > a")
carCompanyAll.click()

next = driver.find_element_by_css_selector("#_vendor_select_layer > div > div.maker_group > div.rolling_btn > button.next")

crawlingpage()
for i in range(3):
    print("다음 페이지")
    next.click()
    crawlingpage()