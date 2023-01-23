import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import tkinter as tk
import webbrowser
import gc

def jump_to_link(url):
    webbrowser.open_new(url)

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
ChromeOptions.add_argument('--headless')

CHROMEDRIVER = "..\driver\chromedriver"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
chrome_service.creation_flags = CREATE_NO_WINDOW
driver1 = webdriver.Chrome(service=chrome_service,options=ChromeOptions)
str = "https://www.twitch.tv/kato_junichi0817"
driver1.get(str)
while True:
    time.sleep(5)
    try:
        element = driver1.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/p')
        elem = element.text
    except:
        element = driver1.find_element(By.XPATH,'//*[@id="live-channel-stream-information"]/div/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div')
        elem = element.text
    window = tk.Tk()
    window.geometry("500x300")
    if elem != "オフライン":
        window.title("加藤純一さんはオンラインです")
        canvas = tk.Canvas(width=510, height=200, background="#eee")
        canvas.place(x=-5, y=50)
        text = tk.Label(canvas, text="加藤純一さんの配信を見に行く")
        text.place(x=150, y=90, anchor=tk.NW)
        text.bind("<Button-1>", lambda e:jump_to_link("https://www.twitch.tv/kato_junichi0817"))
        driver1.quit()
        window.mainloop()
    del element
    del elem
    del window
    gc.collect()
    