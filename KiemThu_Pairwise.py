import pandas as pd
import time


# Đã đổi tên hàm thành check_system_checkout để PyCharm không nhầm với Pytest
def check_system_checkout(browser, os, payment, membership):
    # Cố tình cài cắm một lỗi bậc 2 (Lỗi do 2 tham số đụng nhau)
    if os == "macOS" and payment == "MoMo":
        return "FAILED (Lỗi: macOS không mở được app MoMo)"

    # Cố tình cài cắm một lỗi bậc 3 (Lỗi do 3 tham số đụng nhau)
    if browser == "Edge" and os == "Linux" and payment == "Visa":
        return "FAILED (Lỗi bậc 3: Crash hệ thống thanh toán)"

    return "PASSED"


print("BẮT ĐẦU CHẠY KIỂM THỬ TỰ ĐỘNG DỰA TRÊN FILE CSV...")
# Đọc file dữ liệu đã sinh ra từ trước
df = pd.read_csv("pairwise_testcases.csv")

results = []
for index, row in df.iterrows():
    print(f"\nĐang chạy TC{index + 1}: {row['Browser']} | {row['OS']} | {row['Payment_Method']} | {row['Membership']}")
    time.sleep(0.5)

    # Chạy hàm kiểm tra với tên mới
    status = check_system_checkout(row['Browser'], row['OS'], row['Payment_Method'], row['Membership'])
    print(f"Kết quả: {status}")
    results.append(status)

df['Test_Result'] = results
print("\n" + "=" * 50)
print("BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST REPORT)")
print(f"Tổng số ca kiểm thử: {len(df)}")
print(f"Số ca PASSED: {results.count('PASSED')}")
print(f"Số ca FAILED: {len(df) - results.count('PASSED')}")