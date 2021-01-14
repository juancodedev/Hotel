# Generated by Django 3.1.2 on 2021-01-14 16:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCheckIn', models.DateField(default=None)),
                ('TimeCheckIn', models.TimeField(default=None)),
                ('DateCheckOut', models.DateField(default=None)),
                ('TimeCheckOut', models.TimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('CategoryDescription', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(default=None, max_length=50)),
                ('LastName', models.CharField(default=None, max_length=50)),
                ('Rut', models.CharField(default=None, max_length=50)),
                ('Address', models.CharField(default=None, max_length=50)),
                ('Phone', models.CharField(default=None, max_length=50)),
                ('Email', models.CharField(default=None, max_length=50)),
                ('Nationality', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Element', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(default=None, max_length=50)),
                ('Rut', models.CharField(default=None, max_length=50)),
                ('Address', models.CharField(default=None, max_length=50)),
                ('Descriptions', models.CharField(default=None, max_length=50)),
                ('UserId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registration.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('PaymentMethodDescription', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RoomsName', models.CharField(default=None, max_length=50)),
                ('FeaturesId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.features')),
                ('HotelId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='RoomsType',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('RoomsDescription', models.CharField(default=None, max_length=50)),
                ('RoomsId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.rooms')),
            ],
        ),
        migrations.AddField(
            model_name='rooms',
            name='RoomsTypeId',
            field=models.ManyToManyField(to='booking.RoomsType'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('IdBook', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('IdHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registration.userprofile')),
                ('PaymentMethodId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.paymentmethod')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'Payment',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='features',
            name='RoomsId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.rooms'),
        ),
    ]
