from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

#logging.info("Welcome to NgocSon project!!!")

try:
    a = 2 / '6'
except Exception as e:
    raise SignException(e, sys) from e