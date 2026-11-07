# Trả lời Lab 03

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit. Git dùng trạng thái này và hai đầu nhánh để xác định phần thay đổi của mỗi phía khi merge ba chiều.

Trong bài này, hai nhánh thông báo tạo từ cùng commit, sau đó cùng sửa một dòng. Khi master nhận thông báo tiếng Việt còn nhánh Dev 2 thêm tên DVD vào thông báo tiếng Anh, Git không tự quyết định nội dung cần giữ. Đã chạy `git merge-base HEAD origin/master`, rồi `git merge origin/master` để tái hiện và giải quyết conflict bằng cách giữ cả tiếng Việt và tên DVD.

## Vì sao master và release/* phải dùng revert?

Đó là lịch sử đã chia sẻ hoặc mốc phát hành cần truy vết. Revert tạo commit đảo ngược, giữ nguyên các commit trước đó để cộng tác viên tiếp tục đồng bộ bình thường. Reset hoặc rebase làm con trỏ hay SHA thay đổi, có thể dẫn tới ghi đè lịch sử đã chia sẻ.

Với merge commit của PR thêm tên DVD, dùng `git revert -m 1 SHA`: parent 1 là master trước lần merge đó. Commit revert được tạo trên nhánh bugfix và đưa vào master qua PR.

## Reset soft, mixed và hard khác nhau thế nào?

| Lệnh | HEAD | Staging | Working tree |
| --- | --- | --- | --- |
| reset --soft | Lùi về commit đích | Giữ nguyên | Giữ nguyên |
| reset --mixed | Lùi về commit đích | Đặt lại theo commit đích | Giữ nguyên |
| reset --hard | Lùi về commit đích | Đặt lại | Đặt lại các file được theo dõi |

Đã thực hành trên nhánh nháp không push, chỉ với một file tự tạo. Sau hard reset, dùng reflog tìm lại commit và tạo nhánh rescue để đọc lại nội dung file. Reflog không bảo đảm khôi phục nội dung chưa từng được commit. Với rebase, chỉ thực hiện trên nhánh riêng chưa chia sẻ; có thể bỏ dở bằng `git rebase --abort`. Bài này chọn cách merge để xử lý conflict.

## Vì sao test phải fail trước fix?

Test đỏ trên mã cũ chứng minh nó tái hiện đúng lỗi. Khi cùng test chuyển xanh sau sửa, test trở thành regression test để phát hiện lỗi tái xuất hiện. Test giới hạn giỏ và test giảm giá đều được commit trước bản sửa tương ứng.

## Vì sao PR sửa giảm giá có base feature/discount?

Lỗi nằm trên tính năng chưa được tích hợp vào master. Bugfix được tạo từ origin/feature/discount trong bản Dev 2, sửa và kiểm tra trên chính dòng phát triển đó. Sau khi PR bugfix vào feature được merge, mới mở PR tính năng vào master. Chọn master làm base cho PR bugfix lúc này sẽ làm sai luồng tích hợp.
