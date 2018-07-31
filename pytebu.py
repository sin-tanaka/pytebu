from requests_html import HTMLSession
from prettytable import PrettyTable


def cli():
    pass


def get_hatena_hotentry(category='all', top=10):
    HATENA_URL_BASE = 'http://b.hatena.ne.jp/hotentry/'

    url = HATENA_URL_BASE + category

    session = HTMLSession()
    r = session.get(url)

    # 大枠のコンテンツ取得
    sel = '#container > div.wrapper > div > div.entrylist-main > section > ul'
    content_elms = r.html.find(sel, first=True).find('.entrylist-contents-main')

    # 記事タイトルとURL部分
    article_elms = [i.find('.entrylist-contents-title', first=True) for i in content_elms]

    # ブックマーク数
    users_elms = [i.find('.entrylist-contents-users', first=True) for i in content_elms]

    output_table = PrettyTable(['title', 'url', 'bookmarks'])
    output_table.align['title'] = 'l'
    output_table.align['url'] = 'l'
    output_table.align['bookmarks'] = 'l'

    articles = [print_article(i, j) for i, j in zip(article_elms[:top], users_elms[:top]) ]

    [output_table.add_row(i) for i in articles]
    print(output_table)


def print_article(aelm, uelm):
    links = [aelm.text, list(aelm.absolute_links)[0], uelm.text]
    return links


if __name__ == '__main__':
    get_hatena_hotentry()
