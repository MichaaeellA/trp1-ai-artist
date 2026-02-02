import os
import wave

# Folder where Lyria outputs raw audio
raw_folder = "exports"
fixed_folder = "exports/fixed"

# Make the fixed folder if it doesn't exist
os.makedirs(fixed_folder, exist_ok=True)

# Loop through all raw .wav files (even if headers are missing)
for file in os.listdir(raw_folder):
    if file.endswith(".wav"):
        raw_path = os.path.join(raw_folder, file)
        fixed_path = os.path.join(fixed_folder, f"fixed_{file}")

        # Read raw PCM data
        with open(raw_path, "rb") as f:
            raw_data = f.read()

        # Create a proper WAV file
        with wave.open(fixed_path, "wb") as wav_file:
            wav_file.setnchannels(1)        # Mono audio
            wav_file.setsampwidth(2)        # 16-bit audio
            wav_file.setframerate(44100)    # 44.1kHz sample rate
            wav_file.writeframes(raw_data)

        print(f"Fixed WAV saved: {fixed_path}")
