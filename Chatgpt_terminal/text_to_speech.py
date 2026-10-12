from kokoro import KPipeline
import soundfile as sf

# Initialize Kokoro
pipeline = KPipeline(lang_code="a")

# Input text
text = """
Generative AI is a branch of artificial intelligence
that can generate text, images, audio and other content.
"""

# Generate speech
generator = pipeline(
    text,
    voice="af_heart",
    speed=1
)

# Save audio
for i, (gs, ps, audio) in enumerate(generator):
    filename = f"kokoro_output_{i}.wav"
    sf.write(filename, audio, 24000)
    print(f"Audio saved as: {filename}")