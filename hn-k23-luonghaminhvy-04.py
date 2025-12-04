import json
import matplotlib.pyplot as plt

FILE_NAME = "data.json"
bills = []

def display_bills():
    global bills
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        data = json.load(f)
        bills = data["bills"]
    print("bills: ", bills)

def add_bill():
    id = input("Mời nhập mã công tơ: ")

    if len(bills) > 0:
        for i in bills:
            if i["id"] == id:
                print("Mã công tơ đã tồn tại.")
                return
            
    owner_name = input("Mời nhập tên chủ hộ: ")

    if len(bills) > 0:
        for i in bills:
            if i["owner_name"] == owner_name:
                print("Tên chủ hộ đã tồn tại.")
                return
            
    old_electricity_number = input("Nhập số điện cũ: ")
    new_electricity_number = input("Nhập số điện mới: ")
    if float(new_electricity_number) < float(old_electricity_number):
        print("Số điện mới phải lớn hơn hoặc bằng số điện cũ: ")
        return
    consumption = input("Nhập số tiêu thụ: ")
    into_money = input("Nhập thành tiền: ")
    applicable_level = input("Nhập mức áp dụng: ")
    
    bill = {
        "id": id,
        "owner_name": owner_name,
        "old_electricity_number": old_electricity_number,
        "new_electricity_number": new_electricity_number,
        "consumption": consumption,
        "into_money": into_money,
        "applicable_level": applicable_level
    }
    bills.append(bill)
    print("Thêm hoá đơn thành công")

def update_bill():
    id = input("Mời nhập mã công tơ: ")
    found = False
    index = -1

    index = find_index_by_id(id)
    
    if not found:
        print("Không tìm thấy mã công tơ:", id)

    owner_name = input("Mời nhập tên chủ hộ: ")

    if len(bills) > 0:
        for i in bills:
            if i["owner_name"] == owner_name:
                print("Tên chủ hộ đã tồn tại.")
                return

    old_electricity_number = input("Nhập số điện cũ: ")
    new_electricity_number = input("Nhập số điện mới: ")
    if float(new_electricity_number) < float(old_electricity_number):
        print("Số điện mới phải lớn hơn hoặc bằng số điện cũ: ")
        return
    consumption = input("Nhập số tiêu thụ: ")
    into_money = input("Nhập thành tiền: ")
    applicable_level = input("Nhập mức áp dụng: ")

    bills[index]["owner_name"] = owner_name
    bills[index]["old_electricity_number"] = old_electricity_number
    bills[index]["new_electricity_number"] = new_electricity_number
    if bills[index]["new_electricity_number"] < bills[index]["old_electricity_number"]:
        print("Số điện mới phải lớn hơn hoặc bằng số điện cũ: ")
        return
    bills[index]["consumption"] = consumption
    bills[index]["into_money"] = into_money
    bills[index]["applicable_level"] = applicable_level
    print("Cập nhật thành công")

def validate_float_bill_number(float_number, name):
    if float_number < 0:
        raise Exception(f"{name} không được nhỏ hơn 0")
    
def save_build_to_file():
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump({'bills': bills}, f, indent=4, ensure_ascii=False)
    print("Lưu vào file thành công.")

def find_index_by_id(sid):
    for i, s in enumerate(bills):
        if s.get('id') == sid:
            return i
    return None

def delete_bill():
    sid = input("Nhập mã háo đơn ").strip()
    idx = find_index_by_id(sid)
    if idx is None:
        print("Không tìm thấy hoá đơn.")
        return
    
    confirm = input(f"Bạn có chắc muốn xoá {sid}? (y/n): ").strip().lower()
    if confirm == 'y':
        del bills[idx]
        print("Xoá thành công.")
    else:
        print("Đã huỷ.")

def search_bill():
    owner_name = input("Mời nhập tên chủ hộ: ")
    result = None
    for b in bills:
        if owner_name == bills["owner_name"]:
            print(bills["owner_name"])
            return
    print("Không tìm thấy chủ hộ với tên", owner_name)

def sort_bills_by_owner_name():
    print("1. Tăng dần")
    print("2. Giảm dần")
    choice = input("Mời nhập: ")
    if choice == '1':
        bills.sort(key=lambda x: x.get('owner_name', 0))
    elif choice == '2':
        bills.sort(key=lambda x: x.get('owner_name', 0), reverse=True)

def statistic():
    if not bills:
        print("Hoá đơn trống")
        return

    

while True:
    print("---------- Quản lý hoá đơn tiền điện ---------")
    print("1. Hiển thị danh sách hóa đơn")
    print("2. Thêm chỉ số điện")
    print("3. Cập nhật thông tin hóa đơn")
    print("4. Xoá hóa đơn")
    print("5. Tìm kiếm hóa đơn theo tên chủ hộ")
    print("6. Sắp xếp danh sách hóa đơn")
    print("7. Thống kê doanh thu")
    print("8. Vẽ biểu đồ thống kê mức tiêu thụ")
    print("9. Lưu vào file CSV")
    print("10. Thoát")
    choice = input("Mời nhập số từ 1-10: ")
    if choice == '1':
        display_bills()
    elif choice == '2':
        add_bill()
    elif choice == '3':
        update_bill()
    elif choice == '4':
        delete_bill()
    elif choice == '5':
        search_bill()
    elif choice == '6':
        sort_bills_by_owner_name()
    elif choice == '7' or choice == '8':
        print("Tính năng đang trong quá trình phát triển")
    elif choice == '9':
        save_build_to_file()
    elif choice == '10':
        pass
    else:
        print("Không hợp lệ.")