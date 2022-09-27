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

correct-test-path-1:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name CorrectTestPath1 \
		--input file://state-machine/test/input-path-1.json \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:LocalTesting#CorrectPathTest

correct-test-path-2:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name CorrectTestPath2 \
		--input file://state-machine/test/input-path-2.json \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:LocalTesting#CorrectPathTest

correct-test-path-not-managed:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name CorrectTestPathNotManaged \
		--input file://state-machine/test/input-path-not-managed.json \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:LocalTesting#CorrectPathTest

all: create correct-test-path-1 correct-test-path-2 correct-test-path-not-managed

correct-test-path-1-h:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:LocalTesting:CorrectTestPath1 \
		--query 'events[?type==`ExecutionSucceeded`]'

correct-test-path-2-h:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:LocalTesting:CorrectTestPath2 \
		--query 'events[?type==`ExecutionSucceeded`]'

correct-test-path-not-managed-h:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:LocalTesting:CorrectTestPathNotManaged \
		--query 'events[?type==`ExecutionSucceeded`]'

history: correct-test-path-1-h correct-test-path-2-h correct-test-path-not-managed-h