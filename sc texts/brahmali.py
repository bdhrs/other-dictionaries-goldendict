import re
import os

vin_dir = "/home/bhikkhu/git/Tipitaka-Pali-Projector/tipitaka_projector_data/pali/"

vin_dict = {
	"1. Pārājika":"11010a.js",
	"2. Pācittiya": "11020a.js",
	"3. Mahāvagga": "11030a.js",
	"4. Cūḷavagga": "11040a.js",
	"5. Parivāra": "11050a.js"
	}

with open("vinaya.css") as c:
	css = c.read()

for book_name, vin_file in vin_dict.items():
	with open(f"{vin_dir}{vin_file}") as r:

		text = r.read()
		text = text.replace("var P_HTM = [];", "")
		text = re.sub("""P_HTM.*"\\*""", "", text)
		text = text.replace("""* **";""", "\n")
		text = text.replace("""**""", "\n")
		text = text.replace("""*";""", "\n")

		output_dir = "output/"
		output_path = f"{output_dir}{book_name}.txt"

		try:
			os.mkdir(output_dir)
		except:
			pass

		with open(output_path, "w") as w:
			w.write(text)

		# html formatting
		text = re.sub("\\n\\n(.+)", "\n\n<p class='pali'>\\1</p>", text)
		text = re.sub("</p>\\n(.+)", "</p>\\n<p class='english'>\\1</p>", text)
		text = css + text

		output_path = f"{output_dir}{book_name}.html"
		
		with open(output_path, "w") as w:
			w.write(text)

