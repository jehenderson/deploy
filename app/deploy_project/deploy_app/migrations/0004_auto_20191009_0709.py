# Generated by Django 2.2.4 on 2019-10-09 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_app', '0003_auto_20191008_2346'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CredentialRequirements',
            new_name='CredentialRequirement',
        ),
        migrations.RenameModel(
            old_name='Doctype',
            new_name='CredentialType',
        ),
        migrations.RenameModel(
            old_name='ComponentDocuments',
            new_name='Document',
        ),
        migrations.RenameField(
            model_name='credentialrequirement',
            old_name='componentDocuments',
            new_name='component_documents',
        ),
    ]
