# Trả lời thảo luận Lab 01

## 1. Cấu hình --global được lưu ở đâu? Khác --local thế nào?

Cấu hình `--global` áp dụng cho các repository của tài khoản người dùng trên
máy. Git thường lưu cấu hình này trong `~/.gitconfig`; cũng có thể đọc cấu
hình từ đường dẫn XDG. Cấu hình `--local` nằm trong `.git/config` và chỉ áp
dụng cho repository hiện tại. Với cùng một khóa, giá trị local được ưu tiên
hơn global. Dùng `git config --list --show-origin` để xem nguồn cấu hình.

## 2. Vì sao dùng git mv?

`git mv` chuyển hoặc đổi tên tệp trong working tree và đồng thời stage thay
đổi. Git suy luận rename dựa trên mức độ giống nhau của nội dung khi xem
diff; Git không lưu một thuộc tính rename riêng. Vì vậy, chuyển tệp bằng
`mv` rồi `git add -A` cũng có thể được nhận diện là rename.

Trong bài này, dùng `git mv` để chuyển `cart.py` và `dvd.py` vào `aims/`,
giữ nguyên nội dung trong commit chuyển tệp. Lệnh
`git log --oneline --follow -- aims/cart.py` giúp xem lịch sử qua lần đổi tên.

## 3. release/lab01 có phải baseline không?

Có. Nhánh `release/lab01` được tạo từ `master` sau khi PR refactor đã được
merge và chương trình đã được kiểm tra. Nhánh này ghi nhận mốc bài nộp
Lab 01. Ngay khi tạo, hai nhánh có cùng SHA commit.

Đầu nhánh release có thể thay đổi khi thực hiện hotfix theo quy trình ở các
lab sau. Tag phát hành bổ sung một định danh chính xác cho một phiên bản;
tag đã chia sẻ không được di chuyển tùy ý.

## 4. Vì sao vẫn dùng Pull Request khi làm một mình?

PR ghi lại mục đích, phạm vi thay đổi, diff và cách kiểm tra trước khi tích
hợp. Người làm có thể tự review, phát hiện thay đổi ngoài ý muốn và truy
vết quyết định merge. Quy trình này cũng giúp duy trì cách làm nhất quán
khi sau này có thêm người cùng phát triển.

## Kiểm tra sau refactor

Chạy `python3 main.py` từ thư mục gốc repository, kết quả tổng tiền vẫn là
`Total cost: 63.89 $`. Hai module đã chuyển vào package `aims`, imports trong
`main.py` đã cập nhật; `__pycache__/` được bỏ qua bởi `.gitignore`.
