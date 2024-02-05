import json 

class Database():
    
    def get_products(self):
        '''
            return the list of products
        '''
        try:
            with open('./data/products.json', 'r') as data:
                print('d', data)
                products = json.load(data)
                print(':: products', products)
                return products
        except Exception as e:
            print('error', e)
            return []
    
    def add_product(self, product):
        '''
        Creates a Products
        '''
        try:
            # Step 1: Read the existing products
            with open('./data/products.json', 'r') as file:
                products = json.load(file)
            print(':: print products', products)
            # Step 2: Process and update the products list
            ids = [x['id'] for x in products]
            max_id = max(ids, default=0)  # Use default=0 to handle empty list
            products.append({
                'id': max_id + 1,
                'title': product['title'],
                'price': product['price']
            })
            # Step 3: Write the updated products back to the file
            with open('./data/products.json', 'w') as file:
                json.dump(products, file)
            return products
        except Exception as e:
            print('error', e)
            return []
        
        