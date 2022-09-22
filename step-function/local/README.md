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

## Run AWS SF Local

You must be in the same path as the `makefile` file.

Start a Docker container:

```bash
make run
```

With the previous Docker container running, open a different terminal and create the step function:

```bash
make create
```

## Resources

- AWS CLI. User values: <https://docs.dev.awshelena.es/books/aws/page/aws-cli---vdc>
- AWS SAM CLI. Install: <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>
- AWS SF local. Download Docker image: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html>
- AWS SF local. Configure Docker credentials and start Docker image: <https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html>
- AWS SF local. Tutorial code: <https://github.com/mavi888/sam-stepfunctions-sdk-integration>
- AWS SF local. Tutorial video: <https://www.youtube.com/watch?v=P3hEqxKxZe8>
- Docker. Install Docker Engine: <https://docs.docker.com/engine/install/ubuntu/>.
- Docker. Configure Docker Engine to run Docker commands without `sudo`: <https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user>.