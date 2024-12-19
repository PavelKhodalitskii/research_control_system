def get_student_information_by_id_query_template(id: int):
    return f"select * from get_student_by_account_id({id});"

def get_student_information_query_template():
    return f"select * from get_all_student_info();"

def get_graduate_student_by_id_query_template(id: int):
    return f"select * from get_graduate_student_by_account_id({id})"

def get_all_graduate_students_info():
    return f"select * from get_all_graduate_students_info()"

def get_researches_by_account_id(id: int):
    return f"select * from get_researches_by_account_id({id})"