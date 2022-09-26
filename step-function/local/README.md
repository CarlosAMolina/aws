## Introduction

Folder with files to run AWS Step Function locally.

## Requirements

The `Resources` section has links about how to install the following requirements.

- Docker.
- AWS CLI.
- AWS SAM CLI.

### Download de Docker image:

```bash
docker pull amazon/aws-stepfunctions-local
```

### Mock file

Some important notes about the `state-machine/test/MockConfigFile.json` file:

- The third line value is the created step function's name (specified in the `makefile` file).


## Run AWS SF Local

You must be in the same path as the `makefile` file.

Start a Docker container:

```bash
make run
```

With the previous Docker container running, open a new terminal and execute the command to create the step function and run the test:

```bash
make all
```

Note. If you receive this error:

```bash
An error occurred (StateMachineAlreadyExists) when calling the CreateStateMachine operation: State Machine Already Exists: 'arn:aws:states:us-east-1:123456789012:stateMachine:LocalTesting'
make: *** [makefile:10: create] Error 255
```

Or this one:

```bash
An error occurred (ExecutionAlreadyExists) when calling the StartExecution operation: Execution Already Exists: 'arn:aws:states:us-east-1:123456789012:execution:LocalTesting:CorrectTest'
make: *** [makefile:16: correct-test] Error 255
```

Stop the Docker container, repeat the steps explained in this section.

### Analyze results

In the terminal where you executed `make run` you can see all the step function logs.

In order to avoid read all the logs, we can filter the last step function log of each execution to check that it has the expected value. In the new terminal where you executed `make all` you can see these logs running `make history`.

## Resources

- AWS CLI. User values: <https://docs.dev.awshelena.es/books/aws/page/aws-cli---vdc>
- AWS SAM CLI. Install: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>
- AWS SF local. Download Docker image: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html>
- AWS SF local. Configure Docker credentials and start Docker image: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html>
- AWS SF local. Tutorial code: <https://github.com/mavi888/sam-stepfunctions-sdk-integration>
- AWS SF local. Tutorial video: <https://www.youtube.com/watch?v=P3hEqxKxZe8>
- Docker. Install Docker Engine: <https://docs.docker.com/engine/install/ubuntu/>.
- Docker. Configure Docker Engine to run Docker commands without `sudo`: <https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user>.