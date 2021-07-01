## Meme Generator

### an overview of the project.


Meme Generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote. Content - the quotes are spread in a variety of filetypes: PDF/DOCX/CSV/TXT. Application manipulates pictures by adding quote and author to it and save it to the disc.

Dynamic user input is accepted through command-line tool and web service.

Example picture:

![Alt text](./_data/example.jpeg?raw=true "Meme")

## Application was published under following link:
* [MemeGenerator](https://intense-bayou-36829.herokuapp.com/)

### instructions for setting up and running the program.

#### Installation:
  * clone repository
  * create virtual environment
  * install dependencies, all of them are listed in requirements txt 
  * install [Xpdf](https://www.xpdfreader.com/download.html)
  * run unittest [python -m3 unittest]

Application can run in two modes: command line & web mode.

### Command Line:

```
(venv) meme_genarator % python3 meme.py -h
usage: Meme Generator - add caption to pictures [-h] [--path PATH] [--body BODY] [--author AUTHOR]

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      path to an image file
  --body BODY      quote body to add to the image
  --author AUTHOR  quote author to add to the image
(venv) 
```

### Web App

Run application: 

```
(venv) meme_genarator % python3 app.py
```
open web browser, and go to localhost and port 5000.



### Quote Engine Module

The Quote Engine module is responsible for ingesting many types of files that contain quotes and store them in quote_model objects.

#### Ingestors
An abstract base class, IngestorInterface defines two methods:
```
def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```
Strategy objects realizes IngestorInterface for each file type (csv, docx, pdf, txt).

### Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images. It uses PIL module.

### Main application 

* meme.py - command line interface
* app.py - web application
