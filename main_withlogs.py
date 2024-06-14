from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pytesseract
from PIL import Image
import io
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI()

# Request models
class ImageTextRequest(BaseModel):
    base64_image: str

class BoundingBoxRequest(BaseModel):
    base64_image: str
    bbox_type: str

# Decode base64 image function
def decode_base64_image(base64_image: str) -> Image.Image:
    try:
        image_data = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_data))
        return image
    except Exception:
        logger.error("Failed to decode base64 image")
        raise HTTPException(status_code=400, detail="Invalid base64_image.")

# Endpoint to extract text from image
@app.post("/api/get-text")
async def get_text(request: ImageTextRequest):
    try:
        image = decode_base64_image(request.base64_image)
        text = pytesseract.image_to_string(image)
        logger.info(f"Extracted text: {text}")
        return {"success": True, "result": {"text": text}}
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        return {"success": False, "error": {"message": e.detail}}
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        return {"success": False, "error": {"message": "Internal server error"}}

# Endpoint to extract bounding boxes from image
@app.post("/api/get-bboxes")
async def get_bboxes(request: BoundingBoxRequest):
    try:
        image = decode_base64_image(request.base64_image)
        box_type = request.bbox_type

        if box_type not in ["word", "line", "paragraph", "block", "page"]:
            logger.error("Invalid bbox_type")
            raise HTTPException(status_code=400, detail="Invalid bbox_type.")

        boxes = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        box_keys = {'word': 'text', 'line': 'line_num', 'paragraph': 'par_num', 'block': 'block_num', 'page': 'page_num'}
        key = box_keys[box_type]

        bboxes = [
            {"x_min": boxes['left'][i], "y_min": boxes['top'][i], "x_max": boxes['left'][i] + boxes['width'][i], "y_max": boxes['top'][i] + boxes['height'][i]}
            for i in range(len(boxes['level']))
            if boxes[key][i] != -1
        ]
        logger.info(f"Extracted bboxes: {bboxes}")
        return {"success": True, "result": {"bboxes": bboxes}}
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        return {"success": False, "error": {"message": e.detail}}
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        return {"success": False, "error": {"message": "Internal server error"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
