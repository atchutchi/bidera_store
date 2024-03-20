# Bidera Store

## Overview
Welcome to Bidera Store, your one-stop online shop for fresh and high-quality food products ranging from vegetables, beef, pork, goat meat, seafood, rice, fish, and much more. Our platform is designed to provide a seamless and convenient shopping experience, allowing customers to purchase products by quantity and enjoy home delivery services.

[Here is the live version of the project](#)

![Bidera Store Responsive Mockup](./static/assets/img/readme/bidera_store_mockup.png)

## Strategy

**Project Objectives**
Bidera Store aims to revolutionize the way people shop for food online by offering a wide selection of fresh products, customizable quantities, and efficient home delivery. Our goal is to ensure that every household has access to quality food products without the hassle of visiting physical stores.

## User Stories
### USER STORY: Online Shopping
As a **customer**, I can **browse through various food products** so that **I can select and purchase them online.**

#### Acceptance Criteria

- The platform must display a wide range of food products with detailed descriptions and prices.
- Customers should be able to select the quantity of products they wish to purchase.
- The shopping cart system must accurately reflect the items added by the customer.

#### Tasks

- [x] Implement a product listing page with categories and filters.
- [x] Develop a dynamic shopping cart system.
- [x] Create a secure checkout process.

### USER STORY: Home Delivery
As a **customer**, I can **choose home delivery for my orders** so that **I receive my purchases without leaving my home.**

#### Acceptance Criteria

- The platform must offer an option to choose home delivery during the checkout process.
- Customers should be provided with estimated delivery times and tracking information.
- The delivery service must cover a wide geographical area to accommodate various customers.

#### Tasks

- [x] Integrate a home delivery option in the checkout process.
- [x] Partner with reliable delivery services.
- [x] Implement a system to provide customers with delivery updates.

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