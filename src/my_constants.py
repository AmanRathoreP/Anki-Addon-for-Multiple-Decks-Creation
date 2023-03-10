import os
import json

root_dir = os.path.dirname(os.path.dirname(__file__))

logs_dir = os.path.join(root_dir, "logs")
style_sheets_dir = os.path.join(root_dir, "user_files")

with open(os.path.join(root_dir, "meta.json"), 'r') as f:
    meta = json.load(f)

with open(os.path.join(root_dir, "config.json"), 'r') as f:
    config = json.load(f)

try:
    style_sheet_to_use = meta["config"]["style_sheet_to_use"]
    use_external_style_sheet = meta["config"]["use_external_style_sheet"]
except:
    style_sheet_to_use =config["style_sheet_to_use"]
    use_external_style_sheet =config["use_external_style_sheet"]