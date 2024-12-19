def get_teacher_information_by_id_query_template(id: int):
    return f"select * from get_teacher_by_account_id({id});"

def get_teachers_information_query_template():
    return f"select * from get_all_teachers_info();"