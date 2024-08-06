class Livro:
    
    def __init__(self, titulo, review, preco, url_img):
        self.titulo = titulo
        self.review = review
        self.preco = preco
        self.url_img = url_img
    
    def get_titulo(self):
        return self.titulo

    def get_review(self):
        return self.review
    
    def get_preco(self):
        return self.preco
    
    def get_url_img(self):
        return self.url_img
    
    
    
   
