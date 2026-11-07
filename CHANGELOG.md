# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-07

### Added
- Sắp xếp giỏ theo tiêu đề và giá bằng sort_by_title(), sort_by_cost().
- Tìm DVD theo danh mục, không phân biệt hoa thường.

## [1.0.0] - 2026-11-07

### Added
- In giỏ hàng bằng Cart.print_cart().
- Tìm DVD theo tiêu đề bằng search_by_title().
- Tính tổng tiền sau giảm giá bằng total_after_discount().
- Unit test cho giới hạn giỏ, tổng tiền và giảm giá.

### Fixed
- Từ chối DVD thứ 21 khi giỏ đã đủ 20 DVD (#7).
- Sửa công thức giảm giá và kiểm tra phần trăm trong khoảng 0–100.
