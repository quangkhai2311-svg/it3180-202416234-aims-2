# Trả lời thảo luận Lab 02

## 1. Vì sao cần đồng bộ với master trước khi mở hoặc merge PR?

Trong khi Dev 2 làm tìm kiếm, Dev 1 đã đưa chức năng in giỏ vào master. Đồng bộ giúp nhánh tìm kiếm nhận các thay đổi đó, phát hiện xung đột và kiểm tra chương trình khi hai phần cùng tồn tại. Chạy thử trên nhánh cũ chỉ chứng minh mã cũ hoạt động.

Ở bài này, bản clone Dev 2 bắt đầu trước khi PR in giỏ được merge. Sau commit tìm kiếm, thực hiện `git fetch origin` và `git merge origin/master`, chạy lại `python3 main.py`, rồi push nhánh và mở PR. `fetch` cập nhật thông tin remote; `merge` tích hợp thay đổi vào nhánh hiện tại.

## 2. Khi nào không nên rebase?

Không rebase các commit đã chia sẻ mà người khác đang dựa vào, đặc biệt master và các nhánh release. Rebase viết lại commit với SHA mới; đẩy lịch sử đã viết lại có thể buộc cộng tác viên sửa lịch sử của họ. Với nhánh dùng chung, dùng merge để đồng bộ. Rebase phù hợp với commit riêng chưa chia sẻ, hoặc khi cả nhóm đã thống nhất cách phối hợp.

`Rebase and merge` của GitHub trong PR tài liệu đưa các commit lên master hiện tại theo chuỗi tuyến tính. Thao tác này khác với tự rebase rồi force-push master.

## 3. feature/* khác topic/* thế nào?

Đây là quy ước đặt tên, không phải hai loại nhánh có cơ chế Git khác nhau. `feature/cart-print` và `feature/search-by-title` bổ sung chức năng chương trình; `topic/pr-template` và `topic/use-case-diagram` gom thay đổi theo chủ đề tài liệu hoặc quy trình. Cả hai đều tách từ master, commit, push và tích hợp qua PR.

## 4. Ba cách merge đã thực hành

| Cách | Áp dụng | Lịch sử sau tích hợp |
| --- | --- | --- |
| Create a merge commit | PR in giỏ | Giữ các commit của nhánh và thêm merge commit có hai parent. |
| Squash and merge | PR tìm kiếm | Gộp thay đổi thành một commit mới trên master. |
| Rebase and merge | PR tài liệu use case | Đưa từng commit lên master, không tạo merge commit; SHA có thể đổi. |

## 5. Review và bảo vệ master

Repo yêu cầu thay đổi đi qua PR, áp dụng cả với quản trị viên và hủy approval cũ khi có commit mới. Bài được thực hiện một mình nên đặt 0 approval; tác giả tự kiểm tra diff và kết quả chạy. Không có partner thực hiện Request changes hoặc Approve. Trong PR in giỏ, phần xử lý giỏ trống được bổ sung sau khi PR đã mở, trên cùng nhánh.
