import scrapy

class ContractSpider(scrapy.Spider):
    name = "contracts"
    start_urls = [
        'https://apps.nd.gov/csd/spo/services/bidder/listCurrentContracts.htm',
    ]

    def parse(self, response):
        print("Hello")
        print(f"Contract : {response}")
        for contract in response.css('table tr'):
            yield {
                'contract_name': contract.css('td:nth-child(1) a::text').get(),
                'contract_number': contract.css('td:nth-child(2)::text').get(),
                'vendor_name': contract.css('td:nth-child(3)::text').get(),
            }
