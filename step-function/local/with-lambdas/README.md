## Introduction

Project to deploy a step function and lambdas locally.

## Requirements

- AWS SAM CLI
- AWS SF local Docker.
- Configure dummy AWS credentials if no configuration has been done yet:

```bash
echo -e "[default]\naws_access_key_id = foo\naws_secret_access_key = foo" > ~/.aws/credentials
```

## Run the project

First, create the app with SAM (see the `Resources` section).

Run the lambda:

```bash
cd sam-app
sam local start-lambda
```

Run the local step-function Docker:

```bash
cd ..
make run
```

Create the step-function:

```bash
make create
```

Invoke the step function:

```bash
make invoke 
```

## Resources

- Local lambda with SAM: see the folder `lambda/local/lambda-and-api` in this project. 

- Tutorial: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html#create-local-statemachine>
