import base64
import os
import subprocess
import tempfile

from fastapi import FastAPI, UploadFile, Header, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI()


class ConcatRequest(BaseModel):
    videos_base64: list[str]

API_KEY = os.environ.get("API_KEY", "")


def check_auth(x_api_key: str | None):
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/mux")
async def mux(
    video: UploadFile,
    audio: UploadFile,
    x_api_key: str | None = Header(default=None, alias="X-Api-Key"),
):
    check_auth(x_api_key)

    work_dir = tempfile.mkdtemp(prefix="b7_mux_")
    try:
        video_path = os.path.join(work_dir, "video_in.mp4")
        with open(video_path, "wb") as f:
            f.write(await video.read())

        audio_path = os.path.join(work_dir, "audio_in")
        with open(audio_path, "wb") as f:
            f.write(await audio.read())

        output_path = os.path.join(work_dir, "output.mp4")
        ffmpeg = subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", video_path,
                "-i", audio_path,
                "-map", "0:v:0", "-map", "1:a:0",
                "-c:v", "copy", "-c:a", "aac",
                "-shortest",
                output_path,
            ],
            capture_output=True, text=True, timeout=180,
        )
        if ffmpeg.returncode != 0 or not os.path.exists(output_path):
            raise HTTPException(status_code=502, detail=f"ffmpeg failed: {ffmpeg.stderr[-800:]}")

        with open(output_path, "rb") as f:
            data = f.read()

        return Response(content=data, media_type="video/mp4")
    finally:
        subprocess.run(["rm", "-rf", work_dir])


@app.post("/concat")
async def concat(
    req: ConcatRequest,
    x_api_key: str | None = Header(default=None, alias="X-Api-Key"),
):
    check_auth(x_api_key)

    if not req.videos_base64:
        raise HTTPException(status_code=400, detail="videos_base64 rỗng")

    work_dir = tempfile.mkdtemp(prefix="b7_concat_")
    try:
        list_path = os.path.join(work_dir, "list.txt")
        with open(list_path, "w") as listf:
            for i, b64 in enumerate(req.videos_base64):
                p = os.path.join(work_dir, f"clip_{i:02d}.mp4")
                with open(p, "wb") as f:
                    f.write(base64.b64decode(b64))
                listf.write(f"file '{p}'\n")

        output_path = os.path.join(work_dir, "final.mp4")
        ffmpeg = subprocess.run(
            [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                "-i", list_path,
                "-c", "copy",
                output_path,
            ],
            capture_output=True, text=True, timeout=300,
        )
        if ffmpeg.returncode != 0 or not os.path.exists(output_path):
            raise HTTPException(status_code=502, detail=f"ffmpeg concat failed: {ffmpeg.stderr[-800:]}")

        with open(output_path, "rb") as f:
            data = f.read()

        return Response(content=data, media_type="video/mp4")
    finally:
        subprocess.run(["rm", "-rf", work_dir])
