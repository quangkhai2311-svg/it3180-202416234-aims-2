# Trả lời Lab 05

## Upstream first so với release first

Upstream first sửa trên master trước rồi backport về các bản phát hành. Cách này giảm khả năng quên sửa dòng mới, nhưng patch có thể cần điều chỉnh cho mã cũ. Release first sửa ở đúng bản phát hành bị ảnh hưởng trước, giúp tái hiện và kiểm tra baseline thực tế; cần chủ động đưa bản sửa sang tất cả dòng còn bị ảnh hưởng. Bài áp dụng release first.

## Quên đưa bản sửa sang release/lab05 thì phát hiện thế nào?

Chạy cùng kiểm tra tìm lion trên v1.0.1, v1.1.0 và master; dòng chưa sửa trả 0 thay vì 1. Trước khi gắn tag v1.1.0, kiểm tra release/lab05. Dùng git cherry -v origin/release/lab05 origin/release/lab04 để tìm patch tương đương. Dấu - trước bản sửa cho biết dòng đích đã có patch tương đương. git tag --contains FIX_SHA chỉ xét tổ tiên, không đủ để kết luận về một bản cherry-pick có SHA khác.

## Vì sao tách sửa lỗi và bump version?

Commit code/test được cherry-pick -x sang các dòng 1.1.0. Commit bump 1.0.1 và changelog của dòng cũ ở riêng để không hạ version mới. Dòng (cherry picked from commit ...) giữ truy vết nguồn patch.

## Vì sao chưa tạo tag v1.1.0 ở đầu bài?

Baseline cần nhận hotfix trước khi được chốt. Tag đã chia sẻ giữ nguyên; nếu đã phát hành 1.1.0 rồi mới sửa thì phát hành 1.1.1, không di chuyển tag cũ.

## CI hỗ trợ gì?

Workflow chạy unittest trên PR vào master/release/** và push master. Khi check test được đặt là required trên master và không có bypass, CI lỗi chặn merge. PR cố ý làm sai total_cost chỉ để chứng minh điều này và phải đóng, không merge.
