def search_by_category(items, category):
    """Lọc DVD theo danh mục chính xác, không phân biệt hoa thường."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa từ khóa, không phân biệt hoa thường."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
