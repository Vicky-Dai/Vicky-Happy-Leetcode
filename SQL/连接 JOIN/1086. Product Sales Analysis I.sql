SELECT Product.product_name, Sales.year, Sales.price
From Product
Join Sales ON Product.product_id = Sales.product_id