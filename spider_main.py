# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:41:50 2017

@author: PENG
"""
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() # url管理器 管理2个集合 分别存放已抓取的url和待抓取的url
        # 提供4个方法：has_new_url, get_new_url, add_new_url, add_new_urls 
        self.downloader = html_downloader.HtmlDownloader() #下载器
        # 提供 1个方法download(url): 给定url返回字符串
        self.parser = html_parser.HtmlParser() # html页面解析器
        # 提供1个方法parse(new_url, html_cont) 返回页面解析得到的urls和data
        self.outputer = html_outputer.HtmlOutputer() # 输出器
        # 提供2个方法 collect(data) 来添加数据到最终结果， output_html()将最终结果输出到html文件
    
    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1;
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'crawl %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if(count == 100):
                    break
                count = count + 1
            except:
                print 'crawl failed'
        self.outputer.output_html()
  
  
if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)