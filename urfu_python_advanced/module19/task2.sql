select
  name,
  avg(g.grade) as avg_grade
from
  students
  inner join grades g on students.id = g.student_id
group by
  students.id
order by
  avg_grade desc
limit
  10