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

First, create and start the lambda with SAM locally:

```bash
sam init # Select options `1 - AWS Quick Start...`, `1 - Hello World Example`, answer yes to the question `Use the most popular runtime ... (Python and zip)` and default answer for the rest of questions.
cd sam-app
# `vi template.yaml` if you want to modify Runtime Python version.
sam build
sam local start-lambda
```

In a new terminal, run the local step-function Docker:

```bash
cd ..
make run
```

In a new terminal, create the step-function:

```bash
make create
```

Invoke the step function:

```bash
make invoke 
```

## Resources

- Local lambda with SAM:
    - <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>
    - <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html>

- Tutorial: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html#create-local-statemachine>
