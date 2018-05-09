# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:43:05 2017

@author: PENG
"""
import urllib2

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            #print "url is none"
            return None
        response = urllib2.urlopen(url)
        if response.getcode()!=200:
            #print "response is none"
            return None
        tmpstr = response.read()
        #print tmpstr
        return tmpstr