#サブスクション周りとエンドキーポイント
from signal import alarm
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import settings
import streamlit as st


#streamlit sharingでシークレット情報を扱う
#https://qiita.com/yuu999/items/e56fe82e61db0f74f9cb
# subscription_key = st.secrets.AzureApiKey.KEY
subscription_key = st.secrets["AzureApiKey"]["KEY"]
endpoint = st.secrets["AzureApiKey"]["ENDPOINT"]


# endpoint = st.secrets.AzureApiKey.ENDPOINT
#クライアントを認証(apiを使えるかどうかの認証)
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


#タグ情報を取得する関数
def get_tags(filepath):
  local_image = open(filepath, "rb")
  tags_result = computervision_client.tag_image_in_stream(local_image)

  tags = tags_result.tags
  tags_name = []
  for tag in tags:
    tags_name.append(tag.name)
  return tags_name

#オブジェクトの位置と情報
def detect_objects(filepath):
  local_image = open(filepath, "rb")

  detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
  objects = detect_objects_results.objects
  return objects


#streamlitによるアプリ画面
from PIL import ImageDraw
from PIL import ImageFont

st.title('物体検出アプリ')

#ファイルアップロード機能
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png'])
st.image('img/loveit_sample.jpg')
if uploaded_file is not None:
    #画像ファイルにalpha値が含まれているケースを回避するためrgb変換
    img = Image.open(uploaded_file).convert('RGB')

    #関数でファイルパスを指定するため読み込んだ画像を特定のフォルダに保存
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    # #描画(矩形)
    # draw = ImageDraw.Draw(img)
    # for object in objects:
    #     x = object.rectangle.x
    #     y = object.rectangle.y
    #     w = object.rectangle.w
    #     h = object.rectangle.h
    #     #object_propertyに変更されている
    #     # caption = object.object
    #     caption = object.object_property

    #     font = ImageFont.truetype(font='./Helvetica 400.ttf', size=30)
    #     text_w, text_h = draw.textsize(caption, font=font)

    #     draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=5)
    #     draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
    #     draw.text((x, y), caption, fill='white', font=font)

    # st.image(img)

    # tags_name = get_tags(img_path)
    # tags_name = ', '.join(tags_name)


    # st.markdown('**認識されたコンテンツタグ**')
    # st.markdown(f'>{tags_name}')




