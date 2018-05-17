/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* 关东升 Created on:     2017/6/26 11:29:48                     */
/*==============================================================*/

use petstore;

/* 用户表数据 */
INSERT INTO accounts VALUES('j2ee','j2ee','yourname@yourdomain.com','关东升', '北京丰台区', '北京', '中国',  '18811588888');
INSERT INTO accounts VALUES('ACID','ACID','acid@yourdomain.com','Tony', '901 San Antonio Road', 'Palo Alto', 'USA',  '555-555-5555');

/* 商品表数据 */
INSERT INTO products VALUES ('FI-SW-01','鱼类','神仙鱼', 'Angelfish', 'fish1.jpg', '来自澳大利亚的咸水鱼', 650, 400);
INSERT INTO products VALUES ('FI-SW-02','鱼类','虎鲨', 'Tiger Shark','fish4.jpg', '来自澳大利亚的咸水鱼', 850, 600);
INSERT INTO products VALUES ('FI-FW-01','鱼类','锦鲤', 'Koi','fish3.jpg', '来自日本淡水鱼', 150, 120);
INSERT INTO products VALUES ('FI-FW-02','鱼类','金鱼', 'Goldfish','fish2.jpg', '来自中国的淡水鱼', 150, 120);
INSERT INTO products VALUES ('K9-BD-01','狗类','斗牛犬', 'Bulldog','dog2.jpg', '来自英国友好的伴侣犬', 1500, 1200);
INSERT INTO products VALUES ('K9-PO-02','狗类','狮子狗', 'Poodle','dog6.jpg', '来自法国可爱狗狗',  1250, 1000);
INSERT INTO products VALUES ('K9-DL-01','狗类','斑点狗', 'Dalmation','dog5.jpg', '有很多斑点的狗狗', 2150, 2000);
INSERT INTO products VALUES ('K9-RT-01','狗类', '金毛猎犬', 'Golden Retriever','dog1.jpg', '很好的伴侣犬', 3800, 3400);
INSERT INTO products VALUES ('K9-RT-02','狗类', '拉布拉多犬','Labrador Retriever','dog5.jpg', '很好的狩猎犬', 3600, 3020);
INSERT INTO products VALUES ('K9-CW-01','狗类', '吉娃娃', 'Chihuahua','dog4.jpg', '性格温顺的狗狗', 1500,  120);
INSERT INTO products VALUES ('RP-SN-01','爬行类','响尾蛇', 'Rattlesnake','snake1.jpg','可怕且危险的动物', 150, 110);
INSERT INTO products VALUES ('RP-LI-01','爬行类','鬣蜥蜴', 'Iguana','lizard1.jpg', '主要生活在美洲和马达加斯加、斐济和汤加等地。',2600, 2203);
INSERT INTO products VALUES ('RP-LI-02','爬行类','变色树蜥蜴', 'Iguana','lizard2.jpg', '可随环境及光线强弱改变体色', 1000, 903);
INSERT INTO products VALUES ('RP-LI-03','爬行类','中国水龙蜴', 'Iguana','lizard3.jpg', '生活在中国云南的蜥蜴', 1600, 1003);
INSERT INTO products VALUES ('FL-DSH-01','猫类','马恩岛猫', 'Manx','cat3.jpg', '它能有效地减少老鼠的数量很有好处', 2503, 2120);
INSERT INTO products VALUES ('FL-DLH-02','猫类','波斯', 'Persian','cat1.jpg', '非常好的家猫', 3150, 2620);
INSERT INTO products VALUES ('FL-DLH-03','猫类','狸花猫', 'Persian2','cat2.jpg', '原产于中国的猫', 1000, 940);
INSERT INTO products VALUES ('AV-CB-01','鸟类','亚马逊鹦鹉', 'Amazon Parrot','bird4.jpg', '寿命长达75年的大鸟', 3150, 3000);
INSERT INTO products VALUES ('AV-SB-02','鸟类','鹦鹉1', 'Finch1','bird1.jpg', '会唱歌的鸟儿', 150, 110);
INSERT INTO products VALUES ('AV-SB-03','鸟类','鹦鹉2', 'Finch2','bird2.jpg', '会唱歌的鸟儿', 150, 110);
INSERT INTO products VALUES ('AV-SB-04','鸟类','鹦鹉3', 'Finch3','bird3.jpg', '会唱歌的鸟儿', 150, 110);
INSERT INTO products VALUES ('AV-SB-05','鸟类','鹦鹉4', 'Finch6','bird6.jpg', '会唱歌的鸟儿', 150, 110);
INSERT INTO products VALUES ('AV-SB-06','鸟类','鹦鹉5', 'Finch5','bird5.jpg', '会唱歌的鸟儿', 150, 110);
