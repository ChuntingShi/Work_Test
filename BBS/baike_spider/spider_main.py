# coding:utf-8
from baike_spider import html_downloader, html_parser, url_manager, html_outputer


class SpidrMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader =  html_downloader.HtmlDownloader()
        self.parser =  html_parser.Htmlparser()
        self.outputer = html_outputer.Ht1mlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'% (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_url)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count = count + 1
            except:
                print "craw failed"

        self.outputer.output_html()

if __name__=="_main_":
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpidrMain()
    obj_spider.craw(root_url)