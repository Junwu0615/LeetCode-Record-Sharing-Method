# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from argparse import ArgumentParser, Namespace

class AP:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def parse_args() -> Namespace:
        parse = ArgumentParser()
        parse.add_argument("-i", "--userid",
                           help="give a LeetCode user-id.",
                           default="user0190Nh", type=str)

        parse.add_argument("-n", "--username",
                           help="give your name.",
                           default="Ping Chun", type=str)

        parse.add_argument("-f", "--font",
                           help="give a font type.",
                           default="AniMeMatrix-MB_EN.ttf", type=str)

        parse.add_argument("-bc", "--bgcolor",
                           help="give a background color.",
                           default="#3C3C3C", type=str)

        parse.add_argument("-fc", "--fontcolor",
                           help="give a font color.",
                           default="255,255,255", type=str)

        parse.add_argument("-fs", "--fontshadow",
                           help="give a font shadow.",
                           default="39,39,39", type=str)

        parse.add_argument("-p", "--customizepath",
                           help="If you want to customize the picture, please give the path.",
                           default="None", type=str)

        return parse.parse_args()

    def config_once(self):
        args = AP.parse_args()
        self.obj.userid = args.userid
        self.obj.username = args.username
        self.obj.font = args.font
        self.obj.bg_color = args.bgcolor
        self.obj.font_color = args.fontcolor
        self.obj.font_shadow = args.fontshadow
        self.obj.customize_path = args.customizepath