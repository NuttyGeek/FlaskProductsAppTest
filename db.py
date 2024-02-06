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
        
    def get_product_by_id(self, product_id):
        ''' get product by id'''
        with open('./data/products.json' , 'r') as file:
            products = json.load(file)
            print(':: products', products)
            found = {}
            for p in products:
                print(':: p', p, product_id)
                if p['id'] == product_id:
                    found = p
                    print(':: found', found)
            return found
            # res = [ p for p in products if p['id'] == product_id ]
            # res[0] if len(res) > 0 else {}
        
    def update_product(self, p_id, product):
        ''' update Product '''
        with open('./data/products.json', 'r') as file:
            products = json.load(file)
            p_map = {}
            print(':: products', products)
            for p in products:
                p_map[p['id']] = p
            print(':: p_map', p_map)
            p_map[p_id] = {
                'id': p_id,
                'title': product['title'],
                'price': product['price']
            }
            updated_products = list(p_map.values())
            print(':: updated', updated_products)
            with open('./data/products.json', 'w') as file:
                json.dump(updated_products, file)
        return { 'message': 'Product update successfully '}
    
    def delete_product(self, p_id):
        ''' Delete Product '''
        with open('./data/products.json', 'r') as file:
            products = json.load(file)
            updated_products = [p for p in products if p['id'] != p_id]
            with open('./data/products.json', 'w') as file:
                json.dump(updated_products, file)