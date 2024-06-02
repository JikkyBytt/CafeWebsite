# Step 1: Open the Python shell

# Step 2: Import the necessary models
from myapp.models import Menu, MenuItem  # Import your models

# Step 3: Retrieve the menu instance from the Menu model
menu = Menu.objects.get(name="Your Menu Name")  # Replace "Your Menu Name" with the actual name of your menu

# Step 4: Create and save menu items
# Drinks
espresso = MenuItem(menu=m, item="Espresso", description="A concentrated coffee beverage made by forcing hot water through finely-ground coffee beans. Served in a small cup.", price=2.50)
espresso.save()

cappuccino = MenuItem(menu=m, item="Cappuccino", description="Equal parts espresso, steamed milk, and milk foam, creating a creamy and balanced coffee drink.", price=3.50)
cappuccino.save()

latte = MenuItem(menu=m, item="Latte", description="Espresso mixed with steamed milk, topped with a small amount of milk foam. Creamy and slightly sweet.", price=4.00)
latte.save()

mocha = MenuItem(menu=m, item="Mocha", description="A latte with chocolate syrup mixed in, giving it a rich and indulgent flavor.", price=4.50)
mocha.save()

hot_chocolate = MenuItem(menu=m, item="Hot Chocolate", description="A comforting and indulgent drink made with rich chocolate syrup and steamed milk, topped with whipped cream (optional).", price=4.00)
hot_chocolate.save()

# Pastries & Other Food
croissant = MenuItem(menu=m, item="Croissant", description="A flaky, buttery pastry originating from France, perfect for breakfast or a snack.", price=3.00)
croissant.save()

muffin = MenuItem(menu=m, item="Muffin", description="A soft and moist baked good with various flavors such as blueberry, chocolate chip, or banana nut.", price=2.50)
muffin.save()

scone = MenuItem(menu=m, item="Scone", description="A crumbly pastry often flavored with fruits like cranberry or blueberry, ideal for pairing with coffee or tea.", price=3.50)
scone.save()

bagel_cream_cheese = MenuItem(menu=m, item="Bagel with Cream Cheese", description="A toasted bagel served with a generous spread of cream cheese, available in flavors like plain, sesame, or everything.", price=4.00)
bagel_cream_cheese.save()

cinnamon_roll = MenuItem(menu=m, item="Cinnamon Roll", description="A sweet and indulgent pastry made from rolled dough, cinnamon, sugar, and topped with icing.", price=4.50)
cinnamon_roll.save()

fruit_danish = MenuItem(menu=m, item="Fruit Danish", description="A light and flaky pastry filled with fruit preserves or fresh fruit, often topped with a glaze or icing.", price=3.50)
fruit_danish.save()

yogurt_parfait = MenuItem(menu=m, item="Yogurt Parfait", description="Layers of yogurt, granola, and fresh fruit, served in a glass or cup, offering a refreshing and wholesome snack.", price=5.00)
yogurt_parfait.save()
