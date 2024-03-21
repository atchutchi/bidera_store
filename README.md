# Bidera Store

## Overview
Welcome to Bidera Store, your one-stop online shop for fresh and high-quality food products ranging from vegetables, beef, pork, goat meat, seafood, rice, fish, and much more. Our platform is designed to provide a seamless and convenient shopping experience, allowing customers to purchase products by quantity and enjoy home delivery services.

[Here is the live version of the project](https://bidera-store-4f0dc6400eda.herokuapp.com/)

![Bidera Store Responsive Mockup](./static/assets/img/readme/bidera_store_mockup.png)

## Strategy

**Project Objectives**
Bidera Store aims to revolutionize the way people shop for food online by offering a wide selection of fresh products, customizable quantities, and efficient home delivery. Our goal is to ensure that every household has access to quality food products without the hassle of visiting physical stores.

## User Stories

### Newsletter Subscription
As a **shopper** I can **subscribe to the newsletter** so that **I receive updates on new products, promotions, and other news related to the store.**

### Acceptance Criteria
- Acceptance criteria 1: The subscription form should be easily accessible and visible on the homepage and other strategic locations across the website to encourage subscriptions.
- Acceptance criteria 2: The user must be able to subscribe by simply entering their email address and clicking the subscribe button, without the need for creating an account or providing additional unnecessary information.
- Acceptance criteria 3: Upon successful subscription, the user should receive immediate visual confirmation on the website and a welcome email confirming their subscription and outlining what type of content they can expect to receive.


### Registration and User Accounts
- As a **Site User** I can **EasilySign up with google authentication** so that i can **Avoid introducing a password and information details on regsitration**

- As a **Site User** I can **Easily register for an account** so that **Have a personal account and be abble to view my profile**

- As a **Site User** I can **Easily login or logout** so that i can **Access my personal account information**

- As a **Site User** I can **Easily recover my password in case i forgot it** so that i can **Recover access to my account**

- As a **Site User** I can **Receive an email confirmation after registering** so that i can **Access my personal account information**

- As a **Site User** I can **have a personalized user profile** so that i can **View my personal order history and order confirmations, and save my payment information**


### Contact Story
As a **User** I can **easily contact the store team through a form on the contact page** so that **I can ask questions, request information about products, seek support, or express my concerns quickly and directly**

### Acceptance Criteria
- Acceptance criteria 1: Easy access to the contact form: Users should easily find the contact option on the website, ideally from the main menu or footer on all pages.

- Acceptance criteria 2: Intuitive contact form: The form should be clear and simple, asking for essential information like name, email, subject, and the message.

- Acceptance criteria 3: Form validation: Before submission, the system should validate the information input by the user, such as the correct formatting of the email.

- Acceptance criteria 4: Feedback after submission: After submitting, the user should receive feedback, either on the same page or via email, confirming that the message has been received.


### Viewing and Navigation
- As a **shopper** I can **easy view a list of products** so that i can **select some purchase**

- As a **Shopper** I can **view individual product details** so that i can **Identify the price, description, product rating, product image**

- As a **shopper** I can **Quickly identify deals, clearance items and special offers** so that i can  **take advantage of special savings on the products i'd like to purchase**

- As a **shopper** I can **Easily view the total of my purchases at any time** so that i can **avoid spending too much**


### Wishlist Feature
As a **user** I can **add and remove products from my wishlist ** so that ** I can easily keep track of items I am interested in purchasing later.**

### Acceptance Criteria

- Acceptance criteria 1: As a registered user, when I navigate to a product detail page, I should see a heart icon indicating whether the product is already in my wishlist or not. If the product is not in the wishlist, clicking the heart icon should add the product to my wishlist, and the icon should change to reflect that it's been added.

- Acceptance criteria 2: The wishlist feature should be accessible only to logged-in users. Users who are not logged in should be prompted to log in when trying to add a product to the wishlist or when attempting to access the wishlist page.

- Acceptance criteria 3: As a registered user, I should be able to view my wishlist from a dedicated wishlist page.


### Admin and Store Management
- As a **Store Owner** I can **Add product** so that I can **Add new Items to my store**

- As a **Store Owner** I can **Edit/update a product** so that I can **Change product prices, descriptions, images, and other product criteria**

- As a **Store Owner** I can **Delete a product** so that I can **Remove items that are no longer for sale**


### Purchasing and Checkout
- As a **Shopper** I can **Easily select the quantity of a product when purchasing it** so that I can **Ensure i dont accidentally select the wrong product quantity**

- As a **Shopper** I can **View Items in my bag to be purchased** so that I can **Identify the total cost of my purchase and all items I will receive**

- As a **Shopper** I can **Adjust the quantity of my individual items in my bag** so that I can **Easily make changes to my purchase before checkout**

- As a **Shopper** I can **Enter my payment information** so that I can **Checkout quickly and with no hassles**

- As a **Shopper** I can **Feel my personal and payment is safe and secure** so that I can **Confidently provide the needed information to make a purchase**

- As a **Shopper** I can **View and order confirmation after checkout** so that I can **verify that I haven't made any mistakes**

- As a **Shopper** I can **Receive an email confirmation after checking out** so that I can **keep the confirmation of what I've purchased for my records**


### Sorting and Seaching

- As a **Shopper** I can **Sort the list of available products** so that i can **Easily identify the best rated, Best priced and categorically sorted products**

- As a **Shopper** I can **Sort a specific category of product** so that i can **Find the best-priced or best-rated product in a specific category, or sort the products in that category by name**

- As a **Shopper** I can **Sort multiple categories of products simultaneously** so that i can **find the best-priced or best rated products across broad categories, such as "fruits" or "meat"**

- As a **Shopper** I can **Search a product by name or description** so that i can **Find a specific product i'd like to purchase**

- As a **Shopper** I can **Easily see what I've  searched for and the number of results** so that i can **Quickly decide whether the product I want is available**



## Skeleton 

### Database Schema

The database schema of Bidera Store is designed to efficiently manage products, orders, and deliveries. The schema includes tables for `Products`, `Orders`, `OrderItems`, `Users`, and `DeliveryInformation`.

![Database Schema Diagram](./static/assets/img/readme/database_schema.png)

### Models

Our application utilizes Django models to represent and interact with the database. Below are key models used in Bidera Store:

- **Product Model**: Stores information about the food products available for purchase.
- **Order Model**: Manages customer orders and associates them with users.
- **DeliveryInformation Model**: Contains delivery details for each order.

## Surface

### Wireframes

Wireframes were created to plan the layout of key pages within Bidera Store, focusing on usability and a seamless shopping experience.

[View Wireframes](#)

## Features and Testing

### Feature: Product Browsing and Selection
![Product Page](./static/assets/img/readme/product_page.png)
**Testing**: This feature was tested across multiple devices and browsers to ensure products are displayed correctly and can be added to the shopping cart.

### Feature: Secure Checkout Process
![Checkout Page](./static/assets/img/readme/checkout_page.png)
**Testing**: The checkout process was rigorously tested to ensure security and accuracy in order processing.

## Testing and Troubleshooting

### Resolving NoReverseMatch Error for 'wishlist'

**Problem Description:**  
The application threw a NoReverseMatch error stating "Reverse for 'wishlist' not found. 'wishlist' is not a valid view function or pattern name." This error indicates that Django's URL dispatcher is unable to find a URL pattern named 'wishlist', critical for rendering the wishlist page or functionality within the application.

**Solution:**  
- **URL Name Does Not Exist:** Ensure a URL pattern named 'wishlist' is defined in one of the urls.py files within the application. If missing, add a corresponding path entry to define this URL pattern.
- **Namespace Issue:** If using application namespaces (e.g., `app_name = 'wishlist'` in the application's urls.py), ensure to include the namespace when referencing the URL in templates or reverse function calls. Correctly prefix the URL name with the namespace, changing `{% url 'wishlist' %}` to `{% url 'wishlist:view_wishlist' %}` in templates, and similar adjustments in reverse function calls.

### Resolving TemplateSyntaxError for Custom Tag Library

**Problem:**  
When attempting to access the product detail page, Django throws a TemplateSyntaxError, indicating that the custom tag library 'wishlist_tags' is not registered. The error suggests Django is unable to locate the custom tag library defined in the templatetags directory of the wishlist app.

**Solution:**  
The root cause was the absence of an `__init__.py` file within the templatetags directory of the wishlist app. Django requires each Python directory to contain an `__init__.py` file to be recognized as a package. The presence of this file allows Django and Python to recognize the templatetags directory as a valid module, making the custom template tags available for use in templates.

### Resolving the NoReverseMatch Error for Wishlist URLs

**Problem:**  
The application threw a NoReverseMatch error when attempting to access the product detail page, indicating that the `wishlist_add` and `wishlist_remove` URLs could not be found, suggesting an issue with how URLs were referenced in the template.

**Solution:**  
The error was due to incorrect usage of URL namespacing in the template. The application uses URL namespacing for the wishlist app (`app_name = 'wishlist'` in wishlist/urls.py), requiring specifying both the namespace and the URL name when using the `{% url %}` template tag. The problem was resolved by correctly prefixing the URL names with the `wishlist:` namespace in the product_detail.html template.


<!-- Correct URL references with namespacing -->
{% if product|in_user_wishlist:user %}
    <a href="{% url 'wishlist:remove_from_wishlist' product.id %}" class="btn btn-danger">Remove from Wishlist</a>
{% else %}
    <a href="{% url 'wishlist:add_to_wishlist' product.id %}" class="btn btn-success">Add to Wishlist</a>
{% endif %}


## Future Development

- Implement a loyalty program for frequent shoppers.
- Expand product range to include organic and dietary-specific items.

## Validator Testing
#### **HTML Validation**
I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/) using the textarea input.

| Feature  | Expected Outcome | Result |
| ------------- | ------------- | ------------- |


### **CSS Validation**
- In my project, I conducted a CSS validation test using the Jigsaw W3 CSS Validator for CSS Level 3 + SVG. The test identified several errors, as displayed in the image below. However, I chose not to correct these errors as the CSS in question is part of a pre-made template from Start Bootstrap - Agency v7.0.12 (https://startbootstrap.com/theme/agency). For reference, the details of these validation errors can be seen in the image provided.
![Jigsaw](./static/)

### **Python Linting**
All code passed the validation tests through the [PEP8CI](https://pep8ci.herokuapp.com/). 
| Feature  | Expected Outcome | Result |
| ------------- | ------------- | ------------- |
| bidera_store/views.py  | Page passes validation with no errors | All clear, no errors found  |
| bidera_store/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| bidera_store/settings.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/views.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/models.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| bag/context.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/views.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/models.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/signals.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/webhook_handler.py  | Page passes validation with no errors | All clear, no errors found  |
| checkout/webhook.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/views.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/models.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| contact/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| home/views.py  | Page passes validation with no errors | All clear, no errors found  |
| home/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| home/models.py  | Page passes validation with no errors | All clear, no errors found  |
| home/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| home/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| home/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| products/views.py  | Page passes validation with no errors | All clear, no errors found  |
| products/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| products/models.py  | Page passes validation with no errors | All clear, no errors found  |
| products/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| products/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| products/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| products/widgets.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/views.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/models.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| profiles/tests.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/views.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/urls.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/models.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/forms.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/apps.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/admin.py  | Page passes validation with no errors | All clear, no errors found  |
| wishlist/tests.py  | Page passes validation with no errors | All clear, no errors found  |

### **JavaScript Linting**
- The code was tested on [jshint](https://jshint.com/) Without errors.

![jshint](./static/)


## Deployment

Bidera Store is deployed on Heroku. Follow these steps for deployment:
1. Set up a Heroku account and create a new app.
2. Connect your GitHub repository to Heroku.
3. Set environment variables in Heroku.
4. Deploy the application.

For detailed deployment instructions, refer to the [Heroku Documentation](https://devcenter.heroku.com/articles/git).

## Credits

### Code
- During the development of the Bidera Store project, I extensively utilized the tools and resources (Template and resources) provided by the [Code Institute Boutique Ado Project](https://codeinstitute.net/).

### Language Used
- TECHNOLOGIES: 
    - HTML5: To build the main structure of the site
    - CSS3:  To style the website with bootstrap
    - JAVASCRIPT: For the frontend interactivity

### Deployment
- Use Code Institute [Django Deployment Instructions](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit#heading=h.5s9novsydyp1)
- Heroku
- Amazon AWS

### Content and Media
- Product images and descriptions were sourced from various free image repositories and manufacturers' websites.

### Acknowledgements
- Thanks to my mentor [Can Sücüllü](https://github.com/cansucullu) were consulted during the development process.
- Special thanks to the Django and Bootstrap documentation for providing valuable resources.

