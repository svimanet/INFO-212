

BOT_NAME = "beer"

SPIDER_MODULES = ["scrapper.spiders"]
NEWSPIDER_MODULE = "scrapper.spiders"





DOWNLOAD_HANDLERS = {
}


DOWNLOADER_MIDDLEWARES = {
   'scrapper.middleware.RandomUserAgentMiddleware': 300,
}






USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]


ITEM_PIPELINES = {
   'scrapper.pipelines.MySQLStorePipeline': 300,
}

LOG_LEVEL = "INFO"
HTTPCACHE_ENABLED = True
DEPTH_LIMIT = 0

CONCURRENT_ITEMS = 10


MYSQL_HOST = ''
MYSQL_DBNAME = ''
MYSQL_USER = ''
MYSQL_PASSWD = ''
MYSQL_TABLE = ''
