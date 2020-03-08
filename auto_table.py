"""
有任何问题请联系QQ：321004240 ————酷酷的学长
针对JXUT疫情表单的自动化填写
请勿商用，仅供学习之用
"""

import time
from selenium import webdriver
from PIL import Image
import pytesseract
import datetime

driver = webdriver.Chrome()  # 选择Chrome浏览器
driver.get('')  # 打开网站
driver.maximize_window()  # 最大化谷歌浏览器

# time.sleep(1)

username = ""  # 请替换成你的用户名
password = ""  # 请替换成你的密码

driver.find_element_by_id('username_text').send_keys(username)  # 自动敲入用户名
driver.find_element_by_id('password_text').send_keys(password)  # 自动敲入密码

driver.save_screenshot("")
imgeLement = driver.find_element_by_xpath('//*[@id="codeimg"]')  # 定位验证码
location = imgeLement.location  # 获取验证码x,y轴坐标
size = imgeLement.size  # 获取验证码的长宽
rangle = (int(location["x"] * 2), int(location["y"] * 2), int(location["x"] * 2 + size["width"] * 2),
          int(location["y"] * 2 + size["height"] * 2))  # 写成需要截取的位置坐标

i = Image.open("")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取需要的区域
frame4.save("")   #图片保存路径
qq = Image.open("")  #图片的保存路径

text = pytesseract.image_to_string(qq).strip()  # 使用image_to_string识别验证码
print(text)  # 打印出验证码

driver.find_element_by_id('code').send_keys(text)

# 采用class定位登陆按钮
# driver.find_element_by_class_name('ant-btn').click() # 点击“登录”按钮
# 采用xpath定位登陆按钮，
driver.find_element_by_xpath('//*[@id="fm1"]/span/input').click()
time.sleep(3)
# driver.close()


# 表单需求
tel = ''  # 1.手机电话
province = ''  # 3.省份
city = ''  # 4.市
countryside = ''  # 5.县
coum = '无'

d1 = datetime.datetime(2020, 2, 24)  # 要求包含当天，自动向前取一天
d2 = datetime.datetime.now()
lag = d2 - d1  # 时间差
# days =lag.days

# 疫情表单填写
# 电话
driver.find_element_by_name('4e9aa5d327284de1a99377b89c4c8d9e').send_keys(tel)

# 使用xpath定位选框位置，并点击 （是否居住学校-否）
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[8]/div[2]/div/label[2]').click()

# 所在省
driver.find_element_by_name('12a82fa4b92842cabdff862915f55b92').send_keys(province)

# 所在市
driver.find_element_by_name('a885d5bf990149408036f2110d0972bf').send_keys(city)

# 所在县
driver.find_element_by_name('c0a2fa6ac0c549b187528adfab6658e2').send_keys(countryside)

# 6.居住位置省市与昨日对比有无变化
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[12]/div[2]/div/label[2]').click()

# 7.居住变化情况
driver.find_element_by_name('5f9d72403beb4b4f86509633c08e471f').send_keys(coum)

# 8.今日体温  健康
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[14]/div[2]/div/label[1]').click()

# 9.今日是否在校  否
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[15]/div[2]/div/label[2]').click()

# 10.今日是否返校
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[16]/div[2]/div/label[2]').click()

# 11.今日返校原因  无
driver.find_element_by_name('fc7a75f9e0d448fc8a967226f0c4682f').send_keys(coum)

# 12.今日离校原因  无
driver.find_element_by_name('b47611fc7c794a8186a716e4dddea193').send_keys(coum)

# 13.今日返昌情况  无
driver.find_element_by_name('465f59b24ec84d389d5da23b349e2573').send_keys(coum)

# 14.今日返昌居住何区、镇或街道   无
driver.find_element_by_name('25fa44ea3ad646dfa2f12d377a825cdc').send_keys(coum)

# 15.返校情况  无
driver.find_element_by_name('20eaa9fea2b74b11adaa82a1d87ceb8e').send_keys(coum)

# 16.今日本人身体状况  健康
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[22]/div[2]/div/label[1]').click()

# 17.本人病情  无
driver.find_element_by_name('b4c89b9988d44e25b4f8bba6a823a3e4').send_keys(coum)

# 18.发热开始日期  无
driver.find_element_by_name('c6b1184ac9314b968432e7c290db35e2').send_keys(coum)

# 19.连续健康天数
driver.find_element_by_name('80c2cf554d094d0bb07b318973081603').send_keys(lag.days)

# 20.今日家庭成员或亲属的身体状况  健康
driver.find_element_by_xpath('//*[@id="wjdc__form"]/div[26]/div[2]/div/label[1]').click()

# 21.家庭成员或亲属的病情  无
driver.find_element_by_name('c6134b8da6d04aeb8d0f271d769f972c').send_keys(coum)

