import scrapy
from scrapy.crawler import CrawlerProcess
from newspaper import Article
import random
import os
from scrapy.crawler import CrawlerProcess
import json

def scrape(url):
    class ProductDescriptionSpider(scrapy.Spider):
        name = 'product_description'

        def start_requests(self):
            # url = sys.argv[1]
            yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            # Extract the main content from the URL
            main_content = self.extract_full_text(response)

            # Find the "About Us" link
            about_us_link = response.css('a::attr(href)').re_first(r'/about-us/?$')
            our_work_link = response.css('a::attr(href)').re_first(r'/our-work/?$')

            if about_us_link:
                about_us_url = response.urljoin(about_us_link)
                yield scrapy.Request(url=about_us_url, callback=self.parse_about_us, meta={'main_content': main_content, 'url': response.url})
            elif our_work_link:
                our_work_url = response.urljoin(our_work_link)
                yield scrapy.Request(url=our_work_url, callback=self.parse_our_work, meta={'main_content': main_content, 'url': response.url})
            else:
                self.log(f"No 'About Us' or 'Our Work' link found on {response.url}")
                self.parse_content(response.url, main_content)

        def parse_about_us(self, response):
            main_content = response.meta['main_content']
            url = response.meta['url']
            about_us_content = self.extract_full_text(response)

            full_text = main_content + '\n\n' + about_us_content
            self.parse_content(url, full_text)

        def parse_our_work(self, response):
            main_content = response.meta['main_content']
            url = response.meta['url']
            our_work_content = self.extract_full_text(response)

            full_text = main_content + '\n\n' + our_work_content
            self.parse_content(url, full_text)

        def parse_content(self, url, full_text):
            # Extract the title, text, authors, and publish date using newspaper3k
            article = Article(url)
            article.download()
            article.parse()
            title = article.title
            text = article.text
            authors = article.authors
            publish_date = article.publish_date

            # Save the extracted data to a JSON file
            self.save_to_file(url, title, text, full_text, authors, publish_date)

            # Print the extracted data to the console
            self.display_data(url, title, text, full_text, authors, publish_date)

        def extract_full_text(self, response):
            # Use Scrapy's built-in selectors to extract the complete text content of the website
            text_elements = response.css(
                'p::text, li::text, h1::text, h2::text, h3::text, h4::text, h5::text, '
                'h6::text, span::text, div::text, td::text, th::text'
            ).getall()
            full_text = '. '.join([p.strip() for p in text_elements if p.strip()])
            return full_text

        # ... (the rest of the code remains the same)
        def save_to_file(self, url, title, text, full_text, authors, publish_date):
            # Create a directory to store the JSON files
            output_dir = 'scraped_data'
            os.makedirs(output_dir, exist_ok=True)

            # Extract domain name from URL
            domain = url.split('//')[-1].split('/')[0]

            # Construct the filename based on the domain name
            filename = f"{domain}.json"
            file_path = os.path.join(output_dir, filename)

            # Save the extracted data to a JSON file
            data = {
                'title': title,
                'text': text,
                'full_text': full_text,
                'authors': authors,
                'publish_date': publish_date
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"Saved data to {file_path}")

        def display_data(self, url, title, text, full_text, authors, publish_date):
            # Print the extracted data to the console in a formatted manner
            print("=" * 80)
            print(f"URL: {url}")
            print(f"Title: {title}")
            print("\nText:")
            print(text)
            print("\nFull Text:")
            self.print_full_text(full_text)
            print(f"\nAuthors: {', '.join(authors)}")
            print(f"Published: {publish_date}")
            print("=" * 80)
            print()

        def print_full_text(self, full_text):
            # Print the full text in a consolidated, paragraph-based format
            paragraphs = [p for p in full_text.split('\n\n') if p.strip()]
            for paragraph in paragraphs:
                print(paragraph)
                print()

    
    process = CrawlerProcess()
    process.crawl(ProductDescriptionSpider)
    process.start()
    # return process

