# MindForger documentation build
#
# Generates https://www.mindforger.com/docs from the Markdown notebooks in memory/
# to distro/www.mindforger.com/docs - see build/sitemap.md for the site structure.
#
# Run: cd build && make doc  (or: make -C build doc)

ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)
BUILD := $(ROOT)/build
SOURCE := $(ROOT)/memory
DISTRO := $(ROOT)/distro
OUT := $(DISTRO)/www.mindforger.com/docs

PYTHON ?= python3
PORT ?= 8080

.DEFAULT_GOAL := help

.PHONY: help
help: ## show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: doc-deps
doc-deps:
	@$(PYTHON) -c "import markdown, pygments" 2>/dev/null \
		|| { echo "Error: Python 'markdown' and 'pygments' are required:"; \
		     echo "       pip3 install --user markdown pygments"; exit 1; }

.PHONY: doc-clean
doc-clean: ## purge the distro/ directory with generated documentation
	rm -rf $(DISTRO)
	@echo "DONE documentation cleaned"

.PHONY: doc
doc: doc-deps doc-clean ## generate HTML documentation from Markdown sources
	@echo "Generating documentation from Markdown..."
	$(PYTHON) $(BUILD)/make/generate_docs.py \
		--source-dir $(SOURCE) \
		--sitemap $(BUILD)/sitemap.md \
		--assets-dir $(BUILD)/assets \
		--output-dir $(OUT)
	@echo "DONE documentation generated to file://$(OUT)/index.html"

.PHONY: doc-check
doc-check: ## check generated documentation for broken links and images
	$(PYTHON) $(BUILD)/make/check_docs.py --output-dir $(OUT)

.PHONY: doc-live
doc-live: doc ## serve documentation locally for preview
	@echo "Serving documentation at http://localhost:$(PORT)"
	$(PYTHON) -m http.server $(PORT) --directory $(OUT)

.PHONY: doc-assets
doc-assets: ## download vendored web assets (Tabler, KaTeX, Lato) to build/assets
	$(PYTHON) $(BUILD)/make/download_assets.py --assets-dir $(BUILD)/assets

.PHONY: doc-upload-info
doc-upload-info: ## show what to upload to www.mindforger.com/docs
	@echo "Upload the content of the following directory to www.mindforger.com/docs:"
	@echo "  $(OUT)"
	@du -sh $(OUT) 2>/dev/null || echo "  (not generated yet - run 'make doc')"
