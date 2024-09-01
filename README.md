# Scrapping website by using fast api

This is a FastAPI application for scraping product information from https://dentalstall.com/shop/. This app is build by using python and fastapi framework. To run the application docker and docker compose are used.

## Prerequisites

1. Docker
2. Docker Compose

## Build and Run the Application

1. Clone the repository :

   - Open Command shell.
   - Run `https://github.com/shadix16/fastapi_scrapper.git`
   - Go to project directory by following command
   - Run `cd fastapi_scrapper/`

2. Build and run the app :

    - Run `docker-compose up --build`

3. To start scraping, go to http://localhost:8000/docs and use the /scrape endpoint. The endpoint requires the following parameters:

    - api_token: A static API token (in our case it is "your_static_token").
    - page_limit: The number of pages to scrape.
    - proxy: (Optional) A proxy string.


4. After scraping, you can view the json file containing the data inside "fastapi_scrapper/data" directory. Similarly, all images scraped are inside "fastapi_scrapper/data/images".

5. Use the command `docker-compose down -v` to stop and remove the containers.
