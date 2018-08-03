# pytebu

![](https://raw.githubusercontent.com/sin-tanaka/pytebu/master/Screenshop.png)

Command Line Client for Hatena Bookmark HotEntry inspired by gotebu(https://github.com/massa142/gotebu)

# Installation

```sh
$ pip install git+https://github.com/sin-tanaka/pytebu
```


# Usage

```sh
# show all categories
$ pytebu -l
['all', 'general', 'social', 'economics', 'life', 'knowledge', 'it', 'fun', 'entertainment', 'game']

# show hot entries
$ pytebu it
+----------------------------------------------------------------+--------------------------------------------------------------------+------------+
| title                                                          | url                                                                | bookmarks  |
+----------------------------------------------------------------+--------------------------------------------------------------------+------------+
| 杭州市から渋滞が消えた！人工知能が交通信号を制御する - 中華... | http://tamakino.hatenablog.com/entry/2018/08/03/080000             | 146 users  |
| IFTTTにGoogle App Scriptを混ぜたらヤバい化学反応が起こった...  | http://moguno.hatenablog.jp/entry/2018/08/02/163119                | 1140 users |
| 世界最強｢グーグル検索｣が背負う期待と責任 | インターネット |... | https://toyokeizai.net/articles/-/231700                           | 165 users  |
| イケてるエンジニアになろうシリーズ 〜Dockerガチ入門編〜 - ...  | http://moro-archive.hatenablog.com/entry/2018/08/01/000000         | 331 users  |
| 「Windows 95」から「5G」まで　ネット回線の進化とコンテンツ...  | https://time-space.kddi.com/it-technology/20180803/2393            | 79 users   |
| The Next Chapter - Treasure Data                               | https://www.treasuredata.co.jp/blog_jp/the-next-chapter/           | 161 users  |
| 初音ミクが目の前で踊っているようにしか見えない疑似ホログラ...  | https://gigazine.net/news/20180803-hatsune-miku-holography/        | 125 users  |
| 機械学習プロジェクトが失敗する9つの理由 - 六本木で働くデー...  | https://tjo.hatenablog.com/entry/2018/08/03/080000                 | 126 users  |
| 【それってネット詐欺ですよ！】 突然「Googleをお使いのあなた... | https://internet.watch.impress.co.jp/docs/column/dlis/1136222.html | 99 users   |
| 「命乞いするロボットの電源を切るのは難しい」ことが最新の研...  | http://news.livedoor.com/article/detail/15106844/                  | 21 users   |
+----------------------------------------------------------------+--------------------------------------------------------------------+------------+
```