PYTHON		= python3
MAIN_SCRIPT	= gen_tex.py
PDFLATEX	= pdflatex
OUTPUT_NAME	= Al-Quran



$(OUTPUT_NAME).pdf: $(OUTPUT_NAME).tex images/*
	$(PDFLATEX) $(OUTPUT_NAME).tex

$(OUTPUT_NAME).tex: $(MAIN_SCRIPT)
	$(PYTHON) $(MAIN_SCRIPT) > $(OUTPUT_NAME).tex


.PHONY: clean
clean:
	-rm $(OUTPUT_NAME).*
