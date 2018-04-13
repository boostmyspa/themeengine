from django.db import models
import zipfile, json, uuid, os

class SimpleText(models.Model):
        header = models.CharField(max_length=128)
        subheader = models.CharField(max_length=128)
        buttonlink = models.CharField(max_length=128)
        blockname = models.CharField(max_length=128)
        merchanttheme = models.ForeignKey('MerchantTheme')


class Merchant(models.Model):
    name = models.CharField(max_length=128)

class Theme(models.Model):
    theme_name = models.CharField(max_length=128)
    theme_schema = models.FileField(upload_to='schemas')
    theme_zip = models.FileField(upload_to='zips')
    is_active = models.BooleanField(default=True)


class MerchantTheme(models.Model):
    theme = models.ForeignKey(Theme)
    merchant = models.ForeignKey(Merchant)
    created_at = models.DateTimeField(auto_now=True)

    #Todo: Integrate New Theme

    def create_new_theme(self):

        #Create a New Copy of the Theme Files for the Merchant to have Specifically
        if not self.created_at:
            zip_ref = zipfile.ZipFile(self.theme.theme_zip, 'r')
            zip_ref.extractall('/directorytostatic/%s/%s' %(self.merchant.name, self.theme.theme_name))
            zip_ref.close()

        #Load the JSON, Create the Blocks
        data_json = json.load(open(self.theme.theme_schema))
        for block in data_json['blocks']:
            if block['type'] == 'simple-text':
                SimpleText.objects.create(
                    header = block['settings'][0]['header'],
                    subheader = block['settings'][0]['header'],
                    buttonlinkheader = block['settings'][0]['header'],
                    merchanttheme = self
                )