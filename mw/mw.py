#!/usr/bin/env python3.10
# coding: utf-8

import json
from simsapa.app.stardict import export_words_as_stardict_zip, ifo_from_opts, DictEntry
from pathlib import Path
from typing import List
import os
from bs4 import BeautifulSoup
import pandas as pd
import re

mw_dict = {}
counter = 0

with open("mw.css", "r") as c:
	css = c.read()

with open(f"xml/mw.xml") as f:
	soup = BeautifulSoup(f, "xml")

print(soup.key1)


# for filename in os.listdir("xml"):

# 	with open(f"xml/{filename}") as f:
# 		soup = BeautifulSoup(f, "xml")
# 		root = str(soup.h2)
# 		if re.findall("√", root):
# 			html = css
# 			html += str(soup.h2)
# 			root = re.sub("<h2>(.+?)(<| |\\().+", "\\1", str(root))
# 			root_clean = re.sub("√", "", root)
# 			root_clean = re.sub("\d", "", root_clean)
# 			try:
# 				for child in soup.h2.next_siblings:
# 					html += str(child)
# 				html += "<br><br>"
# 			except:
# 				print(f"{filename} has no <h2> ")
# 			html += "</body></html>"
# 			whitney_dict[root] = {"definition_html": html,
#                          "definition_plain": "", "synonyms": [root_clean]}

# whitney_df = pd.DataFrame.from_dict(whitney_dict, orient='index')
# whitney_df.reset_index(inplace=True)
# whitney_df.rename({"index": "word"}, axis='columns', inplace=True)
# whitney_df.to_csv("output/whitney.csv", sep="\t", index=None)
# whitney_df.to_json("output/whitney.json", force_ascii=False,
#                    orient="records", indent=5)

# zip_path = Path("./output/whitney.zip")

# with open("output/whitney.json", "r") as gd_data:
#     data_read = json.load(gd_data)


# def item_to_word(x):
#     return DictEntry(
#         word=x["word"],
#         definition_html=x["definition_html"],
#         definition_plain=x["definition_plain"],
#         synonyms=x["synonyms"],
#     )


# words = list(map(item_to_word, data_read))

# ifo = ifo_from_opts(
#     {
#         "bookname": "Whitney Sanskrit Roots",
#         "author": "William Dwight Whitney",
#         "description": "The Roots, Verb-Forms and Primary Derivatives of the Sanskrit Language by William Dwight Whitney. Trübner & Co, London, 1895. Encoded by Bodhirasa 2022",
#         "website": "",
#     }
# )

# export_words_as_stardict_zip(words, ifo, zip_path)
