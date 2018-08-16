# -*- coding: utf-8 -*-

# Scrapy settings for app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'app'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'app (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'scrapy_magicfields.MagicFieldsMiddleware': 100,
   'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
   # 'app.middlewares.AppSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'app.pipelines.AppPipeline': 300,
    # 'app.pipelines.ScreenshotPipeline': 300,  # XXX: this is cool but expensive (space)
    # 'scrapy_jsonschema.JsonSchemaValidatePipeline': 100, # XXX: too strict
    # 'scrapy.pipelines.files.FilesPipeline': 1,  # XXX: not currently downloading any files
    # 'scrapy.pipelines.images.ImagesPipeline': 1, # XXX: turn this on for ScreenshotPipeline
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500, # XXX: send items to elasticsearch AWESOME!!!
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# XXX: cache storage takes up too much space
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# # HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

SPLASH_URL = 'http://splash:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

DELTAFETCH_ENABLED = True

MAGIC_FIELDS = {
    "timestamp": "$time",
    "url": "$response:url",
    "spider": "$spider:name",
}

ELASTICSEARCH_SERVERS = ['http://elasticsearch']
ELASTICSEARCH_INDEX = 'jobs'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'  # Custom unique key
# can also accept a list of fields if need a composite key
# ELASTICSEARCH_UNIQ_KEY = ['url', 'id']

# FEED_FORMAT = 'jsonlines'
# FEED_URI = "file:///usr/src/data/items/jobs/%(name)s/%(time)s.jl"
# FILES_STORE = '/usr/src/data/items/files'
# IMAGES_STORE = '/usr/src/data/items/images'
