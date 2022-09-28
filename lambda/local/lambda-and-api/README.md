## Introduction

This project deploys a lambda locally using SAM.

### Build

```bash
sam init # Select options `1 - AWS Quick Start...`, `1 - Hello World Example`, answer yes to the question `Use the most popular runtime ... (Python and zip)` and default answer for the rest of questions.
cd sam-app
# `vi template.yaml` if you want to modify Runtime Python version.
sam build
```

As the comments show, before execute the `sam build` command, you can edit the `sam-app/template.yaml` file and set the desired `Runtime: pythonX.X` value.

### Test

#### Local

##### Run API

After build with SAM, runt the app:

```bash
cd sam-app
sam local start-api
```

You can test the API accessing the following URL:

```bash
http://127.0.0.1:3000/hello
```

Or you can call the lambda directly:

```bash
sam local invoke "HelloWorldFunction" -e events/event.json
```

##### Run Lambda

```bash
sam local start-lambda
sam local invoke "HelloWorldFunction" -e events/event.json
```

### Modify the lambda

You can edit the lambda without restart the execution by modifying the following file:

```bash
vi sam-app/.aws-sam/build/HelloWorldFunction/app.py
```

## Resources

- Install AWS SAM CLI
  - <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>

- Tutorial
  - <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>
  - <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html>
