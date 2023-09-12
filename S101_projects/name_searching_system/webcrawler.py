"""
File: webcrawler.py
Name: Jeff Tsai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        # print(response)
        tags = soup.find_all('table', {'class', 't-stripe'})
        m_count = f_count = 0
        for tag in tags:
            targets = tag.tbody.text
            targets = targets.split()
            # print(targets)
            for i in range(len(targets)-22):
                if i % 5 == 2:
                    m_count += int(targets[i].replace(",", ""))  # '194,917' -> '194917'
                elif i % 5 == 4:
                    f_count += int(targets[i].replace(",", ""))
        print(f'Male Number: {str(m_count)}')
        print(f'Female Number: {str(f_count)}')
        # for tag in tags:
        #     targets = tag.tbody.text
        #     l =[]
        #     for line in targets:  # clean out data
        #         if not line == '\n':
        #             if not line == ' ':
        #                 l.append(line)
        #     num = ''
        #     n_list = []
        #     loop = 0
        #     for i in range(len(l)):
        #         if l[i].isalpha():
        #             if num != '':
        #                 loop += 1
        #                 if loop < 18:  # rank 1-9
        #                     correction = 1
        #                 elif 18 <= loop < 198:   # rank 10-99
        #                     correction = 2
        #                 elif 198 <= loop < 400:  # rank 100-199
        #                     correction = 3
        #                 elif loop == 401:  # rank 200
        #                     correction = 1
        #                 elif loop > 401:  # stop loop while completed
        #                     break
        #                 if loop % 2 == 1:
        #                     if loop == 1:
        #                         num = ''
        #                     else:
        #                         n_list.append(num[:-correction])  # female data needs correction
        #                         num = ''
        #                 else:
        #                     n_list.append(num)  # male data
        #                     num = ''
        #         else:
        #             if l[i] != ',':
        #                 num += l[i]
        #     m_list = 0
        #     f_list = 0
        #     for i in range(len(n_list)):
        #         if i % 2 == 1:  # female
        #             f_list += int(n_list[i])
        #         else:  # male
        #             m_list += int(n_list[i])
        #     print(f'Male Number: {str(m_list)}')
        #     print(f'Female Number: {str(f_list)}')



if __name__ == '__main__':
    main()
