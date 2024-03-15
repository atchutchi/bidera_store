from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# The contact view for handling the contact form submission
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Optionally save form to the database
            form.save()
            
            # Send an email
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                settings.DEFAULT_FROM_EMAIL,
                ['biderastore@gmail.com'],
            )
            
            # Add a success message for on-page confirmation
            messages.success(request, 'Your message has been sent successfully. We will get back to you shortly.')
            
            # Redirect back to the contact page, which will show the success message
            return redirect('contact')
    else:
        form = ContactForm()

    # Render the contact page with the ContactForm instance
    return render(request, 'contact/contact.html', {'form': form})
