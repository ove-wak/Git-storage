drop table if exists users;
-- drop table if exists rooms;
drop table if exists entries;
create table users (
  id integer primary key autoincrement,
  username string not null,
  password string not null
);
-- create table rooms (
--   id integer primary key autoincrement,
--   roomname string not null
-- );
create table entries (
  id integer primary key autoincrement,
  userid integer not null,
  -- room integer not null,
  text string not null,
  time string not null
);