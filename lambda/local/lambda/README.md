## Introduction

This project deploys a lambda locally using LocalStack.

## Requirements

Install the `requirements.txt` file:

```bash
pip install -r requirementst.txt
```

## Run lambda

Init LocalStack:

```bash
make run
```

In a new terminal, create the lambda function:

```bash
make create
```

Invoke the lambda function:

```bash
make invoke
```

You can modify the `src/lambda_handle.py` file and invoke the lambda without creating it again.

The lambda's output is stored in the `src/output.txt` file, its value must be `{"result":"/foo/bar"}`.

Note. When I run the previous commands, the terminal where I executed the `make run` command shows `WARN --- [uest_thread)] l.utils.docker_utils       : Error while performing automatic host path replacement for path '/home/user/aws/lambda/local/lambda/src/' to source '/home/user/.cache/localstack/volume'`, despite that, the lamba is executed correctly.

## Resources

- LocalStack CLI: <https://docs.localstack.cloud/get-started/#localstack-cli>
- Create lambda with LocalSatck: <https://docs.localstack.cloud/tools/lambda-tools/hot-swapping/>