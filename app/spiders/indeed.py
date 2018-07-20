# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from app.items import Job, JobLoader
from w3lib.html import remove_tags


class IndeedSpider(CrawlSpider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    start_urls = ['http://indeed.com/jobs?l=houston']
    rules = (
            Rule(LinkExtractor(restrict_css='div.pagination'), follow=True),
            Rule(LinkExtractor(restrict_css='div.result', unique=True), callback='parse_item'),
    )

    def parse_item(self, response):
        """Load items with data scraped from response."""
        loader = JobLoader(item=Job(), response=response)
        loader.add_css('post_url', 'div.result::attr(data-jk)')
        loader.add_css('id', 'div.result::attr(id)')
        result_loader = loader.nested_css('div.result')
        result_loader.add_css('company', '.company')
        result_loader.add_css('post_age', 'span.date::text')
        result_loader.add_css('post_dt', 'span.date::text')
        result_loader.add_css('job_title', '.jobtitle')
        result_loader.add_css('location', '.location *::text')
        result_loader.add_css('job_summary', '.summary')
        return loader.load_item()
