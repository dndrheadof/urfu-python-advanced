select
  name,
  avg(g.grade) as avg_grade
from
  teachers
  inner join assignments a on teachers.id = a.teacher_id
  inner join grades g on a.id = g.assignment_id
group by
  name
order by
  avg_grade
limit
  1