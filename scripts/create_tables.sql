CREATE TABLE Observation (
    id    Varchar(20) NOT NULL
  , time  Double      NOT NULL
  , light Double      NOT NULL
  , error Double      NOT NULL
  , PRIMARY KEY (id, time)
);

CREATE TABLE Result (
    id       Varchar(20) NOT NULL
  , time     Double      NOT NULL
  , category Varchar(20) NOT NULL
  , chance   Double      NOT NULL
  , PRIMARY KEY (id, time, category)
);
