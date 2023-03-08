from django.db import models

# Create your models here.
class AccountBox(models.Model):
    accountName = models.CharField(
        "Hesap Adı", max_length=250, blank=True, null=True, default="empty value"
    )
    accountAmount = models.DecimalField("Toplam Tutar", max_digits=20, decimal_places=2)
    accountImge = models.ImageField(
        "Banka Görseli", null=True, blank=True, upload_to="images/"
    )
    accountStatus = models.BooleanField("Aktif Mi?", null=False, default=True)

    class Meta:
        verbose_name = "Hesap Adı"
        verbose_name_plural = "Hesaplar"

    def __str__(self):
        return f"{self.accountName}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    CustomerTitle = models.CharField(
        "Firma Ünvanı", max_length=255, null=False, blank=False, default="Firma Seçiniz"
    )
    CustomerCode = models.CharField(
        "Cari Kodu", max_length=255, null=False, blank=False
    )
    CustomerPhone = models.CharField("Telefon", max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"

    def __str__(self):
        return f"{self.CustomerTitle}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class AccountAction(models.Model):
    CustomerTitle = models.ForeignKey(
        Customer, verbose_name="Firma Adı", on_delete=models.CASCADE
    )
    accountName = models.ForeignKey(
        AccountBox, verbose_name="Hesap Adı", on_delete=models.CASCADE
    )
    InFlow = "GİRİŞ"
    OutFlow = "ÇIKIŞ"
    IN_OUT_FLOW_CHOICES = [
        (InFlow, "Giriş"),
        (OutFlow, "Çıkış"),
    ]
    in_out_flow = models.CharField(
        "Giriş/Çıkış", max_length=5, choices=IN_OUT_FLOW_CHOICES, default=InFlow
    )
    amount = models.DecimalField("Tutar", max_digits=20, decimal_places=2)
    description = models.TextField("Açıklama", null=True, blank=True)
    created_at = models.DateTimeField("Kayıt Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncelleme Tarihi", auto_now=True)

    class Meta:
        verbose_name = "Hesap Hareketi"
        verbose_name_plural = "Hesap Hareketleri"

    def __str__(self):
        return f"{self.accountName}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        getAccountDetail = AccountBox.objects.filter(accountName=self.accountName)
        if self.in_out_flow == "ÇIKIŞ":
            for i in getAccountDetail:
                AccountBox.objects.filter(accountName=i.accountName).update(
                    accountAmount=(i.accountAmount - self.amount)
                )
        else:
            for i in getAccountDetail:
                AccountBox.objects.filter(accountName=i.accountName).update(
                    accountAmount=(i.accountAmount + self.amount)
                )


"""
    # this block for ManyToManyField List Display And Set Verbos Name
    def get_accounts(self):
        return "\n".join([a.accountName for a in self.accountName.all()])

    get_accounts.short_description = "Hesap Adı"

    def get_customers(self):
        return "\n".join([c.CustomerTitle for c in self.CustomerTitle.all()])

    get_customers.short_description = "Firma Adı"
"""