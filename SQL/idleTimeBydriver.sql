-- Question: Find the idle time for each driver in a day.
-- Idle time = time when the driver is not on any ride (gaps between consecutive trips).

-- Table: trips
-- trip_id | driver_id | start_time          | end_time
-- 101     | 1         | 2026-06-25 08:00:00 | 2026-06-25 09:30:00
-- 102     | 1         | 2026-06-25 10:15:00 | 2026-06-25 11:00:00
-- 103     | 1         | 2026-06-25 14:00:00 | 2026-06-25 15:30:00
-- 104     | 2         | 2026-06-25 09:00:00 | 2026-06-25 10:00:00

-- Expected output:
-- driver_id | trip_date  | idle_time
-- 1         | 2026-06-25 | 3 hrs 45 min
-- 2         | 2026-06-25 | 0


WITH gaps AS (
  SELECT
    driver_id,
    DATE(start_time) AS trip_date,
    start_time,
    LAG(end_time) OVER (
      PARTITION BY driver_id, DATE(start_time)
      ORDER BY start_time
    ) AS prev_end_time
  FROM trips
)
SELECT
  driver_id,
  trip_date,
  COALESCE(SUM(unix_timestamp(start_time) - unix_timestamp(prev_end_time)), 0) / 60 AS idle_minutes
FROM gaps
GROUP BY driver_id, trip_date;