# Random Meme Generator
-----
## Overview
Meme Generator is a program that facilitates the creation of memes.

The script can be invoked from the command line:
```
python3 main.py 
```

The program optionally accepts three parameters:
--path - path to an image file
--body - quote body to add to the image
--author - quote author to add to the image

If none of these parameter are scpecified, the program will create a random image with a random quote.

## Tech Stack (Dependencies)
Our tech stack will include the following:
 * **Pandas** as a tool to manipulate .csv files
 * **Python Docs** as a tool to manipulate .docx files
 * **Pillow** as a tool to load and transform images
 * **Python3** and **Flask** as our server language and server framework
You can download and install the dependencies mentioned above using `pip` as:

```
pip install -r requirements.txt
```

## Main Files: Project Structure
```sh
├── README.md
├── main.py ** the main driver of the app. The memes are generated here.
├── app.py ** routing setup for web application.
├── MemeGenerator
│   ├── meme_generator.py **
│   └── Roboto-Light.ttf
├── QuoteEngine
│   ├── csvingestor.py
│   ├── docxingestor.py
│   ├── ingestor.py ** The class that consolidates all the parsers.
│   ├── ingestor_interface.py ** The Abstract Class that is used to structure individual parsers.
│   ├── pdfingestor.py
│   ├── quote.py ** This is where QuoteModel is created to represent quotes.
│   └── textingestor.py
├── _data
│   ├── DogQuotes
│   ├── SimpleLines
│   └── photos
│       └── dog
├── templates
├── tmp
└── venv
```
