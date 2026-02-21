from ClassTeacher import ClassTeacher

db = ClassTeacher("postgresql://postgres:123@localhost:5432/postgres")


def test_add_teacher():
    teacher_id = 55555
    email = '555sss@gmail.com'
    group_id = 66666

    db.add_new_teacher(teacher_id, email, group_id)
    new_teacher = db.get_teacher_by_id(teacher_id)
    db.delete_teacher(teacher_id)

    assert new_teacher[0]["teacher_id"] == teacher_id
    assert new_teacher[0]["email"] == email
    assert new_teacher[0]["group_id"] == group_id


def test_update_teacher():
    teacher_id = 55555
    email = '555sss@gmail.com'
    group_id = 66666

    db.add_new_teacher(teacher_id, email, group_id)

    new_email = '666ccc@gmail.com'
    new_group_id = 77777

    db.update_teacher(teacher_id, new_email, new_group_id)
    update_teacher = db.get_teacher_by_id(teacher_id)
    db.delete_teacher(teacher_id)

    assert update_teacher[0]["email"] == new_email
    assert update_teacher[0]["group_id"] == new_group_id


def test_delete_teacher():
    teacher_id = 55555
    email = '555sss@gmail.com'
    group_id = 66666

    db.add_new_teacher(teacher_id, email, group_id)
    new_teacher = db.get_teacher_by_id(teacher_id)
    db.delete_teacher(teacher_id)
    delete_teacher = db.get_teacher_by_id(teacher_id)

    assert new_teacher[0]["teacher_id"] == teacher_id
    assert new_teacher[0]["email"] == email
    assert new_teacher[0]["group_id"] == group_id

    assert len(delete_teacher) == 0
