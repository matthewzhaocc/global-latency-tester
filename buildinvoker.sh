#!/bin/bash
mkdir tmp
cp invokeAPIs/* tmp/ -r
cd tmp/
pip3 install -r requirements.txt --target . 
zip -r ../invoker.zip *
cd ..
rm -rf tmp/