import logging
import pathlib


"""https://realpython.com/python-logging/#using-handlers"""
# Create a custom logger
logger = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(str(pathlib.Path.cwd().joinpath("src/lambda-log.log")))
# TODO fix logger, log.info logs are not created.
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.info("test")
logger.warning("test")


def lambda_handler(event: dict, context):
    logger.error("Init lambda")
    logger.info(f"Event: {event}")
    response = {"result": "foo"}
    logger.info(f"Output: {response}")
    return response


if __name__ == "__main__":
    lambda_handler({"foo":"bar"}, None)