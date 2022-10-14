from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='YOUR_API_KEY')

# Generate Blog articles using Hemingwai
blog = hemingwai.generate_blog(blog_title='Why SEO is important for your Business?',
                               blog_keywords='SEO, Business',
                               source_language='en', token_count=20, temperature=0.7, n_gen=2)
print(blog)

# Generate Blog Titles using Hemingwai
blog_titles = hemingwai.generate_blog_title(blog_keywords='startups, raising vc funding, being influential', blog_intro='Raising VC capital became the hot topic in the industry, but does it really make sense for startups?')
print(blog_titles)

# Generate Product Descriptions using Hemingwai
product_description = hemingwai.generate_product_descriptions(
    product_name='Black Backpack Bag', product_category='Shoes & Bags, Women', brand='Cortexian',
    product_features='Color: Black, Material: Faux Leather',
    source_language='en', token_count=400, temperature=0.65, n_gen=3)
print(product_description)

# Autocomplete the rest using Hemingwai
autocomplete = hemingwai.generate(prompt='He also teaches architectural and urban design studios in several '
                                         'universities as an adjunct professor.',
                                  source_language='en', token_count=50, temperature=0.7, n_gen=2)
print(autocomplete)

paraphrase = hemingwai.paraphrase(prompt='He also teaches architectural and urban design studios in several'
                                         ' universities as an adjunct professor.',
                                  source_language='en', token_count=200, temperature=1, n_gen=2)
print(paraphrase)


