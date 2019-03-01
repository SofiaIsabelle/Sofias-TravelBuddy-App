from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import date, datetime
from time import strptime
Name_Regex = re.compile(r'^[A-Za-z ]+$')

# Create your models here.
