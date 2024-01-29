<a href='https://github.com/Junwu0615/LeetCode-Record-Sharing-Method'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/LeetCode-Record-Sharing-Method.svg'> 
<a href='https://github.com/Junwu0615/LeetCode-Record-Sharing-Method'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.github.com/Junwu0615/df4349f01a564de4cf309a290098ba58/raw/LeetCode-Record-Sharing-Method_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/Junwu0615/LeetCode-Record-Sharing-Method) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-Pillow_10.1.0-green.svg?style=plastic)](https://pypi.org/project/pillow/) 
[![](https://img.shields.io/badge/Package-BeautifulSoup_4.12.2-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests_2.31.0-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-Numpy_1.26.2-green.svg?style=plastic)](https://pypi.org/project/numpy/) 
[![](https://img.shields.io/badge/Package-ArgumentParser_1.2.1-green.svg?style=plastic)](https://pypi.org/project/argumentparser/) 

## 前言
原先我是想衝刺寫哩扣，為後續找工作提升錄取率等等，然後找有沒有現成資源讓履歷有農題紀錄，但沒看過有人做這玩意兒；時間往後一拉我已找到工作，而寫哩扣的動力當然就大幅下降，後來想到我或許可以藉此激勵自己，每天農題把紀錄提升上來 lol，於是自己瞎搞一個。

## 歷史紀錄
| 事件 | 敘述 | 時間 |
| :--: | :-- | :--: |
| v1.0 |  Graphics Interchange Format | 2024/01/27 |
| v1.1 |  新增陰影顏色、進度條顯示 | 2024/01/30 |
| - | 擴增 PDF 來展現內容 | - |
| - | 最初想像這位[大神](https://github.com/anuraghazra/github-readme-stats)的方法動態更新數據，但顯然俺不會... | - |

## How To Use

### STEP.1　CLONE
```python
git clone https://github.com/Junwu0615/LeetCode-Record-Sharing-Method.git
```

</br>

### STEP.2　INSTALL PACKAGES
```python
pip install -r requirements.txt
```

</br>

### STEP.3　RUN
```python
python LeetCode-Record-Sharing-Method.py -h
```

</br>

### STEP.4　HELP
- `-h`　Help :　Show this help message and exit.
- `-i`　User ID :　Give a LeetCode user-id.
- `-n`　User Name :　Give your name.
- `-f`　Font :　Give a font type.　Default :　"AniMeMatrix-MB_EN.ttf"
- `-bc`　Background Color :　Give a background color.　Default :　"#3C3C3C"
- `-fc`　Font Color :　Give a font color.　Default :　"255,255,255"
- `-fs`　Font Shadow :　Give a font shadow.　Default :　"39,39,39"
- `-p`　Customize Path :　If you want to customize the picture, please give the path.　Default :　"None"

</br>

### STEP.5　EXAMPLE
範例是從 LeetCode 看到的幾位解題達人 [Sithis](https://leetcode.com/Sithis/)、[numb3r5](https://leetcode.com/numb3r5/)、[uwi](https://leetcode.com/uwi/) 之數據來呈現，他們數據比較豐富 www。
</br>
</br>

<img src="https://github.com/Junwu0615/LeetCode-Record-Sharing-Method/blob/main/sample_img/00.jpg"/>
<img src="https://github.com/Junwu0615/LeetCode-Record-Sharing-Method/blob/main/sample_img/01.jpg"/>

### I.　純色背景
運行完畢後會產出 `gif` 檔。 </br>
- `-i`　Sithis </br>
- `-n`　"Sithis" </br>
- `-f`　"AniMeMatrix-MB_EN.ttf" </br>
- `-bc`　#FFFFFF </br>
- `-fc`　"64,64,64" </br>
- `-fs`　"39,64,64" </br>
- `-p`　"None" </br>
```python
python LeetCode-Record-Sharing-Method.py -i Sithis -n "Sithis" -f "AniMeMatrix-MB_EN.ttf" -bc #FFFFFF -fc "64,64,64" -fs "190,190,190" -p "None"
```
![Sithis.gif](/sample_img/Sithis_leetcode_simple_bg.gif)
- `-i`　numb3r5 </br>
- `-n`　"numb3r5" </br>
- `-f`　"AniMeMatrix-MB_EN.ttf" </br>
- `-bc`　#3C3C3C </br>
- `-fc`　"255,255,255" </br>
- `-fs`　"39,39,39" </br>
- `-p`　"None" </br>
```python
python LeetCode-Record-Sharing-Method.py -i numb3r5 -n "numb3r5" -f "AniMeMatrix-MB_EN.ttf" -bc #3C3C3C	 -fc "255,255,255" -fs "39,39,39" -p "None"
```
![numb3r5.gif](/sample_img/numb3r5_leetcode_simple_bg.gif)
- `-i`　uwi </br>
- `-n`　"uwi" </br>
- `-f`　"AniMeMatrix-MB_EN.ttf" </br>
- `-bc`　#3C3C3C </br>
- `-fc`　"255,255,255" </br>
- `-fs`　"39,39,39" </br>
- `-p`　"None" </br>
```python
python LeetCode-Record-Sharing-Method.py -i uwi -n "uwi" -f "AniMeMatrix-MB_EN.ttf" -bc #3C3C3C -fc "255,255,255" -fs "39,39,39" -p "None"
```
![uwi.gif](/sample_img/uwi_leetcode_simple_bg.gif)


### II.　自定義背景
加入自定義的圖片，路徑放置於 `./sample_img/xxx` 。
- `-i`　Sithis </br>
- `-n`　"Sithis" </br>
- `-f`　"AniMeMatrix-MB_EN.ttf" </br>
- `-bc`　None </br>
- `-fc`　"64,64,64" </br>
- `-p`　"./sample_img/pexels-pixabay-235985.jpg" </br>
```python
python LeetCode-Record-Sharing-Method.py -i Sithis -n "Sithis" -f "AniMeMatrix-MB_EN.ttf" -bc None -fc "39,39,39" -fs "157,157,157" -p "./sample_img/pexels-pixabay-235985.jpg"
```
![00.gif](/sample_img/00.gif)

```python
python LeetCode-Record-Sharing-Method.py -i numb3r5 -n "numb3r5" -f "AniMeMatrix-MB_EN.ttf" -bc None -fc "255,255,255" -fs "39,39,39" -p "./sample_img/pexels-pixabay-164175.jpg"
```
![01.gif](/sample_img/01.gif)

```python
python LeetCode-Record-Sharing-Method.py -i uwi -n "uwi" -f "SHOWG.TTF" -bc None -fc "255,250,250" -fs "39,39,39" -p "./sample_img/pexels-pixabay-531880.jpg"
```
![02.gif](/sample_img/02.gif)

</br>

## 相關資源
- [色階表](https://www.ifreesite.com/color/online-color-picker.htm)
- [創作者免費圖庫](https://www.pexels.com/zh-tw/)
