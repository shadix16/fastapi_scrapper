from fastapi import APIRouter, Depends, HTTPException
from module_scrapper.handlers import ScraperServiceHandler
from module_scrapper.auth import check_auth
from module_scrapper.schema import ValidateResponseModel, ValidateScrapeSettings

# Create a new APIRouter instance, which will be used to define API endpoints
router = APIRouter()


# Define a POST endpoint at the root ("/") of the router
@router.post("/", dependencies=[Depends(check_auth)], response_model=ValidateResponseModel)
async def create(settings: ValidateScrapeSettings):
    """
    This is an asynchronous function that handles a POST request to the root ("/") endpoint.
    It is responsible for initiating a scraping service based on the provided settings.

    Args:
        settings (ValidateScrapeSettings): The settings required for the scraping process, validated against a schema.

    Returns:
        ValidateResponseModel: A response model that includes the status, message, and response data from the scraper service.
    """

    # Initialize the ScraperServiceHandler with the provided settings/payload
    _service_obj = ScraperServiceHandler(settings)

    # Execute the scraping request using the service handler
    status, response = _service_obj.execute_request()

    # Check the status returned by the service handler
    if status == 200:
        # If status is 200 (OK), return a success response
        message = "success"
        return ValidateResponseModel(status=status, message=message, response=response)
    elif status == 400:
        # If status is 400 (Bad Request), return a failure response
        message = "failed"
        return ValidateResponseModel(status=status, message=message, response=response)
    else:
        # For any other status, raise an HTTP 500 Internal Server Error
        raise HTTPException(status_code=500, detail="Internal Error")
