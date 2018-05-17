/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* 关东升 Created on:     2017/6/26 11:29:48                     */
/*==============================================================*/

/* 创建数据库 */
CREATE DATABASE  IF NOT EXISTS  petstore;

use petstore;

/* 用户表 */
CREATE TABLE IF NOT EXISTS accounts (
    userid varchar(80) not null,   	 /* 用户Id  */
    password varchar(25)  not null,	 /* 用户密码 */
    email varchar(80) not null,  	 /* 用户Email */
    name varchar(80) not null, 		 /* 用户名 */
    addr varchar(80) not null, 		 /* 地址 */
    city varchar(80) not  null, 	 /*  所在城市 */
    country varchar(20) not null, 	 /*  国家 */
    phone varchar(80) not null, 	 /*  电话号码 */
PRIMARY KEY (userid));

/* 商品表 */
CREATE TABLE IF NOT EXISTS products (
    productid varchar(10) not null,	/* 商品Id */
    category varchar(10) not null,	/* 商品类别 */
    cname varchar(80) null,		/* 商品中文名 */
    ename varchar(80) null,		/* 商品英文名 */
    image varchar(20) null,		/* 商品图片 */
    descn varchar(255) null,		/* 商品描述 */
    listprice decimal(10,2) null, 	/* 商品市场价 */
    unitcost decimal(10,2) null,	/* 商品单价 */
PRIMARY KEY (productid));

/* 订单表 */
CREATE TABLE IF NOT EXISTS orders (
    orderid bigint not null,		/* 订单Id */
    userid varchar(80) not null,	/* 下订单的用户Id */
    orderdate datetime not null,		/* 下订单时间 */
    status int not null default 0,	/* 订单付款状态  0待付款  1已付款 */    
    amount decimal(10,2) not null,	/* 订单应付金额 */
PRIMARY KEY (orderid));

/* 订单明细表 */
CREATE TABLE IF NOT EXISTS orderdetails (
    orderid bigint not null,		/* 订单Id */
    productid varchar(10) not null,	/* 商品Id */
    quantity int not null,		/* 商品数量 */
    unitcost decimal(10,2) null,	/* 商品单价 */
PRIMARY KEY (orderid, productid));