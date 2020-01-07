from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    if not request.session['reviewed_products']:
        request.session['reviewed_products'] = []
    request.session['is_review_exists'] = False

    if request.method == 'POST':
        review_text = request.POST.get('text')
        new_review = Review.objects.create(text=review_text, product=product)
        request.session['reviewed_products'].append(product.id)

    reviews = Review.objects.filter(product=product)
    if product.id in request.session['reviewed_products']:
        request.session['is_review_exists'] = True

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exists': request.session['is_review_exists']
    }

    return render(request, template, context)
