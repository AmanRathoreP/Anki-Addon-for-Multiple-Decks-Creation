<div align="center">
  <h1>Anki Multiple decks creator - v1.1.0</h1>
</div>

<p align="center">
  This addon helps user to create multiple empty decks at once.
  <!-- TODO add some of the github badges and shields-->
</p>


## Features

* Can use to create multiple decks from and external file
* Interactive GUI
* Support for importing multiple files form different location
  * Can be imported using drag and drop
  * Can be imported using the selection menu
* Selection of multiple themes
  * Can specify custom theme
* Works with QT5 as well as QT6

## Quick start

### via anki downloader (_Recommended_)
Copy the following addon id and download it 
```bash
461193445
```
> NOTE: This is the [anki homepage](https://ankiweb.net/shared/info/461193445) for the addon.
### via custom download
- Step 1.) Download the latest version of the addon by seeing the release section
- Step 2.) Place the addon files into the anki addon folder
- Step 3.) ... __TODO__

### About the files
```
📦root                              # this is your addon folder where all the addon files are stored
 ┣ 📂logs                           # contains some log files
 ┃ ┣ 📜logs.log                     # the file in which data is logged(this will probably not exists in your addon)
 ┃ ┗ 📜README.md                    # contains some information about that specific folder
 ┣ 📂src                            # contains some files used by the addon
 ┃ ┣ 📜my_constants.py              # contains constants which are used all over the addon
 ┃ ┣ 📜my_logger.py                 # contain the logger which logs some information during development stage
 ┃ ┗ 📜my_user_interactive_GUI.py   # can be run independently and has all the code to display the dialog for input
 ┣ 📂user_files                     # this folder mainly contains the css files for the addon's GUI
 ┃ ┣ 📜default.css                  # a css file for the addon
 ┃ ┗ 📜README.md                    # contains some information about that specific folder
 ┣ 📜.gitignore                     # contains information about the files which are not tracked by version control system
 ┣ 📜config.json                    # file for the user from which user can tik and tweak the addon settings
 ┣ 📜config.md                      # file for the user 
 ┣ 📜main.py                        # responsible for all the master execution of code of addon (all stuff of this file is directly imported to the 📜__init__.py)
 ┣ 📜README.md                      # contains whole documentation of the addon
 ┣ 📜_version.py                    # contains version information about the addon
 ┗ 📜__init__.py                    # file for initialization of the addon and Anki only looks for this file
```

## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](issues.md)

Thank you for considering contributing to Anki Multiple decks creator!

First note we have a code of conduct, please follow it in all your interactions with the program files.

We welcome any type of contribution, _not only code_. You can help with:
- **QA**: File bug reports, the more details you can give the better (e.g. images or videos)
- **New Features**: You can suggest an modifications or just ask for advancements in the old features of addon.
- **Code**: Take a look at the [open issues](issues.md). Even if you can't write the code yourself, you can comment on them, showing that you care about a given issue matters. It helps us to handel them.

## Demo
### You can download the file shown in the below demo from from [here](https://github.com/AmanRathoreP/AmanRathoreP/blob/main/Files/Multiple%20decks%20creator%20example%20files.zip). Note that these files are separated with ``` `` ```

![img1](https://github.com/AmanRathoreP/AmanRathoreP/blob/main/imgs/multiple_decks_creator_img_1.png)
![img2](https://github.com/AmanRathoreP/AmanRathoreP/blob/main/imgs/multiple_decks_creator_img_2.png)
![gif1](https://github.com/AmanRathoreP/AmanRathoreP/blob/main/imgs/multi_decks_creator.gif)

## Author

- [@Aman](https://www.github.com/AmanRathoreP)
   - [GitHub](https://www.github.com/AmanRathoreM)
   - [Telegram](https://t.me/aman0864)
   - Email -> *aman.proj.rel@gmail.com*
## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2023, Aman Rathore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
