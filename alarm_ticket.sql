-- auto-generated definition
CREATE TABLE splunk
(
  splunk_id     INT UNSIGNED AUTO_INCREMENT
    PRIMARY KEY,
  cat_id        VARCHAR(255) NOT NULL,
  path          TEXT         NOT NULL,
  port_status   VARCHAR(255) NOT NULL,
  src_interface VARCHAR(255) NOT NULL,
  device_time   VARCHAR(255) NOT NULL,
  hostname      VARCHAR(255) NOT NULL,
  host          VARCHAR(255) NOT NULL,
  flap          VARCHAR(255) NOT NULL
)
  ENGINE = InnoDB
  COLLATE = utf8mb4_unicode_ci;

-- auto-generated definition
CREATE TABLE tts
(
  ticketNo        VARCHAR(50)  NOT NULL
    PRIMARY KEY,
  incident_id     VARCHAR(255) NOT NULL,
  affected_item   VARCHAR(255) NOT NULL,
  cat_id          VARCHAR(255) NOT NULL,
  status          VARCHAR(255) NOT NULL,
  problem_status  VARCHAR(255) NOT NULL,
  downtime_start  VARCHAR(255) NOT NULL,
  downtime_time   VARCHAR(255) NOT NULL,
  owner_group     VARCHAR(255) NOT NULL,
  repairteam      VARCHAR(255) NOT NULL,
  oss_source      VARCHAR(255) NULL,
  oss_destination VARCHAR(255) NULL,
  address         TEXT         NULL,
  title           VARCHAR(255) NULL,
  description     TEXT         NULL,
  activity        MEDIUMTEXT   NULL,
  CONSTRAINT tts_ticketNo_uindex
  UNIQUE (ticketNo)
)
  ENGINE = InnoDB
  COLLATE = utf8mb4_unicode_ci;

-- auto-generated definition
create table online_active
(
  catid     varchar(255)                        not null
    primary key,
  timestamp timestamp default CURRENT_TIMESTAMP not null
  on update CURRENT_TIMESTAMP,
  constraint online_active_catid_uindex
  unique (catid)
)
  engine = InnoDB;

