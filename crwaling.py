import os
import re

import requests
from bs4 import BeautifulSoup


class Notice:
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    SAVE_PATH = os.path.join(ROOT_PATH, 'saved_data')

    def __init__(self):
        self._notice_list = {}
        # 초기화 함수에서 저장 폴더를 만들어줌
        os.makedirs(self.SAVE_PATH, exist_ok=True)

    def get_html(self):
        root= os.path.dirname(os.path.abspath(__file__))
        dir_path= os.path.join(root, 'saved_data')
        file_path = os.path.join(dir_path, 'test_crawling.html')

        if os.path.exists(file_path):
            html = open(file_path, 'rt').read()
        else:
            response = requests.get('http://www.leagueoflegends.co.kr/?m=news&cate=notice')
            html = response.text
            open(file_path, 'wt').write(html)
        return html


