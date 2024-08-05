from datasets import load_dataset, Audio
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

# Load the Whisper model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")


def get_text(audio):
    '''
    this method will take a audio with array of audios
    '''
    inputs = processor(audio["array"], sampling_rate=audio["sampling_rate"], return_tensors="pt")
    # Generate transcription
    with torch.no_grad():
        predicted_ids = model.generate(inputs.input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription