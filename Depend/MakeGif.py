# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""

import os, json
import requests
import numpy as np
from bs4 import BeautifulSoup
from PIL import ImageFont, ImageDraw, Image

class MakeGif:
    def __init__(self, obj):
        self.userid = obj.userid
        self.username = obj.username
        self.font = obj.font
        self.bg_color = obj.bg_color # 282A36 #404040 #FFFFFF #404040
        self.font_color = obj.font_color
        self.font_shadow = obj.font_shadow
        self.customize_path = obj.customize_path

        temp = self.font_color.split(",")
        self.font_color = (int(temp[0]), int(temp[1]), int(temp[2]))
        temp = self.font_shadow.split(",")
        self.font_shadow = (int(temp[0]), int(temp[1]), int(temp[2]))

        self.img_size = (450, 220)
        self.save_path = "./Sample/"

        # LeetCode_bbg_fw.png | LeetCode_bbg.png | LeetCode_wbg.png
        self.logo = "./Depend/Logo/LeetCode_bbg_fw.png"

        # georgiab.ttf | MATURASC.TTF | MAGNETOB.TTF | AniMeMatrix-MB_EN.ttf
        self.font_style = f"C:/Windows/Fonts/{self.font}"

        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def check_folder(self, path: str):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    def customize_img(self) -> tuple:
        img = Image.open(self.customize_path)
        bg_img = img.resize(self.img_size, Image.BILINEAR)
        return bg_img, "external_img"

    def simple_bg(self) -> tuple:
        bg_img = Image.new("RGBA", self.img_size, self.bg_color)
        return bg_img, "simple_bg"

    def array_to_img(self, img) -> Image:
        return Image.fromarray(np.array(img)).convert('RGB')

    def fine_tuning_word(self, word, i) -> int:
        if word == "i":i -= 0.5
        elif word == " ":i -= 0.4
        elif word == ",":i -= 0.6
        elif word == "1":i -= 0.3
        elif word == ".":i -= 0.6
        elif word == "l":i -= 0.3
        elif word == "m":i += 0.2
        elif word == "w": i += 0.2
        elif word == "u": i += 0.2
        return i

    def get_source(self) -> dict:
        # Solved Problem
        payload = {
            'operationName':  'userSessionProgress',
            'query':  '\n    query userSessionProgress($username: String!) '
                      '{\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  '
                      'matchedUser(username: $username) {\n    submitStats {\n      acSubmissionNum '
                      '{\n        difficulty\n        count\n        submissions\n      }\n      '
                      'totalSubmissionNum {\n        difficulty\n        count\n        '
                      'submissions\n      }\n    }\n  }\n}\n    ',
            'variables':  {'username': self.userid},

        }
        ret_dict = {}
        url = 'https://leetcode.com/graphql/'
        res = requests.post(url, json=payload, headers=self.headers)
        loader = json.loads(res.text)
        for i in loader['data']['allQuestionsCount']:
            if i['difficulty'] not in ret_dict:
                ret_dict[i['difficulty']] = [None, i['count']]

        for i in loader['data']['matchedUser']['submitStats']['acSubmissionNum']:
            if i['difficulty'] in ret_dict:
                ret_dict[i['difficulty']][0] = i['count']

        # Rank
        payload['operationName'] = "userPublicProfile"
        payload['query'] = ("\n    query userPublicProfile($username: String!) {\n  matchedUser(username: $username) "
                            "{\n    contestBadge {\n      name\n      expired\n      hoverText\n      icon\n    }\n    "
                            "username\n    githubUrl\n    twitterUrl\n    linkedinUrl\n    profile {\n      ranking\n      "
                            "userAvatar\n      realName\n      aboutMe\n      school\n      websites\n      countryName\n      "
                            "company\n      jobTitle\n      skillTags\n      postViewCount\n      postViewCountDiff\n      "
                            "reputation\n      reputationDiff\n      solutionCount\n      solutionCountDiff\n      "
                            "categoryDiscussCount\n      categoryDiscussCountDiff\n    }\n  }\n}\n    ")
        res = requests.post(url, json=payload, headers=self.headers)
        loader = json.loads(res.text)
        ret_dict['Rank'] = loader['data']['matchedUser']['profile']['ranking']

        return ret_dict

    def draw_gif(self, ret_dict: dict):
        content_list, progress_bar, img_list = [], [], []
        for k, v in ret_dict.items():
            if k not in ['All', 'Rank']:
                content_list.append(f"{k} : {v[0]} / {v[1]}")
                progress_bar.append([str(round(int(v[0]) / int(v[1]) * 100, 2)) + "%"])

        count = 0
        for i in progress_bar:
            character = ''
            for j in range(int(float(i[0][:-1]) / 10)):
                character += ">>"
            for j in range(10 - int(float(i[0][:-1]) / 10)):
                character += "--"
            progress_bar[count].append(character)
            temp = progress_bar[count][0]
            progress_bar[count][0] = progress_bar[count][1]
            progress_bar[count][1] = temp
            if len(progress_bar[count][1]) == 4:
                progress_bar[count][1] = progress_bar[count][1][:-1] + "0%"
            if len(progress_bar[count][1]) == 3:
                progress_bar[count][1] = progress_bar[count][1][:-1] + "00%"
            progress_bar[count][0] = ">" + progress_bar[count][0] + " " + progress_bar[count][1]
            progress_bar[count][1] = ''
            count += 1

        if self.bg_color != "None":
            bg_img, type_name = self.simple_bg()
        else:
            bg_img, type_name = self.customize_img()

        draw_text = ImageDraw.Draw(bg_img)

        # LOGO
        logo = Image.open(self.logo).convert('RGBA')
        logo = logo.resize((100, 22), Image.BILINEAR)
        bg_img.paste(logo, (10, 10), logo)  # (450,220)

        # gif 開頭緩衝時間
        for i in range(5):
            img_list.append(self.array_to_img(bg_img))

        # 遍歷"使用者和排名"
        i = 0
        rank_w = f"{self.username} / Rank {ret_dict['Rank']}"
        font = ImageFont.truetype(self.font_style, size=18)
        for word in rank_w:
            move = 16 * i
            draw_text.text((bg_img.size[0] / 15.9 + move, 51), word,
                           font=ImageFont.truetype(self.font_style, size=20), fill=self.font_shadow)
            draw_text.text((bg_img.size[0] / 16 + move, 50), word,
                           font=font, fill=self.font_color)
            img_list.append(self.array_to_img(bg_img))
            i = self.fine_tuning_word(word, i)
            i += 1

        # 遍歷"解決問題數"
        i, j, count = 0, 0, 0
        level_w = f"Solved{ret_dict['All'][0]}"
        font = ImageFont.truetype(self.font_style, size=17)
        for word in level_w:
            if count <= 5:
                move = 16 * i
                draw_text.text((bg_img.size[0] / 10.4 + move, bg_img.size[1] / 2.5 + 1), word,
                               font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                draw_text.text((bg_img.size[0] / 10.5 + move, bg_img.size[1] / 2.5), word,
                               font=font, fill=self.font_color)
                i += 1
            else:
                move = 16 * j
                draw_text.text((bg_img.size[0] / 7.4 + move, bg_img.size[1] / 1.9 + 1), word,
                               font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                draw_text.text((bg_img.size[0] / 7.5 + move, bg_img.size[1] / 1.9), word,
                               font=font, fill=self.font_color)
                j += 1
            img_list.append(self.array_to_img(bg_img))
            i = self.fine_tuning_word(word, i)
            count += 1

        # 遍歷"解決問題難易度統計"
        count = 0
        font = ImageFont.truetype(self.font_style, size=17)
        for content in content_list:
            i = 0
            for word in content:
                move = 16 * i
                if count == 0:
                    draw_text.text((bg_img.size[0] / 2.99 + move, bg_img.size[1] / 2.5 + 1), word,
                                   font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                    draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 2.5), word,
                                   font=font, fill=self.font_color)
                elif count == 1:
                    draw_text.text((bg_img.size[0] / 2.99 + move, bg_img.size[1] / 1.65 + 1), word,
                                   font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                    draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.65), word,
                                   font=font, fill=self.font_color)
                elif count == 2:
                    draw_text.text((bg_img.size[0] / 2.99 + move, bg_img.size[1] / 1.25 + 1), word,
                                   font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                    draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.25), word,
                                   font=font, fill=self.font_color)
                img_list.append(self.array_to_img(bg_img))
                i = self.fine_tuning_word(word, i)
                i += 1
            count += 1
        i = 0
        font = ImageFont.truetype(self.font_style, size=10)
        for content1, content2, content3 in zip(progress_bar[0], progress_bar[1], progress_bar[2]):
            for w1, w2, w3 in zip(content1, content2, content3):
                move = 9 * i
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 2.5 + 25), w1,
                               font=font, fill=(0, 202, 202))
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.65 + 25), w2,
                               font=font, fill=(255, 211, 6))
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.25 + 25), w3,
                               font=font, fill=(234, 0, 0))
                if i < 10 * 2:
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 2.5 + 25), w1,
                                   font=font, fill=(0, 202, 202))
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 1.65 + 25), w2,
                                   font=font, fill=(255, 211, 6))
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 1.25 + 25), w3,
                                   font=font, fill=(234, 0, 0))
                img_list.append(self.array_to_img(bg_img))
                i = self.fine_tuning_word(w1, i)
                i += 1

        # gif 結尾停留時間久點
        for i in range(20):
            img_list.append(self.array_to_img(bg_img))

        # bg_img.save(save_path+f"{user_name}_leetcode_{type_name}.png")
        img_list[0].save(self.save_path + f"{self.username}_leetcode_{type_name}.gif",
                         save_all=True, append_images=img_list[1:],
                         duration=60, loop=1, disposal=0)

    def main(self):
        ret_dict = self.get_source()
        self.draw_gif(ret_dict)