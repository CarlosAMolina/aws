import logging
import pathlib


def get_logger():
    """https://realpython.com/python-logging/#using-handlers"""
    logging_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging_level = logging.INFO
    logging_file_pathname = str(pathlib.Path.cwd().joinpath("src/lambda-log.log"))
    logging.basicConfig(
        level=logging_level,
        format=logging_format,
    )
    # Create a custom logger
    logger = logging.getLogger(__name__)
    # Create handlers
    f_handler = logging.FileHandler(logging_file_pathname, mode="w")
    f_handler.setLevel(logging_level)
    # Create formatters and add it to handlers
    f_format = logging.Formatter(logging_format)
    f_handler.setFormatter(f_format)
    # Add handlers to the logger
    logger.addHandler(f_handler)
    return logger


def lambda_handler(event: dict, context):
    logger = get_logger()
    logger.info(f"Init event: {event}")
    response = {"result": "foo"}
    logger.info(f"Output: {response}")
    return response


if __name__ == "__main__":
    lambda_handler({"foo":"bar"}, None)