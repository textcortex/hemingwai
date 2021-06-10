from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='YOUR_API_KEY')

# Generate Blog articles using Hemingwai
blog = hemingwai.generate_blog(blog_title='Why SEO is important for your Business?', target_segment='Young Men',
                               source_language='en', character_count=400, creativity=0.7)
print(blog)

# Autocomplete the rest using Hemingwai
autocomplete = hemingwai.generate(prompt='Was ist los mit dir?', target_segment='',
                                  source_language='de', character_count=200, creativity=0.7)
print(autocomplete)

# Generate Ad copies using Hemingwai
ads = hemingwai.generate_ads(prompt='Pink Geometric Bag', target_segment='Young Women',
                             source_language='en', character_count=200, creativity=0.7)
print(ads)

# Generate Email Body using Hemingwai
email_body = hemingwai.generate_email_body(email_subject='Summer Sale on Selected Sunglasses!', target_segment='',
                                           source_language='en', character_count=200, creativity=0.7)
print(email_body)

# Generate Email Subject using Hemingwai
email_subject = hemingwai.generate_email_subject(keywords='Sunglasses, summer, sale', target_segment='Young people',
                                                 source_language='en', character_count=100, creativity=0.7)
print(email_subject)

# Generate Product Descriptions using Hemingwai
product_description = hemingwai.generate_product_descriptions(
                    product_title='Black Backpack', product_category='Shoes & Bags', target_segment='',
                    source_language='en', character_count=300, creativity=0.7)
print(product_description)

