# settings.py

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
DOWNLOADER_CLIENTCONTEXTFACTORY = 'listcontacts.contextfactory.LegacyConnectContextFactory'
REDIRECT_ENABLED = False
handle_httpstatus_list = [302]
