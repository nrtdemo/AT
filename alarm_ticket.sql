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
create table tts
(
  ticketNo        varchar(50)  not null
    primary key,
  incident_id     varchar(255) not null,
  affected_item   varchar(255) not null,
  cat_id          varchar(255) not null,
  status          varchar(255) not null,
  problem_status  varchar(255) not null,
  downtime_start  varchar(255) not null,
  downtime_time   varchar(255) not null,
  owner_group     varchar(255) not null,
  repairteam      varchar(255) not null,
  oss_source      varchar(255) null,
  oss_destination varchar(255) null,
  bandwidth       varchar(255) null,
  address         text         null,
  title           varchar(255) null,
  description     text         null,
  activity        mediumtext   null,
  constraint tts_ticketNo_uindex
  unique (ticketNo)
)
  engine = InnoDB
  collate = utf8mb4_unicode_ci;


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

