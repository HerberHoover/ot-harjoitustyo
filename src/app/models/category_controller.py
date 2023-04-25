from database.categories import add_category as db_add_category

class CategoryController:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_category(self, category_name):
        db_add_category(self.user_id, category_name)
