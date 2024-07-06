LATEX=pdflatex
LATEXOPTS=--halt-on-error --shell-escape --file-line-error --interaction=nonstopmode

MAIN = regular_polygon

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(LATEXOPTS) $(MAIN).tex
	$(LATEX) $(LATEXOPTS) $(MAIN).tex
	$(LATEX) $(LATEXOPTS) $(MAIN).tex

clean:
	rm -f *.pdf *.log *.aux *.toc *.out

.PHONY: all clean
