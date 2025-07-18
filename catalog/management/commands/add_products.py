from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'add products to the database'

    def handle(self, *args, **options):
        # Очищаем БД
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Накатываем фикстуру
        call_command('loaddata', 'catalog_fixture.json')

        cat, _ = Category.objects.get_or_create(name='Устаревшая техника')
        products = [
            {'name': 'Nokia 1221', 'price': 1000, 'category': cat},
            {'name': 'TV Samsung 733', 'price': 3000, 'category': cat},
                    ]

        for product_data in products:
            prod, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {prod.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {prod.name}'))
