SELECT Name
FROM (
    SELECT Manage.Name as Name, count(Report.id) as cnt 
    FROM
    Employee as Manager join Employee as Report
    ON Manager.Id = Report.ManagerId
    GROUP BY Manager.Id 
) AS ReportCount
WHERE cnt >= 5