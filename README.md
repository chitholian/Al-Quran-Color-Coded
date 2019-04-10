
# Al-Quran Color Coded
This project is intended to create a `pdf` file from existing images scanned from a hard-copy of the Holly Quran.

## Features
- 15 Lines Per Page.
- Hafezi Quran.
- Color Coded.
- Tajweed Rules.
- Index of Chapters (Surah List).
- Index of Juz (Para List).
- Dual Page View (On a Landscape Page).

## Building

You need `make`, `python3`, `pdflatex` installed to build the intended PDF file.

- For Fedora and its derivatives:

```
sudo dnf install make python3 texlive-latex
```

- For Ubuntu and its derivatives:

```
sudo apt install make python3 texlive-latex
```

- From the project root directory run:

```
make
```

It should create a file named `Al-Quran.pdf` in the same directory. Open it with your favourite PDF viewer.

- To clean the project directory run:

```
make clean
```
