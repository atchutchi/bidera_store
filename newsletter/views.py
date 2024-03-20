from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Send the discount code to the email or display it on the screen.
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'any_template.html', {'form': form})
