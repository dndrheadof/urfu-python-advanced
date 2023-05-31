select
  name
from
  students
  inner join students_groups sg on students.group_id = sg.id
  inner join (
    select
      teachers.teacher_id,
      AVG(g.grade) as avg_grade
    from
      teachers
      inner join assignments a on teachers.id = a.teacher_id
      inner join grades g on a.id = g.assisgnment_id
    group by
      name order_by avg_grade desc
    limit
      1
  ) as easy_teacher
WHERE
  sg.teacher_id = easy_teacher.id