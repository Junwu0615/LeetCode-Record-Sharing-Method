# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
import os, json, requests
import numpy as np
from rich.console import Console
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
        temp = self.font_color.split(',')
        self.font_color = (int(temp[0]), int(temp[1]), int(temp[2]))
        temp = self.font_shadow.split(',')
        self.font_shadow = (int(temp[0]), int(temp[1]), int(temp[2]))
        self.logo = './package/Logo/LeetCode_bbg_fw.png' # LeetCode_bbg_fw.png | LeetCode_bbg.png | LeetCode_wbg.png
        self.font_style = f'C:/Windows/Fonts/{self.font}' # georgiab.ttf | MATURASC.TTF | MAGNETOB.TTF | AniMeMatrix-MB_EN.ttf
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.img_size = (450, 220)
        self.save_path = './sample'
        self.console = Console()

    @staticmethod
    def check_folder(path: str):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    @staticmethod
    def array_to_img(img) -> Image:
        return Image.fromarray(np.array(img)).convert('RGB')

    @staticmethod
    def fine_tuning_word(word, idx) -> int:
        if word == 'i': return idx - 0.5
        elif word == ' ': return idx - 0.4
        elif word == ',': return idx - 0.6
        elif word == '1': return idx - 0.3
        elif word == '.': return idx - 0.6
        elif word == 'l': return idx - 0.3
        elif word == 'm': return idx + 0.2
        elif word == 'w': return idx + 0.2
        elif word == 'u': return idx + 0.2
        else: return idx

    @staticmethod
    def customize_bg(img_size: tuple[int, int], customize_path: str) -> tuple:
        img = Image.open(customize_path)
        bg_img = img.resize(img_size, Image.BILINEAR)
        return bg_img, 'customize'

    @staticmethod
    def simple_bg(img_size: tuple[int, int], bg_color: str) -> tuple:
        bg_img = Image.new('RGBA', img_size, bg_color)
        return bg_img, 'simple'

    @staticmethod
    def get_source(headers, userid) -> dict:
        # Solved Problem
        payload = {
            'operationName':  'userSessionProgress',
            'query':  '\n    query userSessionProgress($username: String!) '
                      '{\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  '
                      'matchedUser(username: $username) {\n    submitStats {\n      acSubmissionNum '
                      '{\n        difficulty\n        count\n        submissions\n      }\n      '
                      'totalSubmissionNum {\n        difficulty\n        count\n        '
                      'submissions\n      }\n    }\n  }\n}\n    ',
            'variables':  {'username': userid},

        }
        ret_dict = {}
        url = 'https://leetcode.com/graphql/'
        res = requests.post(url, json=payload, headers=headers)
        loader = json.loads(res.text)
        for idx in loader['data']['allQuestionsCount']:
            if idx['difficulty'] not in ret_dict:
                ret_dict[idx['difficulty']] = [None, idx['count']]

        for idx in loader['data']['matchedUser']['submitStats']['acSubmissionNum']:
            if idx['difficulty'] in ret_dict:
                ret_dict[idx['difficulty']][0] = idx['count']

        # Rank
        payload['operationName'] = 'userPublicProfile'
        payload['query'] = ('\n    query userPublicProfile($username: String!) {\n  matchedUser(username: $username) '
                            '{\n    contestBadge {\n      name\n      expired\n      hoverText\n      '
                            'icon\n    }\n    username\n    githubUrl\n    twitterUrl\n    linkedinUrl\n    '
                            'profile {\n      ranking\n      userAvatar\n      realName\n      aboutMe\n      school\n'
                            '      websites\n      countryName\n      company\n      jobTitle\n      skillTags\n      '
                            'postViewCount\n      postViewCountDiff\n      reputation\n      reputationDiff\n      '
                            'solutionCount\n      solutionCountDiff\n      '
                            'categoryDiscussCount\n      categoryDiscussCountDiff\n    }\n  }\n}\n    ')
        res = requests.post(url, json=payload, headers=headers)
        loader = json.loads(res.text)
        ret_dict['Rank'] = loader['data']['matchedUser']['profile']['ranking']
        return ret_dict

    def progress_bar(self, title: str):
        match title:
            case 'args':
                self.console.print(f"Get Parameter ...")
                self.console.print(f"Get User ID: {self.userid}")
                self.console.print(f"Get User Name: {self.username}")
                self.console.print(f"Get Font: {self.font}")
                self.console.print(f"Get Font Color: {self.font_color}")
                self.console.print(f"Get Font Shadow: {self.font_shadow}")
                self.console.print(f"Get Back Ground Color: {self.bg_color}")
                self.console.print(f"Get Customize Path: {self.customize_path}")
            case 'done':
                self.console.print(f'Making GIF Finish ! -> {self.save_path}')

    def draw_gif(self, ret_dict: dict):
        content_list, progress_bar, img_list = [], [], []
        for k, v in ret_dict.items():
            if k not in ['All', 'Rank']:
                content_list.append(f'{k} : {v[0]} / {v[1]}')
                progress_bar.append([str(round(int(v[0]) / int(v[1]) * 100, 2)) + '%'])

        count = 0
        for idx in progress_bar:
            character = ''
            character += ''.join(['>>' for _ in range(int(float(idx[0][:-1]) / 10))])
            character += ''.join(['--' for _ in range(10 - int(float(idx[0][:-1]) / 10))])

            progress_bar[count].append(character)
            temp = progress_bar[count][0]
            progress_bar[count][0] = progress_bar[count][1]
            progress_bar[count][1] = temp
            if len(progress_bar[count][1]) == 4:
                progress_bar[count][1] = progress_bar[count][1][:-1] + '0%'
            if len(progress_bar[count][1]) == 3:
                progress_bar[count][1] = progress_bar[count][1][:-1] + '00%'
            progress_bar[count][0] = '>' + progress_bar[count][0] + ' ' + progress_bar[count][1]
            progress_bar[count][1] = ''
            count += 1

        if self.bg_color != 'None':
            bg_img, type_name = MakeGif.simple_bg(self.img_size, self.bg_color)
        else:
            bg_img, type_name = MakeGif.customize_bg(self.img_size, self.customize_path)

        draw_text = ImageDraw.Draw(bg_img)

        # FIXME LOGO
        logo = Image.open(self.logo).convert('RGBA')
        logo = logo.resize((100, 22), Image.BILINEAR)
        bg_img.paste(logo, (10, 10), logo)  # (450,220)

        # FIXME gif 開頭緩衝時間
        img_list += [MakeGif.array_to_img(bg_img) for idx in range(5)]

        # FIXME 遍歷'使用者和排名'
        idx = 0
        rank_w = f"{self.username} / Rank {ret_dict['Rank']}"
        font = ImageFont.truetype(self.font_style, size=18)
        for word in rank_w:
            move = 16 * idx
            draw_text.text((bg_img.size[0] / 15.9 + move, 51), word,
                           font=ImageFont.truetype(self.font_style, size=20), fill=self.font_shadow)
            draw_text.text((bg_img.size[0] / 16 + move, 50), word,
                           font=font, fill=self.font_color)
            img_list.append(MakeGif.array_to_img(bg_img))
            idx = MakeGif.fine_tuning_word(word, idx)
            idx += 1

        # FIXME 遍歷'解決問題數'
        idx, idx2, count = 0, 0, 0
        level_w = f"Solved{ret_dict['All'][0]}"
        font = ImageFont.truetype(self.font_style, size=17)
        for word in level_w:
            if count <= 5:
                move = 16 * idx
                draw_text.text((bg_img.size[0] / 10.4 + move, bg_img.size[1] / 2.5 + 1), word,
                               font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                draw_text.text((bg_img.size[0] / 10.5 + move, bg_img.size[1] / 2.5), word,
                               font=font, fill=self.font_color)
                idx += 1
            else:
                move = 16 * idx2
                draw_text.text((bg_img.size[0] / 7.4 + move, bg_img.size[1] / 1.9 + 1), word,
                               font=ImageFont.truetype(self.font_style, size=19), fill=self.font_shadow)
                draw_text.text((bg_img.size[0] / 7.5 + move, bg_img.size[1] / 1.9), word,
                               font=font, fill=self.font_color)
                idx2 += 1
            img_list.append(MakeGif.array_to_img(bg_img))
            idx = MakeGif.fine_tuning_word(word, idx)
            count += 1

        # FIXME 遍歷'解決問題難易度統計'
        count = 0
        font = ImageFont.truetype(self.font_style, size=17)
        for content in content_list:
            idx = 0
            for word in content:
                move = 16 * idx
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
                img_list.append(MakeGif.array_to_img(bg_img))
                idx = MakeGif.fine_tuning_word(word, idx)
                idx += 1
            count += 1

        idx = 0
        font = ImageFont.truetype(self.font_style, size=10)
        for content1, content2, content3 in zip(progress_bar[0], progress_bar[1], progress_bar[2]):
            for w1, w2, w3 in zip(content1, content2, content3):
                move = 9 * idx
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 2.5 + 25), w1,
                               font=font, fill=(0, 202, 202))
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.65 + 25), w2,
                               font=font, fill=(255, 211, 6))
                draw_text.text((bg_img.size[0] / 3 + move, bg_img.size[1] / 1.25 + 25), w3,
                               font=font, fill=(234, 0, 0))
                if idx < 10 * 2:
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 2.5 + 25), w1,
                                   font=font, fill=(0, 202, 202))
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 1.65 + 25), w2,
                                   font=font, fill=(255, 211, 6))
                    draw_text.text((bg_img.size[0] / 3 + move + 1.5, bg_img.size[1] / 1.25 + 25), w3,
                                   font=font, fill=(234, 0, 0))
                img_list.append(MakeGif.array_to_img(bg_img))
                idx = MakeGif.fine_tuning_word(w1, idx)
                idx += 1

        # FIXME gif 結尾停留時間久點
        img_list += [MakeGif.array_to_img(bg_img) for idx in range(20)]

        # FIXME 儲存檔案
        # bg_img.save(f'{self.save_path}{user_name}_leetcode_{type_name}.png')
        img_list[0].save(f'{self.save_path}/{self.username}_leetcode_{type_name}.gif',
                         save_all=True, append_images=img_list[1:], duration=60, loop=1, disposal=0)

    def main(self):
        MakeGif.check_folder(self.save_path)
        self.progress_bar('args')
        ret_dict = MakeGif.get_source(self.headers, self.userid)
        self.draw_gif(ret_dict)
        self.progress_bar('done')