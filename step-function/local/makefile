ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	docker run -p 8083:8083 \
	--mount type=bind,readonly,source=$(ROOT_DIR)/state-machine/test/MockConfigFile.json,destination=/home/StepFunctionsLocal/MockConfigFile.json \
	-e SFN_MOCK_CONFIG="/home/StepFunctionsLocal/MockConfigFile.json" \
	amazon/aws-stepfunctions-local
