# coding=utf-8
#!/usr/bin/python

# URL 管理器


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            #print("add_new_url", url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        # 取出并且移除
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)

        #print("get_new_url", new_url)
        return new_url
