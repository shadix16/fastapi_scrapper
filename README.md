# Scrapping website by using fast api

This is a FastAPI application for scraping product information from https://dentalstall.com/shop/.

## Prerequisites

1. Docker
2. Docker Compose

## Build and Run the Application

1. Clone the repository :

   - Open Command shell.
   - Run `git clone https://github.com/shadix16/fastapi_scrapper.git`
   - Go to project directory by following command
   - Run `cd fastapi_scrapper/`

2. Build and run the app :

    - Run `docker-compose up --build`

3. To start scrapping use below curl:
      - curl --location 'http://localhost:8000/scrape/' \
--header 'Authorization: ea19219nnska9921' \
--header 'Content-Type: application/json' \
--data '{
    "limit_pages": 4,
    "proxy": ""
}'
      - Authorization: A static token already provided in the above curl.
      - limit_pages: The number of pages to scrape.
      - proxy: (Optional) A proxy string.
      
4. After scraping a directory with name data name will be created where you can see the images and other details.

