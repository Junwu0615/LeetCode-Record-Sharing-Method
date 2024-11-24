# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from Depend.MakeGif import MakeGif
from Depend.ArgumentParser import AP

class Entry:
    def __init__(self):
        self.userid = None
        self.username = None
        self.font = None
        self.bg_color = None
        self.font_color = None
        self.font_shadow = None
        self.customize_path = None

    def main(self):
        ap = AP(self)
        ap.config_once()
        mg = MakeGif(self)
        mg.main()

if __name__ == '__main__':
    entry = Entry()
    entry.main()