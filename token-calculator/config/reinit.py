# -*- coding: utf-8 -*-
from tiktoken.model import MODEL_TO_ENCODING
import json
import os


class ConfigOpenAI:
  all_model: list[str] = []
  all_encoding: list[str] = []
  encodingToModel = {v: k for k, v in MODEL_TO_ENCODING.items()}


def reinitOpenAIConfig():
  print("start: 重新生成 openai.json ....")


  list_model = list(MODEL_TO_ENCODING.keys())
  list_encoding = list(set(MODEL_TO_ENCODING.values()))
  print(f"\t{len(list_model)}个模型、{len(list_encoding)}个编码:    {list_encoding}")

  encoding_map_model : dict[str, list[str]] = {}
  for model,encode in MODEL_TO_ENCODING.items():
    if encoding_map_model.get(encode) is None:
      encoding_map_model[encode] = list()
    encoding_map_model[encode].append(model)
  
  # 准备输出数据
  output_data = {
    "all_model": list_model,
    "all_encoding": list_encoding,
    "encoding_map_model": encoding_map_model,
  }

  # 确保config目录存在
  config_dir = os.path.dirname(os.path.abspath(__file__))
  output_file = os.path.join(config_dir, "openai.json")
  
  # 写入JSON文件
  with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)
  
  print("end: 重新生成 openai.json")



reinitOpenAIConfig()
