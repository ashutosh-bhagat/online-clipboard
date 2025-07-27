from typing import Optional
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import string
import secrets
from fastapi.responses import FileResponse, PlainTextResponse

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://clipy-clipboard.vercel.app/"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
import threading, time, shutil

def delete_after_delay(path, delay_sec=86400):
    def delayed_delete():
        time.sleep(delay_sec)
        shutil.rmtree(path)
    threading.Thread(target=delayed_delete).start()


def generate_code(length=6):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

@app.post("/upload")
async def upload_data(
    file: UploadFile = File(...)
):
    try:
        while True:
            code = generate_code()
            if not os.path.exists(os.path.join(UPLOAD_FOLDER, code)):
                break

        save_dir = os.path.join(UPLOAD_FOLDER, code)
        os.makedirs(save_dir, exist_ok=True)

        filepath = os.path.join(save_dir, file.filename)
        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())
        
        delete_after_delay(save_dir)

        return JSONResponse({"code": code})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@app.post("/upload_text")
async def upload_text(text: str = Body(...)):
    try:
        while True:
            code = generate_code()
            if not os.path.exists(os.path.join(UPLOAD_FOLDER, code)):
                break

        save_dir = os.path.join(UPLOAD_FOLDER, code)
        os.makedirs(save_dir, exist_ok=True)
        filepath = os.path.join(save_dir, "text.txt")
        with open(filepath, "w", encoding="utf-8") as buffer:
            buffer.write(text)

        delete_after_delay(save_dir)

        return JSONResponse({"code": code})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text upload failed: {str(e)}")

@app.get("/get/{code}")
async def get_data(code: str):
    try:
        folder_path = os.path.join(UPLOAD_FOLDER, code)

        if not os.path.exists(folder_path):
            raise HTTPException(status_code=404, detail="Invalid code")

        files = os.listdir(folder_path)

        if not files:
            raise HTTPException(status_code=404, detail="No content found for this code")

        if "text.txt" in files:
            with open(os.path.join(folder_path, "text.txt"), "r", encoding="utf-8") as f:
                content = f.read()
            return PlainTextResponse(content)

        file_path = os.path.join(folder_path, files[0])
        return FileResponse(file_path, filename=files[0])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")


