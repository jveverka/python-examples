#!/usr/bin/env python3

import time
import torch
import json
import os
import argparse

parser = argparse.ArgumentParser(
                    prog = 'image-recognizer',
                    description = 'Recognize objects in set of images in given folder.',
                    epilog = '.')
parser.add_argument('-d', '--imagedir', type = str, required = True)
args = parser.parse_args()

root_path = args.imagedir
result_set = []

# Load Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

def transform_results(json_string):
    data = json.loads(json_string)
    results = []
    indices = data["xmin"].keys()
    for index in indices:
        result = {}
        result["index"] = index
        result["xmin"] = data["xmin"][index]
        result["ymin"] = data["ymin"][index]
        result["xmax"] = data["xmax"][index]
        result["ymax"] = data["ymax"][index]
        result["confidence"] = data["confidence"][index]
        result["class"] = data["class"][index]
        result["name"] = data["name"][index]
        results.append(result)
    return results

def list_files(dir_root_path):
    dir_list = os.listdir(dir_root_path)
    for dir_item in dir_list:
       full_path = dir_root_path + "/" + dir_item
       #print("path: " + full_path)
       if os.path.isdir(full_path):
          list_files(full_path)
       elif os.path.isfile(full_path):
          print("processing file: " + full_path)
          file_name, file_extension = os.path.splitext(full_path)
          if file_extension.upper() == ".JPG" or file_extension.upper() == ".JPEG" :
             start = time.time()
             results = model(full_path)
             transformed_results = transform_results(results.pandas().xyxy[0].to_json())
             print("RESULT: " + str(transformed_results))
             duration = time.time() - start
             result_set.append({ "path": full_path, "annotations": transformed_results, "duration": duration })
          else:
             print("ERROR: unsupported file extension: " + file_extension)
       else:
          print("ERROR: unsupported file type: " + full_path)


list_files(root_path)

class_counter = {}
for result in result_set:
    for item in result["annotations"]:
       class_name = item["name"]
       if class_name in class_counter:
          class_counter[class_name] = class_counter[class_name] + 1
       else:
          class_counter[class_name] = 1

print("FINAL RESULTS:")
print(str(class_counter))
