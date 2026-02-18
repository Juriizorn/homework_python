from sqlalchemy import create_engine, text


class ClassTeacher:

    __script = {
        "get_list_teacher": text("SELECT * FROM teacher"),
        "add_new_teacher": text("INSERT INTO teacher "
                                "(\"teacher_id\", \"email\", \"group_id\") "
                                "VALUES (:teacher_id, :email, :group_id)"),
        "update_teacher": text("UPDATE teacher SET email = :email, "
                               "group_id = :group_id "
                               "WHERE teacher_id = :teacher_id"),
        "delete_teacher": text("DELETE FROM teacher "
                               "WHERE teacher_id = :teacher_id"),
        "get_teacher_by_id": text("SELECT * FROM teacher "
                                  "WHERE teacher_id = :teacher_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_list_teacher(self):
        conn = self.__db.connect()
        resp = conn.execute(self.__script["get_list_teacher"])
        return resp.mappings().all()

    def add_new_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(self.__script["add_new_teacher"],
                     {"teacher_id": teacher_id,
                      "email": email, "group_id": group_id})
        conn.commit()
        conn.close()

    def update_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(self.__script["update_teacher"],
                     {"teacher_id": teacher_id,
                      "email": email, "group_id": group_id})
        conn.commit()
        conn.close()

    def delete_teacher(self, teacher_id):
        conn = self.__db.connect()
        conn.execute(self.__script["delete_teacher"],
                     {"teacher_id": teacher_id})
        conn.commit()
        conn.close()

    def get_teacher_by_id(self, teacher_id):
        conn = self.__db.connect()
        resp = conn.execute(self.__script["get_teacher_by_id"],
                            {"teacher_id": teacher_id})
        return resp.mappings().all()
