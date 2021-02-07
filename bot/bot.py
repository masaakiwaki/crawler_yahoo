from selenium import webdriver
from bs4 import BeautifulSoup
import os.path
import datetime
import pytz
import csv


# create file_name (now data,time)
def File_Name(output_name):
    dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    fdt_now = dt_now.strftime('%Y%m%d%H%M%S')
    file_name = os.path.join(os.path.dirname(os.path.abspath('__file__')), (fdt_now + "_" + output_name))
    return file_name


def Scraping():
    # webdirver config (colaboratory only)
    drivepath = os.path.join(os.path.dirname(os.path.abspath('__file__')), ('chromedriver.exe'))
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(drivepath, options=options)
    driver.get("https://www.yahoo.co.jp/")

    # screen capture
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    capture_name = File_Name('screen.png')
    driver.save_screenshot(capture_name)

    # get HTML
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')

    # yahoo news extract
    links = soup.select('a[href^="https://news.yahoo.co.jp/pickup/"]')

    # news list creale
    news_list = [["title","url"]]
    for link in links:
      news_url = link.get("href")
      link = link.select("span")
      news_title = (link[0].text)
      news_list.append([news_title,news_url])
    news_list

    # webdirver quit
    driver.quit()

    # csv create new file
    csv_name = File_Name('news.csv')
    f = open(csv_name, "w")
    writecsv = csv.writer(f, lineterminator='\n')

    # output
    writecsv.writerows(news_list)

    # csv create close
    f.close()

    return news_list, capture_name, csv_name



if __name__ == "__main__":
    main()


