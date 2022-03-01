from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='gAAAAABhfEQ7Gl5N3slm_YuQy_Xfh7SKyd_qR09QPnDUULi_mgIeTTbnQ0_1xTepGXoULTisGnQMqcUM7O8VSH51mC2GlHrWAihX8xiHFojutjIWZdmcLhgE6bL6CxQIaZlPKMu644dC')

# Generate Blog articles using Hemingwai
blog = hemingwai.generate_blog(blog_title='Why SEO is important for your Business?', blog_categories=['SEO', 'Business'],
                               source_language='en', character_count=400, creativity=0.7, n_gen=2)
print(blog)

# Generate Product Descriptions using Hemingwai
product_description = hemingwai.generate_product_descriptions(
                    product_title='Black Backpack Bag', product_category=['Shoes & Bags', 'Women'], product_brand='Cortexian',
                    product_features=['Color: Black', 'Material: Faux Leather'],
                    source_language='en', character_count=400, creativity=0.6, n_gen=3)
print(product_description)


# Autocomplete the rest using Hemingwai
autocomplete = hemingwai.generate(prompt='Was ist los mit dir?', parameters='',
                                  source_language='de', character_count=200, creativity=0.7, n_gen=2)
print(autocomplete)

# Generate Ad copies using Hemingwai
ads = hemingwai.generate_ads(prompt='Pink Geometric Bag', parameters='Young Women',
                             source_language='en', character_count=200, creativity=0.7, n_gen=2)
print(ads)

# Generate Email Body using Hemingwai
email_body = hemingwai.generate_email_body(email_subject='Summer Sale on Selected Sunglasses!', parameters='',
                                           source_language='en', character_count=200, creativity=0.7, n_gen=2)
print(email_body)

# Generate Email Subject using Hemingwai
email_subject = hemingwai.generate_email_subject(keywords='Sunglasses, summer, sale', parameters='Young people',
                                                 source_language='en', character_count=100, creativity=0.7)
print(email_subject)


instagram_caption = hemingwai.generate_instagram_caption(product='Rayban Black Finish Sunglasses',
                                                         audience='University students',
                                                         source_language='en', character_count=300,
                                                         creativity=0.8, n_gen=3)
print(instagram_caption)
