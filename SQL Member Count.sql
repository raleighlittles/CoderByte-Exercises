SELECT ReportsTo,
  COUNT(*) as Members, 
  ROUND(AVG(Age)) as AverageAge 
  FROM maintable_5E2SV  WHERE ReportsTo IS NOT NULL 
  GROUP BY ReportsTo 
  ORDER BY ReportsTo
