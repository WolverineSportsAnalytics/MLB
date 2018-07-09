# MLB [![Build Status](https://travis-ci.org/WolverineSportsAnalytics/MLB.svg?branch=master)](https://travis-ci.org/WolverineSportsAnalytics/MLB) [![Coverage Status](https://coveralls.io/repos/github/WolverineSportsAnalytics/MLB/badge.svg?branch=master)](https://coveralls.io/github/WolverineSportsAnalytics/MLB?branch=master)
MLB daily fantasy sports predictor

# Sql Statements
select date, avg(abs(fanduelPoints - RotoWireProjection)) as avgs from players where fanduelPoints is not null group by date;
