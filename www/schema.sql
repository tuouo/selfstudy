-- schema.sql

drop database if exists awesome;
create table awesome;
use awesome;

grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users(
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `password` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `create_at` real not null,
    unique key `idx_email`(`email`),
    key `idx_create_at`(`create_at`),
    primary key(`id`)
)engine = innoodb default charset = utf8;

create table blogs(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `create_at` real not null,
    key `idx_create_at`(`create_at`),
    primary key(`id`)
)engine = innoodb default charset = utf8;

create table comment(
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `create_at` real not null,
    key `id_create_at`(`create_at`)
    primary key(`id`)
)engine = innoodb default charset = utf8;