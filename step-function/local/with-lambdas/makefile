run:
	docker run \
		--rm \
		-p 8083:8083 \
		--network="host" \
		--env-file aws-stepfunctions-local-credentials.txt \
		amazon/aws-stepfunctions-local

create:
	aws stepfunctions create-state-machine \
		--endpoint-url http://localhost:8083 \
		--definition file://state-machine/state-machine.asl.json \
		--name "HelloWorld" \
		--role-arn "arn:aws:iam::123456789012:role/DummyRole"

invoke:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name test \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:HelloWorld 
