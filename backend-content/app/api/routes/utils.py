from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import Any, Union
import requests
from app.core.config import settings
import logging
import base64

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/transcript")
def process_input(input_data: Union[str, UploadFile]) -> Any:
    """
    Process the input data based on its type (string, uploaded file, or byte stream)
    and pass the resulting byte stream to another HTTP API.
    """
    byte_stream = None
    logger.info(f"Input is a string: {input_data}")

    if isinstance(input_data, str):
        logger.info(f"Input is a string: {input_data}")
        try:
            response = requests.get(input_data)
            response.raise_for_status()
            byte_stream = response.content
        except requests.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Failed to fetch the online resource: {e}")
    
    elif isinstance(input_data, UploadFile):
        logger.info(f"Input is an uploaded file: {input_data.filename}")
        # Input is an uploaded file, read it as a byte stream
        try:
            byte_stream = input_data.file.read()
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to read the uploaded file: {e}")
    
    else:
        raise HTTPException(status_code=400, detail="Invalid input type")

    byte_str = base64.b64encode(byte_stream)
    # Assume the next HTTP API endpoint is 'http://example.com/api' and it accepts byte stream as 'file'
    try:
        response = requests.post(f'{settings.AUDIO_SERVICE_URL}/transcribe', files={'filebytestr': byte_str})
        response.raise_for_status()
        return response.json()  # Assuming the response is an object array in JSON format
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to call the downstream API: {e}")



# @router.get("/transcript")
# def get_transcript(input_data: str) -> Any:
#     logger.info(f"Input is a string: {input_data}")
#     try:
#         response = requests.get(input_data)
#         response.raise_for_status()
#         byte_stream = response.content
#     except requests.RequestException as e:
#         raise HTTPException(status_code=400, detail=f"Failed to fetch the online resource: {e}")

#     byte_str = base64.b64encode(byte_stream)
#     logger.info(f"Byte string: {byte_str}")
#     # Assume the next HTTP API endpoint is 'http://example.com/api' and it accepts byte stream as 'file'
#     try:
#         response = requests.post(f'{settings.AUDIO_SERVICE_URL}/transcribe', files={'filebytestr': byte_str})
#         response.raise_for_status()
#         return response.json()  # Assuming the response is an object array in JSON format
#     except requests.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Failed to call the downstream API: {e}")