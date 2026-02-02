import asyncio
from src.ai_content.providers.google import lyria

# ----- CONFIGURATION -----
PROMPT = "Energetic Ethiopian jazz with percussion"
PROVIDER = "lyria"
DURATION = 30  # seconds
OUTPUT_FILE = "outputs/ethiopian_jazz.wav"  # will create outputs folder if it doesn't exist

# ----- SCRIPT -----
async def main():
    import os
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    print(f"🎵 Generating music with prompt: {PROMPT}")
    print(f"Provider: {PROVIDER}, Duration: {DURATION}s")
    
    # Load Lyria provider
    music_provider = lyria.LyriaProvider()
    
    try:
        # Generate music
        result = await music_provider.generate(
            prompt=PROMPT,
            duration=DURATION,
        )
        
        # Save to file
        with open(OUTPUT_FILE, "wb") as f:
            f.write(result)
        
        print(f"✅ Music generated successfully! Saved to {OUTPUT_FILE}")

    except Exception as e:
        print(f"❌ Generation failed: {e}")

# Run async
if __name__ == "__main__":
    asyncio.run(main())
