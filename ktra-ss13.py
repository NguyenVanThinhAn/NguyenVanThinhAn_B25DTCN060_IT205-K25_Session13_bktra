data = [{'id': 1, 'type': "Xe tải", 'owner': "andepzai"},{'id': 2, 'type': "Xe máy", 'owner': "andepzai"},]
setting = {
    "col1": 10,
    "col2": 10,
    "col3": 10,
    "line_length":30
}

while True:
    select = input("""
QUẢN LÝ BÃI XE SMART PARKING
1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Tìm kiêm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoát chương trình
""")
    
    match select:
        case "1":
            type_in = input("Nhập loại xe: ").strip()
            owner_in = input("Nhập tên chủ xe: ").strip()

            data.append({"id": len(data) + 1,"type":type_in,"owner":owner_in})

        case "2":
            print(f"{"ID":<{setting["col1"]}}|{"Loại xe":<{setting["col2"]}}|{"Chủ xe":<{setting["col1"]}}")
            print("-"* setting["line_length"])
            for i,v in enumerate(data):
                if v.get("deleted"):
                    continue
                print(f"{v["id"]:<{setting["col1"]}}|{v["type"]:<{setting["col2"]}}|{v["owner"]:<{setting["col3"]}}")
        case "3":
            id_in = None
            while True:
                try:
                    id_in = int(input("Nhập id xe bạn muốn tìm: "))
                    break
                except:
                    print("Lỗi, vui lòng nhập lại")
            id_in -= 1
            
            try:
                if data[id_in]:
                    v = data[id_in]
                    print(f"{v["id"]}|{v["type"]}|{v["owner"]}")
                else:
                    raise Exception("Không tìm thấy dữ liệu!!!")
            except:
                print("Không tìm thấy dữ liệu")
        case "4":
            id_in = None
            while True:
                try:
                    id_in = int(input("Nhập id xe bạn muốn tìm: "))
                    break
                except:
                    print("Lỗi, vui lòng nhập lại")
            id_in -= 1
            
            try:
                if data[id_in]:
                    data[id_in]["deleted"] = True
                    print("Đã xóa xe")
                else:
                    raise Exception("Không tìm thấy xe có ID",id_in + 1)
            except:
                print("Không tìm thấy xe để xóa")
        case "5":
            print("Đã xóa")
            break
        case _:
            print("Vui lòng nhập (1-5)")
