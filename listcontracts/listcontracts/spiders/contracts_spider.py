import scrapy

class ContactSpider(scrapy.Spider):
    name = "contracts"
    handle_httpstatus_list = [200]

    custom_settings = {
        'ITEM_PIPELINES': {'__main__.MyFilesPipeline': 1},
        'FILES_STORE': '/listcontacts/to/save/files',
        'DOWNLOADER_CLIENTCONTEXTFACTORY': 'listcontracts.contextfactory.LegacyConnectContextFactory',
    }
    start_urls = [
        'https://apps.nd.gov/csd/spo/services/bidder/listCurrentContracts.htm',
    ]

    def start_requests(self):
        yield scrapy.Request('https://apps.nd.gov/csd/spo/services/bidder/listCurrentContracts.htm', self.parse)

    def parse(self, response):
        if response.status != 302:
            for contract in response.css('table tr'):
                yield {
                    'contract_name': contract.css('td:nth-child(1)').get(),
                    'contract_number': contract.css('td:nth-child(2)').get(),
                    'vendor_name': contract.css('td:nth-child(3)::text'),
                    'url': contract.css('td:nth-child(7) a::text').get()
                }
        else :
            print(f"responses : {response}");
