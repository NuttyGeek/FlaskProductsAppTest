
class PayloadValidations():
    
    def validate_product(self, payload):
        '''
        Check if product payload id correct 
        return True/ False
        '''
        try:
            valid =  len(payload['title']) > 0 and payload['price'] > 0
            return valid
        except:
            return False
    