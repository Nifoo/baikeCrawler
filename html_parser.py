# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:42:52 2017

@author: PENG
"""
import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print 'page_url is none or html_cont is none'
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
        
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # url格式为 /view/任意位数字.htm
        links = soup.find_all('a', href=re.compile(r"/item/"))
        #print links
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url) 
            #urlparse.urljoin(base, url[, allow_fragments])
            #urljoin主要是拼接URL，它以base作为其基地址，然后与url中的相对地址相结合组成一个
            #绝对URL地址。如果基地址并非以字符/结尾的话，那么URL基地址最右边部分就会被这个相
            #对路径所替换。如果希望在该路径中保留末端目录，应确保URL基地址以字符/结尾。
            # print page_url, new_url, new_full_url
            new_urls.add(new_full_url)
        return new_urls
        
    def _get_new_data(self, page_url, soup):
        # 对于每个页面只提取title和summary
        res_data = {}        
        res_data['url'] =  page_url
        
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data