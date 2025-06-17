SELECT
  COUNTIF(Attrition) / COUNT(*) AS attrition_rate
FROM
  `retail-analytics-portfolio.newhrattritiondataset.employee_attrition`;

SELECT
  Department,
  COUNTIF(Attrition) / COUNT(*) AS attrition_rate
FROM
  `retail-analytics-portfolio.newhrattritiondataset.employee_attrition`
GROUP BY Department
ORDER BY attrition_rate DESC;

SELECT
  Tenure_Band,
  COUNTIF(Attrition) / COUNT(*) AS attrition_rate
FROM
  `retail-analytics-portfolio.newhrattritiondataset.employee_attrition`
GROUP BY Tenure_Band
ORDER BY attrition_rate DESC;

SELECT
  JobRole,
  ROUND(AVG(DailyRate), 2) AS avg_daily_rate
FROM
  `retail-analytics-portfolio.newhrattritiondataset.employee_attrition`
GROUP BY JobRole
ORDER BY avg_daily_rate DESC;
