import os
from src.ai_content.providers.google import veo

# Ensure exports folder exists
os.makedirs("exports", exist_ok=True)

# Initialize Veo provider
provider = veo.VeoProvider()

# Your custom prompt
prompt = "Sunrise over Ethiopian mountains"
duration = 5  # seconds
aspect_ratio = "16:9"

try:
    # Use the currently supported method
    result_bytes = provider.generate(prompt=prompt, duration=duration, aspect_ratio=aspect_ratio)

    # Save video file
    output_file = f"exports/video_sunrise.mp4"
    with open(output_file, "wb") as f:
        f.write(result_bytes)

    print(f"✅ Video saved to {output_file}")

except Exception as e:
    print("❌ Video generation failed:", e)
