def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa từ khóa; Lab 02 phân biệt hoa thường."""
    return [dvd for dvd in items if keyword in dvd.title]
