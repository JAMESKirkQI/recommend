
from pathlib import Path
import time
from datetime import datetime

from django.core import serializers
from django.test import TestCase

# Create your tests here.
from recommend.models import *

if __name__ == '__main__':
    # print(Path(__file__).resolve().parent.parent)

    s = datetime.strptime("2015-02-02 15:46:18", "%Y-%m-%d %H:%M:%S")
    print(s.hour)

