import boto3
import pprint

REGION_NAME = "TODO"
STEP_FUNCTION_ARN = "TODO"
client = boto3.client("stepfunctions", region_name=REGION_NAME)
response = client.list_executions(
    stateMachineArn=STEP_FUNCTION_ARN,
    statusFilter="FAILED",
    maxResults=1,
)
execution = response["executions"][0]
start_datetime = execution["startDate"]
stop_datetime = execution["stopDate"]
pprint.pprint(response)
print(start_datetime, stop_datetime)
