from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash

from .forms import productForm
from ..models import Product, User, db, cart
from ..services import findproduct

products = Blueprint('products', __name__, template_folder='products_templates')

# @products.route('/products', methods=['GET', 'POST'])
# def product():
#     form = productForm()
#     my_list = range(1, 20)
#     product_list = []
#     for i in my_list:
#         product = findproduct(i)
#         if product:
#             name = product['Name']
#             price = product['Price']
#             description = product['Description']
#             img_url = product['img_url']
#             category = product['Category']
#             rating = product['Rating']
#             image_1 = product['image_1']
#             item = Product(name, price, description, img_url, category, rating, image_1)
#             item.saveProduct()
#             product_list.append(item)
#     return render_template('product.html', form=form, product_list=product_list)

    # if 'more_info' in request.form:
    #     product = findproduct(request.form['more_info'])
    #     return render_template('single_product.html', form=form, product=product)
    # elif 'add_to_cart' in request.form:        
    #     product = findproduct(request.form['add_to_cart'])
    #     name = product['Name']
    #     price = product['Price']
    #     description = product['Description']
    #     img_url = product['img_url']
    #     category = product['Category']
    #     rating = product['Rating']
    #     user_id = current_user.id
    #     item = Product(name, price, description, img_url, category, rating, user_id)
    #     item.saveProduct()
    #     flash(f'{product["Name"]} added to cart')


@products.route('/products', methods=['GET', 'POST'])
def product():
    form = productForm()
    my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13','14','15','16','17','18','19']
    product_list = []
    for i in my_list:
        product_list.append(Product.query.filter_by(id=i).first())
    if 'more_info' in request.form:
        product = Product.query.filter_by(id=request.form['more_info']).first()
        return render_template('single_product.html', form=form, product=product)
    elif 'add_to_cart' in request.form:        
        product_id = request.form['product_id']
        product = Product.query.filter_by(id=product_id).first()
        # cart.add(product)
        flash(f'{product.name} added to cart')
    return render_template('products.html', form=form, product_list=product_list)