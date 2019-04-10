parts = ["", "Alaf Lam Meem", "Sayaqool", "Tilkal Rusull", "Lan Tana Loo", "Wal Mohsanat", "La Yuhibbullah", "Wa Iza Samiu", "Wa Lau Annana", "Qalal Malao", "Wa A'lamu", "Yatazeroon", "Wa Mamin Da'abat", "Wa Ma Ubrioo", "Rubama", "Subhanallazi", "Qal Alam", "Aqtarabo", "Qadd Aflaha", "Wa Qalallazina", "A'man Khalaq", "Utlu Ma Oohi", "Wa Manyaqnut", "Wa Mali", "Faman Azlam", "Elahe Yuruddo", "Ha'a Meem", "Qala Fama Khatbukum", "Qadd Sami Allah", "Tabarakallazi", "Amma Yatasa'aloon", "Tajweed Rules", "Color Coded Tajweed Rules", "", ""]

chapters = ["", "Al-Fatihah (The Opening)", "Al-Baqarah (The Cow)", "Al-'Imran (The Family of Amran)", "An-Nisa' (The Women)", "Al-Ma'idah (The Food)", "Al-An'am (The Cattle)", "Al-A'raf (The Elevated Places)", "Al-Anfal (Voluntary Gifts)", "Al-Bara'at / At-Taubah(The Immunity)", "Yunus (Jonah)", "Hud (Hud)", "Yusuf (Joseph)", "Ar-Ra'd (The Thunder)", "Ibrahim (Abraham)", "Al-Hijr (The Rock)", "An-Nahl (The Bee)", "Bani Isra'il (The Israelites)", "Al-Kahf (The Cave)", "Maryam (Mary)", "Ta Ha (Ta Ha)", "Al-Anbiya' (The Prophets)", "Al-Hajj (The Pilgrimage)", "Al-Mu'minun (The Believers)", "An-Nur (The Light)", "Al-Furqan (The Discrimination)", "Ash-Shu'ara' (The Poets)", "An-Naml (The Naml)", "Al-Qasas (The Narrative)", "Al-'Ankabut (The Spider)", "Ar-Rum (The Romans)", "Luqman (Luqman)", "As-Sajdah (The Adoration)", "Al-Ahzab (The Allies)", "Al-Saba' (The Saba')", "Al-Fatir (The Originator)", "Ya Sin (Ya Sin)", "As-Saffat (Those Ranging in Ranks)", "Sad (Sad)", "Az-Zumar (The Companies)", "Al-Mu'min (The Believer)", "Ha Mim (Ha Mim)", "Ash-Shura (Counsel)", "Az-Zukhruf (Gold)", "Ad-Dukhan (The Drought)", "Al-Jathiyah (The Kneeling)", "Al-Ahqaf (The Sandhills)", "Muhammad (Muhammad)", "Al-Fath (The Victory)", "Al-Hujurat (The Apartments)", "Qaf (Qaf)", "Ad-Dhariyat (The Scatterers)", "At-Tur (The Mountain)", "An-Najm (The Star)", "Al-Qamar (The Moon)", "Ar-Rahman (The Beneficent)", "Al-Waqi'ah (The Event)", "Al-Hadid (Iron)", "Al-Mujadilah (The Pleading Woman)", "Al-Hashr (The Banishment)", "Al-Mumtahanah (The Woman who is Examined)", "As-Saff (The Ranks)", "Al-Jumu'ah (The Congregation)", "Al-Munafiqun (The Hypocrites)", "At-Taghabun (The Manifestation of Losses)", "At-Talaq (Divorce)", "At-Tahrim (The Prohibition)", "Al-Mulk (The Kingdom)", "Al-Qalam (The Pen)", "Al-Haqqah (The Sure Truth)", "Al-Ma'arij (The Ways of Ascent)", "Nuh (Noah)", "Al-Jinn (The Jinn)", "Al-Muzzammil (The One Covering Himself)", "Al-Muddaththir (The One Wrapping Himself Up)", "Al-Qiyamah (The Resurrection)", "Al-Insan (The Man)", "Al-Mursalat (Those Sent Forth)", "An-Naba' (The Announcement)", "An-Nazi'at (Those Who Yearn)", "'Abasa (He Frowned)", "At-Takwir (The Folding Up)", "Al-Infitar (The Cleaving)", "At-Tatfif (Default in Duty)", "Al-Inshiqaq (The Bursting Asunder)", "Al-Buruj (The Stars)", "At-Tariq (The Comer by Night)", "Al-A'la (The Most High)", "Al-Ghashiyah (The Overwhelming Event)", "Al-Fajr (The Daybreak)", "Al-Balad (The City)", "Ash-Shams (The Sun)", "Al-Lail (The Night)", "Ad-Duha (The Brightness of the Day)", "Al-Inshirah (The Expansion)", "At-Tin (The Fig)", "Al-'Alaq (The Clot)", "Al-Qadr (The Majesty)", "Al-Bayyinah (The Clear Evidence)", "Al-Zilzal (The Shaking)", "Al-'Adiyat (The Assaulters)", "Al-Qari'ah (The Calamity)", "At-Takathur (The Abundance of Wealth)", "Al-'Asr (The Time)", "Al-Humazah (The Slanderer)", "Al-Fil (The Elephant)", "Al-Quraish (The Quraish)", "Al-Ma'un (Acts of Kindness)", "Al-Kauthar (The Abundance of Good)", "Al-Kafirun (The Disbelievers)", "An-Nasr (The Help)", "Al-Lahab (The Flame)", "Al-Ikhlas (The Unity)", "Al-Falaq (The Dawn)", "An-Nas (The Human)", "", ""]

pages_of_chapters = [0,2,3,51,78,107,129,152,178,188,209,222,236,250,256,262,268,283,294,306,313,323,332,343,351,360,367,377,386,397,405,412,416,419,429,435,441,446,453,459,468,478,484,490,496,499,503,507,512,516,519,521,524,527,529,532,535,538,543,546,550,552,554,555,557,559,561,563,565,568,570,572,574,577,579,581,583,585,587,588,590,591,592,593,595,596,597,598,598,599,601,601,602,603,603,604,604,605,605,606,606,607,607,608,608,608,609,609,609,609,610,610,610,611,611, 999, 999]

pages_of_parts = [0, 3, 23, 43, 63, 83, 103, 123, 143, 163, 183, 203, 223, 243, 263, 283, 303, 323, 343, 363, 383, 403, 423, 443, 463, 483, 503, 523, 543, 563, 587, 1, 28, 999, 999]

print(r"""\documentclass{book}
\usepackage[margin=0mm,landscape,a3paper]{geometry}
\usepackage{graphicx}
\usepackage{etoolbox}
\makeatletter
\def\ifGm@preamble#1{\@firstofone}
\appto\restoregeometry{%
	\pdfpagewidth=\paperwidth
	\pdfpageheight=\paperheight}
\apptocmd\newgeometry{%
	\pdfpagewidth=\paperwidth
	\pdfpageheight=\paperheight}{}{}
\makeatother
\usepackage[open=true]{bookmark}
\begin{document}
\centering
\newgeometry{margin=0mm,portrait,a4paper}
\bookmark[level=1,page=1]{Cover Page}
\includegraphics[height=.999\textheight,width=\textwidth]{images/cover.jpg}
\newpage
\restoregeometry""")

page, real_page = 2, 2
chapter_index, part_index = 1, 1

while page <= 612:
	print(r"""\includegraphics[height=.999\textheight]{"""+"images/img-{:03d}.jpg".format(page+28)+r"}")
	while abs(page - pages_of_chapters[chapter_index]) == 0:
		print(r"""\bookmark[level=1,page="""+str(real_page)+r"""]{Surah-"""+ "{:03d}. {}".format(chapter_index, chapters[chapter_index]) +r"""}""")
		chapter_index += 1
	while abs(page - pages_of_parts[part_index]) < 2:
		print(r"""\bookmark[level=0,page="""+str(real_page)+r"""]{Para-"""+ "{:02d}: {}".format(part_index, parts[part_index]) +r"""}""")
		part_index += 1
	while abs(page - pages_of_chapters[chapter_index]) == 1:
		print(r"""\bookmark[level=1,page="""+str(real_page)+r"""]{Surah-"""+ "{:03d}. {}".format(chapter_index, chapters[chapter_index]) +r"""}""")
		chapter_index += 1
	print(r"""\includegraphics[height=.999\textheight]{"""+"images/img-{:03d}.jpg".format(page+27)+r"}")
	print(r'\newpage')
	page += 2
	real_page += 1

########## Start Other pages ###########
page = 2

while page <= 28:
	print(r"""\includegraphics[height=\textheight]{"""+"images/img-{:03d}.jpg".format(page)+r"}")
	while abs(page - pages_of_parts[part_index]) < 2:
		print(r"""\bookmark[level=0,page="""+str(real_page)+r"""]{"""+ "{}".format(parts[part_index]) +r"""}""")
		part_index += 1
	print(r"""\includegraphics[height=\textheight]{"""+"images/img-{:03d}.jpg".format(page - 1)+r"}")
	print(r'\newpage')
	page += 2
	real_page += 1

print(r"""\end{document}""")
