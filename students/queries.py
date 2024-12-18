def get_student_information_by_id_query_template(id: int):
    return f"select * from get_student_by_account_id({id});"

def get_student_information_query_template():
    return f"select * from get_all_student_info();"