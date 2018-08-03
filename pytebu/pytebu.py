from requests_html import HTMLSession
from prettytable import PrettyTable
from click import (
    argument,
    command,
    option,
)

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
HATENA_URL_BASE = 'http://b.hatena.ne.jp/hotentry/'


def get_hatena_hotentry(category='all', top=10):
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


def get_hatena_categories():
    session = HTMLSession()
    r = session.get(HATENA_URL_BASE)

    # 大枠のコンテンツ取得
    sel = '#container > div.navi-wrapper.js-navi-category-wrapper.is-unscrolled'
    category_elms = r.html.find(sel, first=True).find('.navi-link')

    categories = [list(i.links)[0].split('/')[-1] for i in category_elms]

    print(categories)


@command(short_help="Hatena category", context_settings=CONTEXT_SETTINGS)
@argument('category', required=False)
@option('--list/-l', 'list_category', is_flag=True, default=False, help='Show all [CATEGORY] type')
def cli(
        category='all',
        list_category=False,
):
    if list_category:
        get_hatena_categories()
    else:
        get_hatena_hotentry(category)


if __name__ == '__main__':
    cli()
