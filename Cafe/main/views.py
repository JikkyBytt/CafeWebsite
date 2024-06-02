from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, MenuItem
from .models import Order
from django.http import JsonResponse

def name(response, item):
    # Get the menu item object
    menu_item = MenuItem.objects.get(item=item)
    
    # Extract item name and description
    item_name = menu_item.item
    item_description=menu_item.description
    item_price=menu_item.price
        
    # Return the HTML response
    return render(response,"main/index.html",{"item_name":item_name,"item_description":item_description,"item_price":item_price})

def home(response):
    return render(response,"main/home.html",{})
    
def menu(response):
    # Get all menu items from the database
    menu_items = MenuItem.objects.all()
    
    # Pass the menu items to the template
    return render(response, "main/menu.html", {"menu_items": menu_items})

def about_us(response):
    return render(response, "main/aboutus.html", {})

def contact_us(response):
    return render(response, "main/contactus.html", {})

def place_order(request):
    if request.method == 'POST':
        # Process the order form data
        total_price = 0
        
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.split('_')[1]
                quantity = int(value)
                
                # Retrieve the menu item from the database
                try:
                    menu_item = MenuItem.objects.get(pk=item_id)
                except MenuItem.DoesNotExist:
                    return JsonResponse({'error': 'Invalid menu item ID'}, status=400)
                
                # Calculate the subtotal price for the item and update the total price
                total_price += menu_item.price * quantity
        
        # You can further process the order here, such as saving it to the database
        
        # Return a JSON response with the total price
        if total_price <=0:
            return JsonResponse({'error': 'Price is 0'}, status=405)
        else:
            order_items = f"Item ID: {item_id}, Quantity: {quantity}"
            order = Order(
                order_items=order_items,
                total_price=total_price,
                user=request.user  # Assuming you have authentication set up
            )
            order.save()
            return JsonResponse({'total_price': total_price})
        
    else:
        # If the request method is not POST, return an error response
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})