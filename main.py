import nt

from tabula.io import read_pdf
import pandas as pd
import numpy as np
import boto3

def get_path_page_pdf_file (path_file, start_page, end_page, chunk_size=10) :
    all_dfs = []  # Danh sách lưu trữ tất cả các DataFrame
    try:

        # reader_pdf = read_pdf(path_file, pages = page_file,multiple_tables=True)
        # return reader_pdf

        # Đọc dữ liệu theo từng phần để giảm tải bộ nhớ
        for page in range(start_page, end_page + 1, chunk_size):
            # Xác định trang kết thúc cho phần hiện tại
            chunk_end_page = min(page + chunk_size - 1, end_page)
            print(f"Reading pages {page} to {chunk_end_page} in sao-ke.pdf file...")

            # Đọc dữ liệu từ phần hiện tại
            dfs = read_pdf(path_file, pages=f'{page}-{chunk_end_page}', multiple_tables=True)
            all_dfs.extend(dfs)  # Thêm các DataFrame của phần hiện tại vào danh sách
    except Exception as e:
        print(f"Error somthing: ",e)
        return None
    return all_dfs
def switch_case(value):
    switcher = {
        1: "01/09/2024",
        2: "02/09/2024",
        3: "03/09/2024",
        4: "04/09/2024",
        5: "05/09/2024",
        6: "06/09/2024",
        7: "07/09/2024",
        8: "08/09/2024",
        9: "09/09/2024",
        10: "10/09/2024"

    }
    return switcher.get(value, "Default Value")

def set_header_from_first_n_rows(df, n=4):
    """
    Thiết lập tiêu đề cột từ n dòng đầu tiên của DataFrame và loại bỏ các dòng này khỏi DataFrame.
    """
    if df is not None and len(df) > n:
        # Lấy n dòng đầu tiên để làm tiêu đề
        new_header = df.iloc[:n].values.tolist()
        # print('>>> test:', new_header)

        # Đặt tiêu đề cột mới
        df.columns = ["Date","Debit","Credit","Balance","Transaction Detail"]
        # Loại bỏ các dòng đã được sử dụng làm tiêu đề
        df = df[n:].reset_index(drop=True)
        return df
    else:
        print("DataFrame không đủ dòng để làm tiêu đề.")
        return df


def set_a_loop_data(df, n=0):
    """
    Thiết lập tiêu đề cột từ n dòng đầu tiên của DataFrame và loại bỏ các dòng này khỏi DataFrame.
    """
    if df is not None and len(df) > n:
        # Loại bỏ các dòng đã được sử dụng làm tiêu đề
        check_case_1 = 0
        value_date = ''
        all_items_groups = []  # Mảng tổng để chứa tất cả các nhóm items
        current_group = []  # Mảng lưu tạm cho mỗi nhóm items khi check_case_1 thay đổi

        New_Array = df.iloc[n:].values.tolist()
        for items in New_Array:
            previous_check_case_1 = check_case_1
            for mini_items in items:
                if (mini_items == switch_case(1) or mini_items == switch_case(2) or mini_items == switch_case(3)
                    or mini_items == switch_case(4) or mini_items == switch_case(5) or mini_items == switch_case(6)
                    or mini_items == switch_case(7) or mini_items == switch_case(8) or mini_items == switch_case(9)
                    or mini_items == switch_case(10)
                ):
                    check_case_1 = check_case_1 + 1

            if check_case_1 != previous_check_case_1:
                if current_group:
                    # Đóng nhóm hiện tại trước khi thay đổi check_case_1
                    all_items_groups.append(current_group)
                # Khởi tạo nhóm mới với giá trị items hiện tại làm value_date
                current_group = [items]
            else:
                # Nếu không có sự thay đổi trong check_case_1, tiếp tục thêm items vào nhóm hiện tại
                current_group.append(items)

        if current_group:
            all_items_groups.append(current_group)

        return all_items_groups
    else:
        print("DataFrame không đủ dòng để làm tiêu đề.")
        return df

def analysis_data_important(data):
    Array_Date = []
    Array_Credit = []

    Array_TransactionId = []


    grouped_content = []  # Danh sách tổng lưu trữ các nhóm content theo từng date
    current_content_group = []  # Nhóm tạm thời để lưu trữ content cho mỗi date
    current_date = 0  # Biến để theo dõi date hiện tại
    for items in data:
        previous_current_date = current_date
        if(items[0][0]):
            # Array_Date.append(items[0][0])
            new_date = items[0][0]
            current_date = current_date + 1
            if current_date != previous_current_date:
                if current_content_group:
                    # print("Appending current group:", current_content_group)
                    grouped_content.append(current_content_group)  # Lưu nhóm cũ vào danh sách tổng
                current_content_group = []  # Khởi tạo nhóm content mới
                # current_date = new_date  # Cập nhật date mới
                Array_Date.append(new_date)  # Thêm date vào danh sách


        if (items[1][2]):
             Array_Credit.append(items[1][2])
        if (items[2][0]):
            Array_TransactionId.append(items[2][0])

        for mini_items in items:

                # Kiểm tra nếu mini_items[4] là số và không phải NaN

                if mini_items[4] is not np.nan:

                        current_content_group.append(mini_items[4])  # Thêm giá trị vào nhóm tạm thời
                        # Array_Content.append(mini_items[4])

    if current_content_group:
        grouped_content.append(current_content_group)
    # print(grouped_content)

    for index, data in enumerate(grouped_content):
        # data là mảng, chúng ta nối các phần tử của mảng thành một chuỗi
        grouped_content[index] = ' '.join(map(str, data))  # Nối các phần tử thành một chuỗi với dấu cách giữa các phần tử
    TOTAL_ARRAY = [Array_Date, Array_TransactionId, Array_Credit, grouped_content]
    return TOTAL_ARRAY

def convert_to_int(array):
    converted_array = []
    for item in array:
        try:
            # Remove any unwanted characters before conversion
            item = str(item).replace(".", "").replace(",", "")
            converted_array.append(int(item))
        except ValueError:
            print(f"Không thể chuyển đổi giá trị: {item}")
    return converted_array

def convert_to_str(array):
    converted_array = []
    for item in array:
        try:
            # Remove any unwanted characters before conversion
            item = str(item).replace(".", "").replace(",", "")
            converted_array.append(str(item))
        except ValueError:
            print(f"Không thể chuyển đổi giá trị: {item}")
    return converted_array

path_file = "./sao-ke.pdf"
# doc cac trang pdf
dfs = get_path_page_pdf_file(path_file, 2,12028,10)

def pad_array(array, target_length, pad_value):
    return array + [pad_value] * (target_length - len(array))

if dfs is not None:
    print(len(dfs))
    if len(dfs) >= 1:
        TOTAL_DATE = []
        TOTAL_CREDIT = []
        TOTAL_TRANSACTION = []
        TOTAL_CONTENT = []
        for index, df in enumerate(dfs):
            # print(f"Processing DataFrame from page {index + 2}")  # Index + 2 vì bắt đầu từ trang 2

            df = set_header_from_first_n_rows(df, n=4)
            check_test = set_a_loop_data(df, 0)

            result = analysis_data_important(check_test)

            Array_Date = result[0]
            Array_Date = convert_to_str(Array_Date)
            TOTAL_DATE.extend(Array_Date)
            Array_TransactionId = result[1]
            try:
                Array_TransactionId = [str(n).replace(".", "") for n in Array_TransactionId]
                Array_TransactionId = [int(n) for n in Array_TransactionId]
            except ValueError:
                print("Lỗi khi chuyển đổi TransactionId.")
                continue
            Array_TransactionId = convert_to_int(Array_TransactionId)
            TOTAL_TRANSACTION.extend(Array_TransactionId)

            Array_Credit = result[2]
            try:
                Array_Credit = [str(n).replace(".", "") for n in Array_Credit]
                Array_Credit = [int(n) for n in Array_Credit]
            except ValueError:
                print("Lỗi khi chuyển đổi Credit.")
                continue

            Array_Credit = convert_to_int(Array_Credit)
            TOTAL_CREDIT.extend(Array_Credit)

            grouped_content = result[3]
            grouped_content = [str(n).replace(",", "") for n in grouped_content]

            grouped_content = convert_to_str(grouped_content)
            TOTAL_CONTENT.extend(grouped_content)

            #xu ly cac data bi thieu
            TOTAL_CREDIT = pad_array(TOTAL_CREDIT, len(TOTAL_DATE), 0)
            TOTAL_CONTENT = pad_array(TOTAL_CONTENT, len(TOTAL_DATE), "DỮ LIỆU KHÔNG THOÃ MÃN !")


        # print('>>> check :',TOTAL_CONTENT)
        saoke_dict = {
                "Date": TOTAL_DATE,
                "TransactionId": TOTAL_TRANSACTION,
                "Amount": TOTAL_CREDIT,
                "Content": TOTAL_CONTENT
            }

        try:
            saoke_df = pd.DataFrame(saoke_dict)
            csv_file = "sao-ke.csv"
            saoke_df.to_csv(csv_file, index=False)
            print("===========================================")
            print("Quá trình ghi file CSV hoàn tất.")
        except Exception as e:
            print(f"Lỗi khi tạo hoặc ghi CSV: {e}")

    else:
            print("Không đủ bảng dữ liệu trên trang chỉ định.")
else:
        print("Không có DataFrame để hiển thị.")




# AFTTER CREATE SAO-KE.CSV FILE.NOW WE HAVE TO CREATE CLIENT TO UP LOAD TO S3 AWS

s3 = boto3.client("s3")

S3_BUCKET_NAME = "liem-project"
S3_FOLDER_ROUTE = "python/liems-project/"

print("HELLO WORLD !")

#Upload file csv
csv_file = "sao-ke.csv"
with open(csv_file,"rb") as f:
    s3.upload_fileobj(f,S3_BUCKET_NAME,S3_FOLDER_ROUTE + csv_file)
print("LOAD THANH CONG ! :V")