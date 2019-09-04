# Generated by Django 2.2.4 on 2019-09-03 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("posts", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ["-created"]}),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
        migrations.AlterField(
            model_name="post", name="content", field=models.TextField(verbose_name="내용")
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, verbose_name="제목"),
        ),
    ]
