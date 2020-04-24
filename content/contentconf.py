# -*- coding: utf-8 -*- #
# site-specific settings
GITHUB_ACCOUNT = 'oumpy'
SOURCEREPOSITORY_NAME = 'hp_management'

# Author
AUTHOR = 'Python会'
SITENAME = '大阪大学医学部 Python会'
SITEURL = ''
AUTHOR_INTRO = u'大阪大学医学部所属のPython職人集団です'
AUTHOR_DESCRIPTION = u'Now is better than never'
# AUTHOR_AVATAR = '../images/'
# AUTHOR_WEB = 'https://twitter.com/oumed_python'
SITESUBTITLE ='Now is better than never.'
SITETAG = SITENAME

# Social
SOCIAL = (
    # ('facebook', ''),
    # ('技術Blog (はてな)','https://oumedpython.hatenablog.com/'),
    ('<i class="fab fa-twitter"></i> Twitter', 'https://twitter.com/oumed_python'),
    ('<i class="far fa-envelope"></i> E-mail', 'mailto:handai.python@gmail.com'),
    ('<i class="fab fa-github"></i> GitHub', 'https://github.com/oumpy'),
    ('<i class="fab fa-youtube"></i> YouTube', 'https://www.youtube.com/channel/UCh1eAeDCpsZeOh0Z9paNfHQ'),
)

# Blogroll
LINKS = (
        # ('Python会ブログ','https://oumedpython.hatenablog.com/'),
        #('大阪大学医学部', 'http://www.med.osaka-u.ac.jp/'),
        #('Python.org', 'http://python.org/'),
        #('Pelican（本サイトで使用）', 'http://getpelican.com/'),
        # ('Jinja2', 'http://jinja.pocoo.org/'),
        # ('You can modify those links in your config file', '#'),
        )

# Settings for Twitter Timeline
TWITTER_TIMELINE_URL = "https://twitter.com/oumed_python?ref_src=twsrc%5Etfw"
TWITTER_USERNAME = 'oumed_python'

CUSTOM_SOCIAL_TITLE = "ソーシャル"
CUSTOM_CATEGORIES_TITLE = "記事カテゴリ"
CUSTOM_TAGS_TITLE = "タグ"
CUSTOM_LINKS_TITLE = "リンク"
CUSTOM_TWITTERTL_TITLE = "Timeline"
CUSTOM_RELATED_ARTICLES_TITLE = "関連記事"

OPEN_GRAPH_IMAGE = 'logo.jpg'

DISPLAY_PAGES_ON_MENU = False
CATEGORYNAMES_ALTERNATIVES = {
    'News': ('お知らせ', 'Python会からのお知らせ'),
    'Blog': ('技術ブログ',),
}
ADD_ON_MENU = (
    ('Python会について', 'index.html'),
    ('活動内容', 'activities.html'),
    ('実績', 'achievements.html'),
    (CATEGORYNAMES_ALTERNATIVES['Blog'][0], 'blog.html'),
    (CATEGORYNAMES_ALTERNATIVES['News'][0], 'news.html'),
    ('会員募集', 'recruit.html'),
    ('Contact', 'contact.html'),
)
HIDE_ARCHIVES_ON_MENU = True
SIDEBAR_HIDE_CATEGORIES = True

SHOW_CATEGORIES_ON_LIST = False
SHOW_CATEGORY_TITLE = True
def readfile(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
    return ''.join(content)
PAGE_EXCLUDES = ['pages/includes']
CATEGORY_CONTENTS = {
    'blog' : readfile('content/pages/includes/blog_content.html'),
    'news' : readfile('content/pages/includes/news_content.html'),
}
DEFAULT_PAGINATION = 10

CUSTOM_TAG_BADGE_COLOR = 'blue'
TAG_GROUPS = [ # (groupname, [articles,...,], badge_color )
    ('Research tools & techniques', ['Bioinformatics', 'Machine Learning', 'Statistics', 'Data Science Competition'], 'darkorange'),
    ('Programming', ['Python', 'Shell script', 'GitHub', '競技プログラミング'], 'darkgreen'),
    ('その他', ['論文関連', '検定試験', '海外留学'], CUSTOM_TAG_BADGE_COLOR),
]
CUSTOM_TAG_BADGE_COLORS = {'News' : 'hotpink'}
for group in TAG_GROUPS:
    for tag in group[1]:
        CUSTOM_TAG_BADGE_COLORS[tag] = group[2]
import urllib.parse
URL_ENCODED_GROUPNAMES = dict([ (group[0], urllib.parse.quote(group[0])) for group in TAG_GROUPS ])

PREVIEW_SITENAME_APPEND = ' (テスト用ページ)'
