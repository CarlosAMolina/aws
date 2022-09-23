ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	docker run --rm -p 8083:8083 \
	--mount type=bind,readonly,source=$(ROOT_DIR)/state-machine/test/MockConfigFile.json,destination=/home/StepFunctionsLocal/MockConfigFile.json \
	-e SFN_MOCK_CONFIG="/home/StepFunctionsLocal/MockConfigFile.json" \
	amazon/aws-stepfunctions-local

create:
	aws stepfunctions create-state-machine \
		--endpoint-url http://localhost:8083 \
		--definition file://state-machine/state-machine.asl.json \
		--name "LocalTesting" --role-arn "arn:aws:iam::123456789012:role/DummyRole"

correct-test:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name CorrectTest \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:LocalTesting#CorrectTest

all: create correct-test