#!/bin/bash

# Bundle the dependencies
pip install -t bundle -r requirements.txt --upgrade

# Add function code to bundle
cp bot.py bundle
cp lambda_function.py bundle
cp words.json bundle

# Zip the bundle
cd bundle
zip -r ../bundle.zip *
cd ..

# Upload the bundle to S3
aws s3 cp bundle.zip s3://promptsbot

# Delete the bundle locally
rm -rf bundle bundle.zip

# Update the Lambda function
aws lambda update-function-code --function-name prompts --s3-bucket promptsbot --s3-key bundle.zip --region us-east-1
