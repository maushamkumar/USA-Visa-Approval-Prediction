from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
from us_visa.utils.main_utils import read_yaml
# logging.info("Hello World")


# try:
#     a = 1/0
# except Exception as e:
#     raise e


a = read_yaml("configs/model.yaml")
print(a)