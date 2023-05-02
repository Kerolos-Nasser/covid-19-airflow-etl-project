CREATE TABLE IF NOT EXISTS covid_19
(
  Country varchar(255),
  Total_Cases DOUBLE PRECISION,
  New_Cases DOUBLE PRECISION,
  Total_Deaths DOUBLE PRECISION,
  New_Deaths DOUBLE PRECISION,
  Total_Recovered DOUBLE PRECISION,
  Active_Cases DOUBLE PRECISION,
  Serious DOUBLE PRECISION,
  Tot_Cases_1M_pop DOUBLE PRECISION,
  Deaths_1M_pop DOUBLE PRECISION,
  Total_Tests DOUBLE PRECISION,
  Tests_1M_pop DOUBLE PRECISION,
  CASES_per_Test DOUBLE PRECISION,
  Death_in_Closed_Cases DOUBLE PRECISION,
  Rank_by_Testing_rate DOUBLE PRECISION,
  Rank_by_Death_rate DOUBLE PRECISION,
  Rank_by_Cases_rate DOUBLE PRECISION,
  Rank_by_Death_of_Closed_Cases DOUBLE PRECISION
);