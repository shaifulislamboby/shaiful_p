# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timezone

from django.db import models


class EmailRecord(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.TextField()
    message = models.CharField(max_length=100)
    send_date = models.DateTimeField(default=datetime.now(timezone.utc))

    def __str__(self):
        return self.email
