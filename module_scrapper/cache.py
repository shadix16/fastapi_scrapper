import redis
from module_scrapper.settings import REDIS_HOST, REDIS_PORT
from module_scrapper.schema import ValidateProduct

"""Below Class is used for caching and checking whether the price of the product is changed or not"""


class Cache:
    def __init__(self):
        super().__init__()
        self.client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def is_price_changed(self, product: ValidateProduct):  # used to calculate changed price
        cached_price = self.client.get(product.product_title)
        cached_price = cached_price.decode('utf-8') if cached_price else None
        print("cache price & new price", cached_price, product.product_price)
        return cached_price is None or cached_price != product.product_price

    def update_cache(self, product: ValidateProduct):     # used to update the cache with product details
        self.client.set(product.product_title, product.product_price)
