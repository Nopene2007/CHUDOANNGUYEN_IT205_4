order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]
# Khởi tạo danh sách đơn hàng ban đầu theo yêu cầu
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]
choice= 0
while True:
    # HIỂN THỊ MENU CHÍNH
    choice=input('''\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình
==================================================
    "Nhập lựa chọn của bạn (1-4): "''').strip()
    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\nDanh sách đơn hàng hiện tại:")
                for i, order in enumerate(order_list):
                    print(f"{i+1}. {order}")
        case "2":
            while True:
                choice=input('''\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
---------------------------------------
    Nhập lựa chọn của bạn (1-4):''').strip()
                match choice:

                    case "1":
                        new_code = input("Nhập mã đơn hàng mới: ")
                        new_status = input("Nhập trạng thái đơn hàng (PENDING, DELIVERING, COMPLETED, CANCELLED): ")

                        news_code = new_code.strip().upper()
                        news_status = new_status.strip().upper()

                        new_order = f"{news_code} - {news_status}"
                        order_list.append(new_order)
                        print("Đã thêm thành công đơn hàng mới vào hệ thống.")

                    case "2":
                        new_position = input("Nhập vị trí đơn hàng cần sửa: ").strip()

                        if not new_position.isdigit():
                            print("Vị trí không hợp lệ! Vui lòng nhập số nguyên dương.")
                            continue
                        position = int(new_position)
                        i = position - 1

                        if 0 <= i < len(order_list):
                            new_code = input("Nhập mã đơn hàng mới: ")
                            new_status = input("Nhập trạng thái mới: ")
                            
                            code = new_code.strip().upper()
                            status = new_status.strip().upper()
                            
                            order_list[i] = f"{code} - {status}"
                            print(f"Đã cập nhật thành công đơn hàng tại vị trí {position}.")
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case "3":
                        position = input("Nhập vị trí đơn hàng cần xóa: ").strip()

                        if not position.isdigit():
                            print("Vị trí không hợp lệ! Vui lòng nhập số nguyên dương.")
                            continue
                            
                        positions = int(position)
                        i = positions - 1

                        if 0 <= i < len(order_list):
                            removed_order = order_list.pop(i)
                            print(f"Đã xóa thành công đơn hàng: {removed_order}")
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case "4":
                        print("Quay lại menu chính thành công.")
                        break
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                        

        case "3":
            count_pending = 0
            count_delivering = 0
            count_completed = 0
            count_cancelled = 0
            for i in order_list:
                parts = i.split(" - ")
                if len(parts) == 2:
                    status = parts[1].strip().upper()
                    match status:
                        case "PENDING":
                            count_pending += 1
                        case "DELIVERING":
                            count_delivering += 1
                        case "COMPLETED":
                            count_completed += 1
                        case "CANCELLED":
                            count_cancelled += 1
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {count_pending}")
            print(f"DELIVERING: {count_delivering}")
            print(f"COMPLETED: {count_completed}")
            print(f"CANCELLED: {count_cancelled}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        case "4":
            print("Thoát chương trình.")
            break 

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")