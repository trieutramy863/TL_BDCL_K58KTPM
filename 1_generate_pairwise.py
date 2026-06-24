from allpairspy import AllPairs
import pandas as pd

# 1. Khai báo các tham số cấu hình của hệ thống
parameters = [
    ["Chrome", "Firefox", "Edge"],            # Trình duyệt
    ["Windows", "macOS", "Linux"],            # Hệ điều hành
    ["Visa", "MasterCard", "MoMo"],           # Cổng thanh toán
    ["Khach_Thuong", "Khach_VIP"]             # Hạng thành viên
]

columns = ["Browser", "OS", "Payment_Method", "Membership"]

# 2. Chạy thuật toán Pairwise
test_cases = []
for i, pairs in enumerate(AllPairs(parameters)):
    test_cases.append(pairs)

# 3. In ra màn hình
df = pd.DataFrame(test_cases, columns=columns)
print(f"Tổng số Test Cases ban đầu (nếu nhân chéo toàn bộ): 3 x 3 x 3 x 2 = 54")
print(f"Tổng số Test Cases sau khi tối ưu Pairwise: {len(df)}")
print("-" * 50)
print(df)

# 4. Lưu ra file CSV
df.to_csv("pairwise_testcases.csv", index=False)
print("\n=> Đã lưu danh sách kịch bản vào file 'pairwise_testcases.csv'")