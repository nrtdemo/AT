-- auto-generated definition
create table splunk
(
  splunk_id     int unsigned auto_increment
    primary key,
  cat_id        varchar(255) not null,
  path          text         not null,
  port_status   varchar(255) not null,
  src_interface varchar(255) not null,
  device_time   varchar(255) not null,
  hostname      varchar(255) not null,
  host          varchar(255) not null,
  flap          varchar(255) not null
)
  engine = InnoDB
  collate = utf8mb4_unicode_ci;

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
  address         text         null,
  title           varchar(255) null,
  description     text         null,
  activity        mediumtext   null,
  bandwidth       varchar(255) null,
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



