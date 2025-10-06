import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

import gradio as gr
from transformers import pipeline

gr.Interface.from_pipeline(pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")).launch()