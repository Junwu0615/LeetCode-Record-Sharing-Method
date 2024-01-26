import os
import requests
import numpy as np
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from PIL import ImageFont, ImageDraw, Image

def parse_args():
    parse = ArgumentParser()
    parse.add_argument("-i", "--userid", help = "give a LeetCode user-id.", default = "user0190Nh", type = str)
    parse.add_argument("-n", "--username", help = "give your name.", default = "Ping Chun", type = str)
    parse.add_argument("-f", "--font", help = "give a font type.", default = "AniMeMatrix-MB_EN.ttf", type = str)
    parse.add_argument("-bc", "--bgcolor", help = "give a background color.", default = "#FFFFFF", type = str)
    parse.add_argument("-fc", "--fontcolor", help = "give a font color.", default = "64,64,64", type = str)
    parse.add_argument("-p", "--customizepath", help = "If you want to customize the picture, please give the path.", default = "None", type = str)
    args = parse.parse_args()
    return args

def customize_img(customize_path, img_size):
    img = Image.open(customize_path)
    bg_img = img.resize(img_size, Image.BILINEAR)
    return bg_img, "external_img"

def simple_bg(bg_color, img_size):
    bg_img = Image.new("RGBA", img_size, bg_color)
    return bg_img, "simple_bg"

def gif(img):
    gif = np.array(img)
    gif = Image.fromarray(gif)
    gif = gif.convert('RGB')
    return gif

def fine_tuning_word(word, i):
    # 字母不曉得為什麼會跑版，只能強制微調
    if word == "i": i -= 0.5 
    elif word == " ": i -= 0.4
    elif word == ",": i -= 0.6
    elif word == "1": i -= 0.3
    elif word == ".": i -= 0.6
    elif word == "l": i -= 0.3
    return i
    
if __name__ == "__main__":
    args = parse_args()
    user_id = args.userid
    user_name = args.username
    img_size = (450, 220)
    bg_color = args.bgcolor #282A36 #404040 #FFFFFF #404040
    temp_color = args.fontcolor
    temp = temp_color.split(",")
    font_color = (int(temp[0]),int(temp[1]),int(temp[2]))
    customize_path = args.customizepath
    logo = "./LeetCode_Logo/LeetCode_bbg_fw.png" # LeetCode_bbg_fw.png | LeetCode_bbg.png | LeetCode_wbg.png
    font_style = f"C:/Windows/Fonts/{args.font}"   # georgiab.ttf | MATURASC.TTF | MAGNETOB.TTF | AniMeMatrix-MB_EN.ttf
    url = f"https://leetcode.com/{user_id}/"
    save_path = "./sample_img/"
    folder = os.path.exists(save_path)
    if not folder: os.makedirs(save_path)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    dict_={ "Eazy": [], "Medium": [], "Hard": [], "Level": [], "Rank": []}
    for i, j in zip(soup.find_all('span', {'class':'mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1'}), dict_.keys()):
        dict_[j].append(i.text)
    for i, j in zip(soup.find_all('span', {'class':'text-xs font-medium text-label-4 dark:text-dark-label-4'}), dict_.keys()):
        dict_[j].append(i.text[1:])
    for i in soup.find_all('div', {'class':'text-[24px] font-medium text-label-1 dark:text-dark-label-1'}):
        dict_["Level"].append(i.text)
    for i in soup.find_all('span', {'class':'ttext-label-1 dark:text-dark-label-1 font-medium'}):
        dict_["Rank"].append(i.text)
        
    count = 0
    content_list = []
    for i, j in dict_.items():
        content_list.append(f"{i} : {j[0]} / {j[1]}")
        if count == 2: break
        count += 1
        
    if bg_color != "None": bg_img, type_name = simple_bg(bg_color, img_size)
    else: bg_img, type_name = customize_img(customize_path, img_size)
    
    img_list = [] # gif 動圖清單
    draw_text = ImageDraw.Draw(bg_img)
    
    # LOGO
    logo = Image.open(logo).convert('RGBA')
    logo = logo.resize((100, 22), Image.BILINEAR)
    bg_img.paste(logo,(10, 10), logo)  #(450,220)
    
    for i in range(5): img_list.append(gif(bg_img)) # gif 開頭緩衝時間
    
    # 遍歷"使用者和排名"
    i = 0
    rank_w = f"{user_name} / Rank {dict_['Rank'][0]}"
    font = ImageFont.truetype(font_style, size=18)
    for word in rank_w:
        move = 16 * i
        draw_text.text((bg_img.size[0]/16+move, 50), word, font=font, fill=font_color)
        img_list.append(gif(bg_img))
        i = fine_tuning_word(word, i)
        i += 1
        
    # 遍歷"解決問題數"
    i = 0
    j = 0
    count = 0
    level_w = f"Solved{dict_['Level'][0]}"
    font = ImageFont.truetype(font_style, size=17)
    for word in level_w:
        if count <= 5:
            move = 16 * i
            draw_text.text((bg_img.size[0]/10.5+move, bg_img.size[1]/2.5), word, font=font, fill=font_color)
            i += 1
        else:
            move = 16 * j
            draw_text.text((bg_img.size[0]/7.5+move, bg_img.size[1]/1.9), word, font=font, fill=font_color)
            j += 1
        img_list.append(gif(bg_img))
        i = fine_tuning_word(word, i)
        count += 1
        
    # 遍歷"解決問題難易度統計"
    count = 0
    font = ImageFont.truetype(font_style, size=17)
    for content in content_list:
        i = 0
        for word in content:
            move = 16 * i
            if count == 0: draw_text.text((bg_img.size[0]/3+move, bg_img.size[1]/2.5), word, font=font, fill=font_color)
            elif count == 1: draw_text.text((bg_img.size[0]/3+move, bg_img.size[1]/1.9), word, font=font, fill=font_color)
            elif count == 2: draw_text.text((bg_img.size[0]/3+move, bg_img.size[1]/1.5), word, font=font, fill=font_color)
            img_list.append(gif(bg_img))
            i = fine_tuning_word(word, i)
            i += 1
        count += 1
    
    i = 0
    author = "Author:github.com/Junwu0615"
    font = ImageFont.truetype(font_style, size=10)
    for word in author:
        move = 10 * i
        draw_text.text((bg_img.size[0]/2.5+move, bg_img.size[1]/1.1), word, font=font, fill=font_color)
        img_list.append(gif(bg_img))
        i = fine_tuning_word(word, i)
        i += 1
    
    for i in range(20): img_list.append(gif(bg_img)) # gif 結尾停留時間久點
    bg_img.save(save_path+f"{user_name}_leetcode_{type_name}.png")
    img_list[0].save(save_path+f"{user_name}_leetcode_{type_name}.gif", save_all=True, append_images=img_list[1:], duration=60, loop=0, disposal=0)