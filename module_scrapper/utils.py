import json
import os
import time
from module_scrapper.schema import ValidateProduct
from bs4 import BeautifulSoup
from module_scrapper.logging import logger
from module_scrapper.settings import BASE_URL, DATA_IMAGE_DIRETORY, USER_AGENT
import requests
import copy


# Manages database operations
class DatabaseUtils:
    def __init__(self, filename="data/products.json"):
        super().__init__()
        self.filename = filename

    # Saves product data to a JSON file
    def save(self, product: ValidateProduct):
        products = self._load_products()
        product_json = product.model_dump()
        products = [p for p in products if p['product_title'] != product_json['product_title']]
        products.append(product_json)
        self._save_products(products)

    # Loads products from the JSON file
    def _load_products(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    # Saves products to the JSON file
    def _save_products(self, products):
        with open(self.filename, "w") as file:
            json.dump(products, file, indent=4)


# Handles notifications
class NotificationUtils:
    def notify(self, message: str):
        print(message)

    def send_email(self):
        pass  # Placeholder for email functionality

    def send_message_on_slack(self):
        pass  # Placeholder for Slack notification


# Manages web scraping operations
class ScrapperUtils:
    def __init__(self):
        super().__init__()
        self.page = 1
        self.products = []
        self.response = None
        self.retries = 3
        self.new_or_updated_products = []
        self.is_break = False
        self.image_url = None

    # Parses HTML content to extract product details
    def create_parser(self):
        try:
            soup = BeautifulSoup(self.response.content, "html.parser")
            product_elements = soup.find_all('li', class_='product')
            logger.info(f"Page {self.page} - {len(product_elements)} products found")

            for element in product_elements:
                title = element.find('h2', class_='woo-loop-product__title').find('a')['href'].split('/')[-2]
                price = int(
                    float(element.find('span', class_='woocommerce-Price-amount').text.strip().replace("₹", "")))
                image_url = element.find('img', class_='attachment-woocommerce_thumbnail')['src']
                if '.jpg' not in image_url:
                    self.image_url = element.find('img', class_='attachment-woocommerce_thumbnail')['data-lazy-src']

                self.products.append(copy.deepcopy(ValidateProduct(
                    product_title=title,
                    product_price=price,
                    path_to_image=self._download_image()
                )))

            logger.info(f"Total products: {len(self.products)}")
            for product in self.products:
                logger.info(f"Product: {product.product_title}")
                if not self.is_price_changed(product):
                    continue
                self.save(product)
                self.update_cache(product)
                self.new_or_updated_products.append(product)

            self.page += 1
        except Exception as u:
            import traceback
            traceback.print_exc()
            raise Exception(u)

    # Retrieves page data from the website
    def _get_page_details(self):
        """Fetches data from a single page"""
        self.retries = 3
        if self.settings.limit_pages and self.page > self.settings.limit_pages:
            self.is_break = True
            return
        url = BASE_URL if self.page == 1 else f"{BASE_URL}/page/{self.page}/"
        print(f"Fetching: {url}")

        for _ in range(self.retries):
            try:
                self.response = requests.get(url, headers={"User-Agent": USER_AGENT},
                                             proxies={"http": self.settings.proxy,
                                                      "https": self.settings.proxy} if self.settings.proxy else None)
                if self.response.status_code == 200:
                    return self.response
            except requests.RequestException:
                time.sleep(5)
        self.response = None

    # Downloads an image from the web
    def _download_image(self):
        os.makedirs(DATA_IMAGE_DIRETORY, exist_ok=True)
        response = requests.get(self.image_url, stream=True)
        if response.status_code == 200:
            path = f"{DATA_IMAGE_DIRETORY}/{os.path.basename(self.image_url)}"
            with open(path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return path
        return ""
