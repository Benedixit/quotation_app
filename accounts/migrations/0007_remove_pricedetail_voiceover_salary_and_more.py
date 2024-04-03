# Generated by Django 5.0.3 on 2024-03-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_pricedetail_animation_artists_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricedetail',
            name='voiceover_salary',
        ),
        migrations.AddField(
            model_name='pricedetail',
            name='final_cost',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricedetail',
            name='prod_mgt',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricedetail',
            name='total_sum',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricedetail',
            name='vat_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricedetail',
            name='voiceover_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='animation_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='audio_studio_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='compositing_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='editing_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='fx_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='illustration_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='invoice_id',
            field=models.CharField(default='500', max_length=50),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='layout_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='lighting_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='lookdev_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='modelling_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='moodboard_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='motion_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='music_sync_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='rendering_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='rigging_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='storyboard_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricedetail',
            name='texturing_price',
            field=models.CharField(blank=True, default='FREE', max_length=100, null=True),
        ),
    ]
