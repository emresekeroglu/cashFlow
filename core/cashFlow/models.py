from django.db import models

# Create your models here.
class AccountBox(models.Model):
    accountName = models.CharField("Hesap Adı", max_length=250, blank=True, null=True)
    accountAmount = models.DecimalField("Toplam Tutar", max_digits=10, decimal_places=2)
    accountImge = models.ImageField("Banka Görseli", null=True, blank=True, upload_to="images/")
    accountStatus = models.BooleanField("Aktif Mi?", null=False, default=True)

    class Meta:
        verbose_name = "Hesap Adı"
        verbose_name_plural = "Hesaplar"

    def __str__(self):
        return f"{self.accountName}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
