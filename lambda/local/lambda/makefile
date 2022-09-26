ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	LAMBDA_REMOTE_DOCKER=0 localstack start

create:
	awslocal lambda create-function --function-name my-cool-local-function \
		--code S3Bucket="__local__",S3Key="$(ROOT_DIR)/src/" \
		--handler lambda_handler.lambda_handler \
		--runtime python3.8 \
		--role cool-stacklifter

invoke:
	awslocal lambda invoke \
		--function-name my-cool-local-function \
		--payload '{"foo": "bar"}' \
		src/output.txt

all: create invoke
