import pandas as pd

df = pd.read_json("/home/bhikkhu/Bodhirasa/Dropbox/dpd/other dictionaries/cpd/en-critical.json")

# replacements
print("regex find and replace")
df.replace("I", "l", inplace=True, regex=True)
df.replace("<br\\/>", "", inplace=True, regex=True)
df.replace("rh", "ṁ", inplace=True, regex=True)
df.replace("ç", "ś", inplace=True, regex=True)


df.drop(labels=2, inplace=True, axis=1)

df.insert(2, "definition_plain", "")
df.insert(3, "synonyms", "")
df.rename({0:"word", 1:"definition_html"}, axis='columns', inplace=True)

df.to_json("output/cpd.json", force_ascii=False, orient="records", indent=5)

print(df)

from typing import List
from pathlib import Path
from simsapa.app.stardict import export_words_as_stardict_zip, ifo_from_opts, DictEntry
import json

zip_path = Path("./output/cpd.zip")

with open("output/cpd.json", "r") as gd_data:
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
        "bookname": "Critical Pāli Dictionary",
        "author": "V. Trenckner et al.",
        "description": "Critical Pāli Dictionary. encoded by Bodhirasa",
        "website": "https://cpd.uni-koeln.de",
    }
)

export_words_as_stardict_zip(words, ifo, zip_path)
