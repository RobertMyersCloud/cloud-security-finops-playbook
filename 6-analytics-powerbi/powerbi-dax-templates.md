# Power BI — DAX Templates for Cloud Analytics

## Date Filters
SpendLast30 =
CALCULATE(SUM(Cost[Amount]), LASTDATE('Date'[Date]))

## Variance %
Variance =
DIVIDE([Actual] - [Budget], [Budget])

## Tag Completeness %
TagCoverage =
DIVIDE(COUNTROWS(TaggedResources), COUNTROWS(AllResources))

## Security Score
SecurityScore =
100 - ([HighFindings] * 5 + [MediumFindings] * 2)
