from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe("audio.wav")

print("Language:", info.language)

for segment in segments:
    print(
        f"[{segment.start:.2f}s → {segment.end:.2f}s] "
        f"{segment.text}"
    )