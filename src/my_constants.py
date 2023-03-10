from aqt import mw
import os
addon_id = 'myaddon2'
root_dir = os.path.join(mw.pm.addonFolder(), addon_id)
logs_dir = os.path.join(root_dir, "logs")
style_sheets_dir = os.path.join(root_dir, "user_files")
style_sheet_to_use = "default.css"
