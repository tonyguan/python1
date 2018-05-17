/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* 关东升 Created on:     2017/6/26 11:29:48                     */
/*==============================================================*/

use qq

/* 用户表数据 */
INSERT INTO users VALUES('111','123', '关东升', '28');
INSERT INTO users VALUES('222','123', '赵1', '30');
INSERT INTO users VALUES('333','123', '赵2', '52');
INSERT INTO users VALUES('888','123', '赵3', '53');

/* 用户好友表Id1和Id2互为好友 */
INSERT INTO friends VALUES('111','222');
INSERT INTO friends VALUES('111','333');
INSERT INTO friends VALUES('888','111');
INSERT INTO friends VALUES('222','333');
