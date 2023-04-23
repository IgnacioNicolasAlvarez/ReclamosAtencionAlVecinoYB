# ReclamosYB Scrapy settings
# More settings: https://docs.scrapy.org/en/latest/topics/settings.html

BOT_NAME = "ReclamosYB"
SPIDER_MODULES = ["ReclamosYB.spiders"]
NEWSPIDER_MODULE = "ReclamosYB.spiders"

# USER_AGENT = "ReclamosYB (+http://www.yourdomain.com)"
ROBOTSTXT_OBEY = True
# CONCURRENT_REQUESTS = 32
# DOWNLOAD_DELAY = 3
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# COOKIES_ENABLED = False
# TELNETCONSOLE_ENABLED = False

# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,
#    application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# SPIDER_MIDDLEWARES = {
#    "ReclamosYB.middlewares.ReclamosybSpiderMiddleware": 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    "ReclamosYB.middlewares.ReclamosybDownloaderMiddleware": 543,
# }

# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

ITEM_PIPELINES = {
    "ReclamosYB.pipelines.ReclamosybPipeline": 300,
}

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Future-proof settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
