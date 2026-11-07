# Bằng chứng Lab 03

Thực hiện ngày 07/11/2026, chế độ một mình (0 approval). Không có review/approval từ partner.

## Các PR và Issue

- [Issue #7](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/issues/7): đã đóng sau PR sửa giới hạn giỏ.
- [PR #8](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/8): test giới hạn giỏ trước fix, rồi sửa điều kiện `>` thành `>=`. Từ khóa đóng Issue đúng nằm trong mô tả PR (`Fixes #7`); commit cũ giữ nguyên lịch sử.
- [PR #9](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/9): Bugfix có base feature/discount; test đỏ trước sửa, 4 tests xanh sau sửa.
- [PR #10](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/10): Đưa tính năng giảm giá đã sửa vào master.
- [PR #11](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/11): Nhánh thứ nhất đổi thông báo sang tiếng Việt.
- [PR #12](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/12): PR ban đầu conflict; merge master, kết hợp tiếng Việt và tên DVD, chạy lại 4 tests.
- [PR #13](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/13): Revert merge commit thêm tên DVD qua PR, giữ nguyên lịch sử.

## Conflict thực tế

- Hai nhánh tạo từ cùng commit `d2727f5da9ddfa545f70f789901b86450e0a0262`.
- Merge base tìm được: `d2727f5da9ddfa545f70f789901b86450e0a0262`.
- GitHub xác nhận PR CONFLICTING; git merge origin/master trả conflict ở aims/cart.py.
- Commit giải quyết conflict: `34ffe3399d55bca558d81ca1f2df2cf6077242e4`.
- Merge commit được revert: `4a502145bcba959a6b6b61fec87a2dc30658d9fb`.
- Nội dung kết hợp trước revert: `print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`.
- Sau revert: `print("Đã thêm đĩa vào giỏ hàng")`.

## Reset và reflog ở máy

- Nhánh topic/undo-practice chỉ ở máy, không push.
- Sau soft reset: `A  undo-practice.txt` (file còn staged).
- Sau mixed reset: `?? undo-practice.txt` (file mới trở thành untracked).
- Sau hard reset: file nháp bị loại khỏi working tree; master không bị reset.
- Commit tìm lại bằng reflog: `c038233002b8a1a3d2eca1aca44a01d421f4b277`.
- Tạo nhánh local rescue/undo-practice từ commit tìm lại, đọc file bằng:

```bash
git show rescue/undo-practice:undo-practice.txt
```

Kết quả: `local reset practice`.

## Kiểm tra cuối

```bash
python3 -m unittest discover -s tests -v
python3 main.py
```

- 4 tests OK: giới hạn 20 DVD, tổng tiền, giảm 20%, phần trăm ngoài khoảng.
- Demo tổng tiền gốc 63.89 $. Không còn dấu conflict.
- Sau khi PR tài liệu merge, tạo release/lab03 từ master. Giữ nguyên release/lab01 và release/lab02.
- Issue #6 trùng chủ đề do người dùng tạo vẫn được giữ nguyên; Issue dùng cho bài là #7.
