# Variables
UV = uv run
SPHINXBUILD = sphinx-build
SPHINXAUTOBUILD = sphinx-autobuild
SOURCEDIR = docs/source
BUILDDIR = docs/build/html

.PHONY: help install build dev clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install  - Instala las dependencias usando uv"
	@echo "  make build    - Genera la documentación HTML estática"
	@echo "  make dev      - Lanza el servidor con auto-refresco (Live Reload)"
	@echo "  make clean    - Borra la carpeta de compilación"

install:
	uv sync

build:
	$(UV) $(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)

dev:
	$(UV) $(SPHINXAUTOBUILD) $(SOURCEDIR) $(BUILDDIR) --open-browser

clean:
	rm -rf $(BUILDDIR)/*