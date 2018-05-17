/* chapter17/mydb-mysql-schema-gbk.sql */

/* 创建数据库 */
CREATE DATABASE  IF NOT EXISTS  MyDB;

use MyDB;

/* 用户表 */
CREATE TABLE IF NOT EXISTS user (
name varchar(20),     /* 用户Id  */
userid int,	          /* 用户密码 */
PRIMARY KEY (userid));

/* 插入初始数据 */
INSERT INTO user VALUES('Tom',1);
INSERT INTO user VALUES('Ben',2);