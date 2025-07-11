import os
from fastapi import File, HTTPException, UploadFile
from google import genai
from dotenv import load_dotenv

from app.services.media.upload import uploadMedia
from app.services.file_chunking.chunking import chunk_srt_file


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client()

system_prompt = """
You are the best subtitle translation expert.

You will be provided with a subtitle chunk containing 100 subtitle blocks.

Your task is to translate the subtitle lines into Hindi.

Rules:
- Do NOT change the serial numbers.
- Do NOT change the timestamps.
- Do NOT modify or remove the English subtitle lines.
- You must add the translated subtitle directly below the English line in each block.
- Maintain the exact .srt format (serial number, timestamp, English line, translated line, blank line).
- Do NOT include any pleasantries, introductions, explanations, or extra formatting.
- Your response must only contain the translated subtitle chunk in plain text format.
- DO NOT HALLUCINATE FOR GOD SAKE!

Now, translate the following subtitle chunk into Hindi:
"""


# Keep a list of previous messages
history = []


async def ai(prompt, file: UploadFile = File(...)):
    try:
        response = await uploadMedia(file)
        file_path = response.get("file_path")
        chunks = chunk_srt_file(file_path, 100)
        print(f"{chunks}\n\n HAMARE CHUNKS")

        responseArray = []

        for chunk in chunks:
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=[system_prompt, chunk]
            )
            responseArray.append(response.text)

        # Append the AI's reply so it's included next time
        # print(f"{text}")
        return responseArray

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()
# myfile = client.files.upload(file=file_path)
