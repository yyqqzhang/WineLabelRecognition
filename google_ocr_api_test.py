# Databricks notebook source
from flask import Flask, request, jsonify
from google.cloud import vision
import openai
import os

# COMMAND ----------

# Set up Google Cloud Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/dbfs/FileStore/yzhang/ocr_label/wine_ocr_391306_523471cf4596.json'

# COMMAND ----------

# Specify the file path
image_path = '/dbfs/FileStore/yzhang/ocr_label/wine1.png'

# COMMAND ----------

# Use Google Cloud Vision to extract text from image
client = vision.ImageAnnotatorClient()
with open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

# COMMAND ----------

# Use the first text annotation (which contains the entire text)
raw_text = texts[0].description
raw_text

# COMMAND ----------


