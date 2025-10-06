import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import pipeline

pipe = pipeline("text-classification")