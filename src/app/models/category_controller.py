from database.categories import add_category, get_categories

class CategoryController:
    """
    A class to handle category-related operations for a specific user.

    Attributes:
        user_id (int): The user ID for which the categories are managed.
    """
    def __init__(self, user_id):
        """
        Initializes a new CategoryController instance.

        Args:
            user_id (int): The user ID for which the categories are managed.
        """
        self.user_id = user_id

    def add_category(self, category_name):
        """
        Adds a new category for the user.

        Args:
            category_name (str): The name of the category to be added.
        """
        add_category(self.user_id, category_name)

    def get_categories(self):
        """
        Retrieves all categories for the user.

        Returns:
            list: A list of tuples containing category information.
        """
        return get_categories(self.user_id)
