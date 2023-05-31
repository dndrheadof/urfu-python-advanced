select
  g.assisgnment_id,
  round(avg(grade), 2) as avg_grade,
  assignment_text
from
  grades as g
  inner join (
    select
      assisgnment_id,
      assignment_text
    from
      assignments
    where
      assignment_text like 'прочитать%'
      or assignment_text like 'выучить%'
  ) as a on a.id = g.assisgnment_id
group by
  a.id