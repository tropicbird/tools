'''
ディズニーのチケットを取る際にアクセスが多くて先に進めないときにひたすらページを更新するスクリプト
'''

from selenium import webdriver
import time
import tqdm

browser = webdriver.Chrome('C:/Users/hdais/Dropbox/github/kaggle-ranking/driver/chromedriver_win32' + '/chromedriver')
browser.get(f'https://reserve.tokyodisneyresort.jp/fo/index.html')

first_url = browser.current_url
print(first_url)
for i in tqdm.tqdm(range(3000)):
    # print(i)
    #ページを更新(ブラウザのリフレッシュ)
    browser.refresh()
    time.sleep(1)
    current_url = browser.current_url
    if first_url != current_url:
        print('入れた！')
        break
print('終わり')