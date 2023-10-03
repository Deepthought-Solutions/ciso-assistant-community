# Generated by Django 4.2 on 2023-07-04 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('version', models.CharField(blank=True, default='1.0', help_text='Version of the assessment (eg. 1.0, 2.0, etc.)', max_length=100, null=True, verbose_name='Version')),
                ('is_draft', models.BooleanField(default=True, verbose_name='draft')),
                ('is_obsolete', models.BooleanField(default=False, verbose_name='obsolete')),
            ],
            options={
                'verbose_name': 'Assessment',
                'verbose_name_plural': 'Assessments',
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('attachment', models.FileField(blank=True, help_text='File for evidence (eg. screenshot, log file, etc.)', null=True, upload_to='evidence/', verbose_name='File')),
                ('ref_url', models.CharField(blank=True, help_text='External url for evidence (eg. Jira ticket)', max_length=1000, null=True, verbose_name='Link')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Evidence',
                'verbose_name_plural': 'Evidence',
            },
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
                ('version', models.CharField(blank=True, default='1.0', help_text='Version of the framework (eg. 1.0, 2.0, etc.)', max_length=100, null=True, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'Framework',
                'verbose_name_plural': 'Frameworks',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
                ('parent_urn', models.CharField(blank=True, max_length=100, null=True, verbose_name='Parent URN')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Order ID')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Level')),
                ('informative_reference', models.CharField(blank=True, max_length=256, null=True, verbose_name='Informative reference')),
            ],
            options={
                'verbose_name': 'Requirement',
                'verbose_name_plural': 'Requirements',
            },
        ),
        migrations.CreateModel(
            name='RequirementAssessment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('status', models.CharField(choices=[('IP', 'In progress'), ('C', 'Compliant'), ('NC', 'Non compliant'), ('PC', 'Partially compliant'), ('NA', 'Not applicable')], default='IP', max_length=100, verbose_name='Status')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Requirement assessment',
                'verbose_name_plural': 'Requirement assessments',
            },
        ),
        migrations.CreateModel(
            name='RequirementGroup',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
                ('parent_urn', models.CharField(blank=True, max_length=100, null=True, verbose_name='Parent URN')),
                ('order_id', models.IntegerField(blank=True, null=True, verbose_name='Order ID')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Level')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequirementLevel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
                ('level', models.IntegerField(verbose_name='Level')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecurityFunction',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
                ('provider', models.CharField(blank=True, max_length=200, null=True, verbose_name='Provider')),
                ('typical_evidence', models.JSONField(blank=True, null=True, verbose_name='Typical evidence')),
            ],
            options={
                'verbose_name': 'Security function',
                'verbose_name_plural': 'Security functions',
            },
        ),
        migrations.CreateModel(
            name='SecurityMeasure',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('type', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In progress'), ('on_hold', 'On hold'), ('done', 'Done')], default='open', max_length=20, verbose_name='Status')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Cost')),
                ('eta', models.DateField(blank=True, help_text='Estimated Time of Arrival', null=True, verbose_name='ETA')),
            ],
            options={
                'verbose_name': 'Security measure',
                'verbose_name_plural': 'Security measures',
            },
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('locale_data', models.JSONField(blank=True, null=True, verbose_name='Locale data')),
                ('urn', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='URN')),
            ],
            options={
                'verbose_name': 'Threat',
                'verbose_name_plural': 'Threats',
            },
        ),
    ]