cd "$(dirname "$0")"
sphinx-apidoc -o . ../sampledbapi -f -P -M -e
sphinx-build -b html . _build
# sphinx-build -b latex . _build
# make latexpdf
