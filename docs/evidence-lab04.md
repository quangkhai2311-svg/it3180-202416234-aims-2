# Bằng chứng Lab 04

Thực hiện ngày 07/11/2026, chế độ một mình (0 approval).

## Chuẩn bị và sửa mốc tạo sớm

- [PR #15](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/15): đưa version, banner, CHANGELOG và câu trả lời vào master.
- Người dùng đã tạo release/lab04 và publish v1.0.0 sớm tại mã Lab 03 `fdb1d47ce275d0af468e130ff5bb68ba982b2f0d`, trước khi PR chuẩn bị được merge.
- [PR #16](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/16): bổ sung đúng phần chuẩn bị vào release/lab04; không có sort.
- Chủ repo yêu cầu chuyển tag v1.0.0. Tag được sửa có kiểm tra SHA cũ bằng force-with-lease, không ghi đè các tag khác, không tắt bảo vệ nhánh.
- Commit cũ: `fdb1d47ce275d0af468e130ff5bb68ba982b2f0d`. Commit đúng: `9377807ff75f63cd3d0c28a8a08b19dd82169d34`.
- Tag v1.0.0 là annotated tag và trùng đầu release/lab04. Các tag v0.1.0, v0.2.0, v0.3.0 giữ nguyên.
- Đây là sửa sai khi tạo baseline ban đầu theo yêu cầu của chủ repo, không phải quy trình di chuyển tag cho các bản phát hành tiếp theo.

## Phát triển tiếp

- [PR #17](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/pull/17): thêm sort_by_title(), sort_by_cost(), hai test và mục Unreleased.
- Master có 6 tests OK; v1.0.0 có 4 tests OK và chưa có sort.
- Test giá dùng đầu vào chưa được sắp xếp, kiểm tra đúng thứ tự và tổng tiền không đổi; đã xác nhận test bắt được phương thức không làm gì.
- Vì baseline được sửa sau PR sort, PR tài liệu này còn mang commit đồng bộ quan hệ tổ tiên của baseline vào master. Commit đồng bộ không đổi nội dung mã nguồn master. Đây là thao tác khắc phục mốc tạo sớm, không đưa tính năng sort vào release.

## Status accounting

```text
$ git log --oneline release/lab04..HEAD
415b9fc chore: include corrected baseline ancestry before sort integration
5e320f8 Merge pull request #17 from quangkhai2311-svg/feature/sort-cart
1f045b0 test: exercise sorting with unsorted DVD prices
a863afb feat: add sort_by_title and sort_by_cost to Cart

$ git log --oneline HEAD..release/lab04
(rỗng)

$ git diff --stat v0.3.0 v1.0.0
CHANGELOG.md          | 15 +++++++++++++++
 aims/__init__.py      |  1 +
 docs/answers-lab04.md | 17 +++++++++++++++++
 main.py               |  3 +++
 4 files changed, 36 insertions(+)

$ git diff --stat v1.0.0 HEAD
CHANGELOG.md       |  3 +++
 aims/cart.py       |  6 ++++++
 tests/test_sort.py | 27 +++++++++++++++++++++++++++
 3 files changed, 36 insertions(+)
```

HEAD ở trên là nhánh kiểm toán trước commit tài liệu này. Sau khi PR kiểm toán merge, master chứa toàn bộ baseline và các commit sort/tài liệu.

## Tái tạo và đóng gói

- Đã checkout detached HEAD tại v0.2.0, chạy demo và quay về master.
- Đã tạo worktree riêng từ tag v1.0.0 đã sửa, chạy main.py và 4 tests OK, rồi xóa worktree.
- Banner: AIMS-mini v1.0.0. Tổng tiền demo: 63.89 $.
- git show v1.0.0:aims/__init__.py trả version 1.0.0; cây tag không có ZIP, pyc, __pycache__ hoặc .DS_Store.
- ZIP aims-repo2-1.0.0.zip được tạo bằng git archive từ chính tag v1.0.0, đã mở kiểm tra version/changelog và xác nhận chưa có sort.
- [GitHub Release 1.0.0](https://github.com/quangkhai2311-svg/it3180-202416234-aims-2/releases/tag/v1.0.0) đã cập nhật target release/lab04 và release notes.

## Bảo vệ release

- Ruleset protect release đang Active, áp dụng release/*, không có bypass, cấm force push và xóa nhánh, bắt buộc PR.
- Đã thử push commit nháp trực tiếp vào release/lab04; GitHub từ chối GH013 với Changes must be made through a pull request. Nhánh thử đã xóa.
- Không có review/approval từ partner vì làm một mình.
