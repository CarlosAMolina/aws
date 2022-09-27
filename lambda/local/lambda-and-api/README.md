## Introduction

This project deploys a lambda locally using SAM.

### Build

#### Change Python runtime

Before execute the `sam build` command, you can edit the `sam-app/template.yaml` file and set the desired `Runtime: pythonX.X` value.

### Test

#### Local

The AWS Docker must be configured.

After build with SAM, runt the app:

```bash
cd sam-app
sam local start-api
```

You can test the API accessing the following URL:

```bash
http://127.0.0.1:3000/hello
```

### Modify the lambda

You can edit the lambda without restart the execution by modifying the following file:

```bash
vi sam-app/.aws-sam/build/HelloWorldFunction/app.py
```


## Resources

- Install AWS SAM CLI
<https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>

- Tutorial
<https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html>
