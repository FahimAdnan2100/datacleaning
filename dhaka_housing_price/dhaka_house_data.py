# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 04:22:23 2021

@author: fahim
"""

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.bdhousing.com/homes/listings/Dhaka?buy_sale_rommate=Sale&city=1&property_type=all_residential')
print(html_text)
soup = BeautifulSoup(html_text, 'lxml')

location = soup.find('i', class_ = 'glyphicon glyphicon-map-marker')



print(f'''
      
      Location: {location}
      ''')

