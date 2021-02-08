#!/bin/bash
mkdir tmp
cp measureapi/* tmp/ -r
cd tmp/
pip3 install -r requirements.txt --target . 
zip -r ../app.zip *
cd ..
rm -rf tmp/