import pandas as pd

df = pd.read_csv("/home/bhikkhu/Bodhirasa/Dropbox/dpd/other dictionaries/peu/peu 22-01-22", sep = "\t", header=None)
df.fillna("", inplace=True)

df.insert(2, "definition_plain", "")
df.insert(3, "synonyms", "")
df.rename({0:"word", 1:"definition_html"}, axis='columns', inplace=True)

df.to_json("output/peu.json", force_ascii=False, orient="records", indent=5)

print(df)

from typing import List
from pathlib import Path
from simsapa.app.stardict import export_words_as_stardict_zip, ifo_from_opts, DictEntry
import json

zip_path = Path("./output/peu.zip")

with open("output/peu.json", "r") as gd_data:
    data_read = json.load(gd_data)

def item_to_word(x):
    return DictEntry(
        word=x["word"],
        definition_html=x["definition_html"],
        definition_plain=x["definition_plain"],
        synonyms=x["synonyms"],
    )

words = list(map(item_to_word, data_read))

ifo = ifo_from_opts(
    {
        "bookname": "Pāḷi Myanmar Abhidhan",
        "author": "Pāḷi Myanmar Abhidhan",
        "description": "Pāḷi Myanmar Abhidhan, translated into English. Version 2022-01-22.",
        "website": "https://github.com/bksubhuti/Tipitaka-Pali-Projector",
    }
)

export_words_as_stardict_zip(words, ifo, zip_path)
