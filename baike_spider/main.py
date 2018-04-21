# coding=utf-8
#!/usr/bin/python

from baike_spider import url_manager, html_download, html_parser, html_outputer

import traceback


class SpiderMain(object):

    def __init__(self):
        # URL 管理器
        self.urls = url_manager.UrlManager()
        # URL 下载器
        self.downloader = html_download.HtmlDownload()
        # URL 解析器
        self.parser = html_parser.HtmlParser()
        # URL 输出器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫的调度程序
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                # 获取待爬取的 URL
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))

                html_content = self.downloader.downloader(new_url)
                if html_content is None:
                    print("html_content None")
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 只爬取 100 条的数据
                if(count == 100000):
                    break

                count = count + 1
            except:
                # traceback.print_exc()
                print("craw failed")

        self.outputer.output_html()

if __name__ == '__main__':
    # 入口 URL:百度百科的 CSDN 相关的百度词条
    root_url = "https://blog.csdn.net/su749520"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
