CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
      DECLARE n_off int;
      SET n_off = N - 1;
  RETURN (
      SELECT Salary from Employee group by salary order by Salary desc LIMIT 1 OFFSET n_off
  );
END