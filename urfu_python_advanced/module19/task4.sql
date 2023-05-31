select
  group_id,
  count(assisgnment_id) as count_overdue_tasks,
  round(avg(overdue_tasks_count)) as avg_overdue,
  max(overdue_tasks_count) max_overdue,
  min(overdue_tasks_count) min_overdue
from
(
    select
      group_id,
      assignments.assisgnment_id,
      SUM(assignments_grades.date > assignments.due_date) as overdue_tasks_count
    from
      assignments
      inner join assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
    group by
      assignments.assisgnment_id
  )
group by
  group_id