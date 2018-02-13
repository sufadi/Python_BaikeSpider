# coding=utf-8
#!/usr/bin/python

'''
HTML 下载器
'''
import urllib.request


class HtmlDownload(object):

    def downloader(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            print("response.getcode() =", response.getcode())
            return None

        return response.read()
