from .forms import NewsletterSignupForm

def newsletter_signup(request):
    form = NewsletterSignupForm()
    return {'newsletter_signup_form': form}
