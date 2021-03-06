#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-30 15:16:10
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def getGift(roomid):
    fp = webdriver.FirefoxProfile(
        r'/Users/eclipse/Library/Application Support/Firefox/Profiles/tmsbsjpg.default')
    browser = webdriver.Firefox(fp)
    browser.implicitly_wait(15)  # seconds
    browser.get("http://www.douyu.com/" + roomid)
    try:
        indexvideo = browser.find_element_by_class_name('cs-textarea')
        print type(indexvideo)
        indexvideo.send_keys('2333333333333')
        print indexvideo
        time.sleep(5)
        sendbut = browser.find_element_by_class_name('b-btn')
        ActionChains(browser).move_to_element(
            indexvideo).click(sendbut).perform()
        gift = browser.find_element_by_class_name('peck-cdn')
    except Exception, e:
        print str(e)
        browser.quit()

    times = 0
    while True:
        try:
            ActionChains(browser).move_to_element(gift).click(gift).perform()
            time.sleep(1)
            print times
            times += 1
        except Exception, e:
            print 'completed by an error'
            browser.quit()
