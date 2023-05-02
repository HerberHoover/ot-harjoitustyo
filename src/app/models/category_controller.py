from database.categories import add_category, get_categories

class CategoryController:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_category(self, category_name):
        add_category(self.user_id, category_name)

    def get_categories(self):
        return get_categories(self.user_id)
