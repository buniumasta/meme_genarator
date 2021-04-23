### Meme Generator
![meme_genarator](https://github.com/buniumasta/meme_genarator/actions/workflows/main.yml/badge.svg)

A multimedia application to dynamically generate memes, including an image with an overlaid quote. Content - the quotes are spread in a variety of filetypes: PDF/DOCX/CSV/TXT. Appliction manipulates pictures by adding quote and author to picture and save it to the disc.

Dynamic user input is accepted through command-line tool and web service

## Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes: body and author.

## Ingestors
An abstract base class, IngestorInterface defines two methods:
```def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```
Strategy objects realizes IngestorInterface for each file type (csv, docx, pdf, txt).

## Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images. It uses PIL module.
