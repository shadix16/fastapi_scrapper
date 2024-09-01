from module_scrapper.utils import NotificationUtils, \
    ScrapperUtils
from module_scrapper.logging import logger
from module_scrapper.cache import Cache
from module_scrapper.utils import DatabaseUtils


# Define ScraperServiceHandler class, which handles the scraping service
# This class inherits from ScrapperUtils, NotificationUtils, Cache, and DatabaseUtils
class ScraperServiceHandler(ScrapperUtils, NotificationUtils, Cache, DatabaseUtils):

    # Constructor method that initializes the handler with settings
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.final_response = {}
        self.message = "success"
        self.status_code = 200

    # Main function to execute the scraping request
    def execute_request(self):
        try:
            # Log the start of the scraping process, including the page limit and proxy settings
            logger.info("start {}{}".format(self.settings.limit_pages, self.settings.proxy))

            # Continuous loop to perform scraping
            while True:
                self._get_page_details()  # Retrieve details for the current page

                # Check if the response is empty or if a condition to break the loop is met
                if not self.response or self.is_break:
                    break

                # Create a parser for the page details obtained
                self.create_parser()

            # Notify that the scraping is completed and log the total number of products scraped
            self.notify("Scrapping is completed with total no of products are {}".format(len(self.products)))

            # Set the final response with the total number of products scraped
            self.final_response = {"total number of product scrapped": len(self.products)}

            # Return the success status code and final response
            return self.status_code, self.final_response

        except Exception as e:
            # Handle any exceptions that occur during scraping
            logger.error(e)
            error = {"error": str(e)}
            self.status_code = 400
            return self.status_code, error
