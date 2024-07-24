import os
import json

from aqt.qt import qtmajor

if qtmajor == 5:
    qt_version = 5
else:
    qt_version = 6

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