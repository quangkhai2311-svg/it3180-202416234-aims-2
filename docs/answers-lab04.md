# Trả lời Lab 04

## Vì sao chuẩn bị bản phát hành trên master trước?

Phiên bản, changelog và mã nguồn cần được review và kiểm thử cùng nhau qua PR vào master trước khi tạo baseline. Nhánh release được tạo từ commit đã kiểm tra, nên thông tin phiên bản và nội dung phát hành khớp nhau.

## Vì sao release không merge ngược vào master trong quy trình bài này?

Master là dòng phát triển chính; nhánh release giữ baseline và chỉ nhận các bản sửa được chọn. Trong quy trình của bài, không merge toàn bộ nhánh release ngược vào master. Lab 05 thực hành chuyển hotfix giữa các dòng bằng cherry-pick để kiểm soát thay đổi và tránh kéo theo thay đổi không phù hợp với dòng đích. Đây là quy ước của bài thực hành, không phải hạn chế kỹ thuật của Git.

## Quy trình này khác GitFlow thế nào?

GitFlow có nhánh develop để tích hợp tính năng; nhánh release thường tách từ develop và sau khi hoàn tất được merge vào master và develop. Bài này dùng master làm dòng phát triển chính, đưa tính năng vào qua PR và tạo release/lab04 từ master để giữ baseline. Không có nhánh develop riêng.

## Vì sao lên 1.0.0 thay vì 0.4.0?

Nhóm quyết định đây là bản ổn định đầu tiên với phạm vi tính năng được chốt và đã kiểm thử: in giỏ, tìm tiêu đề, giảm giá và giới hạn số DVD. Các bản 0.x đại diện cho giai đoạn phát triển ban đầu; 1.0.0 đánh dấu mốc ổn định được cam kết. Đây là quyết định về mức độ ổn định và tương thích, không chỉ do đã hoàn thành Lab 04.
