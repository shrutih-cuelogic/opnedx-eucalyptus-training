from django.db import models


class Reference(models.Model):
    REFERENCE_TYPE_CHOICES = (
        ("Image", ("Image")),
        ("Link", ("Link")),
        ("Video", ("Video")),
        ("Document", ("Document"))
    )

    reference_name = models.CharField(max_length=200)
    reference_type = models.CharField(choices=REFERENCE_TYPE_CHOICES, max_length=20, default="")
    reference_link = models.CharField(max_length=500)
    reference_description = models.CharField(max_length=500)
    reference_status = models.CharField(max_length=20, default="is_alive")
