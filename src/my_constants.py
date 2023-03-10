import os
import json
addon_id = 'myaddon2'
try:
    # * Generate an error in this block whenever you are running GUI dialog outside the anki
    # ewr
    from aqt import mw
    root_dir = os.path.join(mw.pm.addonFolder(), addon_id)

except:
    from warnings import warn
    warn("Running code outside anki")
    root_dir = os.path.join(
        r"C:\Users\amanr\AppData\Roaming\Anki2\addons21", addon_id)


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