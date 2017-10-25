# Github Trends

This is CLI program used for searching for the most popular Python repositories on Github. <br/>

Script finds 20 most stargazers counted repositories created during the last week and prints the following infomation: <br/>
repo name, stars count, repo description, opened issues count and repo URL. <br/>
Data is presented in descending order of repo stars.

The program is based on GitHub [REST API v3](https://developer.github.com/v3/)

Pavel Kadantsev, 2017. <br/>
p.a.kadantsev@gmail.com

# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using command ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment.

# Usage

To execute the script use the following command in CLI: ```python github_trending.py```. <br />
CLI encoding changing may be required for correct script running on Windows platfrom: ```chcp 65001``` for UTF-8 encoding.

# Example of Script Launch

```Hey! Here are the most popular Python projects for the last week on GitHub.


1. Repository name: wedding
    Stars count: 738
    Description: 婚礼大屏互动，微信请柬一站式解决方案
    Issues count: 1
    Link: https://github.com/iammapping/wedding

2. Repository name: nyc-dna-software
    Stars count: 264
    Description: The source code, acquired by ProPublica, for New York City's Forensic Statistical Tool.
    Issues count: 3
    Link: https://github.com/propublica/nyc-dna-software

3. Repository name: mx-maskrcnn
    Stars count: 214
    Description: A MXNet implementation of Mask R-CNN
    Issues count: 0
    Link: https://github.com/TuSimple/mx-maskrcnn
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
