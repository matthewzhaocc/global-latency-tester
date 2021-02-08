#!/bin/bash
mkdir tmp
cp render-htmlpage/* tmp/ -r
cd tmp/
zip -r ../ui.zip *
cd ..
rm -rf tmp/