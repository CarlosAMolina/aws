ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	LAMBDA_REMOTE_DOCKER=0 localstack start

create:
	awslocal lambda create-function --function-name foo-function \
		--code S3Bucket="__local__",S3Key="$(ROOT_DIR)/src/" \
		--handler lambda_handler.lambda_handler \
		--runtime python3.8 \
		--role cool-stacklifter

invoke:
	awslocal lambda invoke \
		--function-name foo-function \
		--payload '{"file_path": "/foo/bar"}' \
		src/output.txt

all: create invoke
