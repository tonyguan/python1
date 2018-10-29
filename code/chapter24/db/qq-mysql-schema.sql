/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* 关东升 Created on:     2017/6/26 11:29:48                     */
/*==============================================================*/

/* 创建数据库 */
CREATE DATABASE  IF NOT EXISTS  qq;

use qq;

/* 用户表 */
CREATE TABLE IF NOT EXISTS users (
    user_id varchar(80) not null,   	 /* 用户Id  */
    user_pwd varchar(25)  not null,	 /* 用户密码 */
    user_name varchar(80) not null,  	 /* 用户名 */
    user_icon varchar(100) not null, 	 /* 用户头像 */
PRIMARY KEY (user_id));


/* 用户好友表Id1和Id2互为好友 */
CREATE TABLE IF NOT EXISTS friends (
    user_id1 varchar(80) not null,   	 /* 用户Id1  */
    user_id2 varchar(80) not null,   	 /* 用户Id2  */
PRIMARY KEY (user_id1, user_id2));
