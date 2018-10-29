/*==============================================================*/
/* 股票信息数据库DDL脚本                                        */
/* 代码文件：代码\chapter22\22.4\db\crebas.sql                  */
/*==============================================================*/

/* 创建数据库 */
create database if not exists NASDAQ;

use NASDAQ;

drop table if exists HistoricalQuote;

drop table if exists Stocks;

/*==============================================================*/
/* Table: HistoricalQuote                                       */
/*==============================================================*/
create table HistoricalQuote
(
   HDate                date not null,
   Open                 decimal(8,4),
   High                 decimal(8,4),
   Low                  decimal(8,4),
   Close                decimal(8,4),
   Volume               bigint,
   Symbol               varchar(10),
   primary key (HDate)
);


/*==============================================================*/
/* Table: Stocks                                                */
/*==============================================================*/
create table Stocks
(
   Symbol               varchar(10) not null,
   Company              varchar(50) not null,
   Industry             varchar(10) not null,
   primary key (Symbol)
);

alter table HistoricalQuote add constraint FK_Reference_1 foreign key (Symbol)
      references Stocks (Symbol) on delete restrict on update restrict;


insert into Stocks (Symbol, Company, Industry) values ('AAPL', 'Apple Inc.', 'Technology');

