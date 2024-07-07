-- 创建表
CREATE TABLE tb_student(
stuid int not null,
stuname VARCHAR(25) not null,
stusex BIT DEFAULT(1),
stubirth DATE,
PRIMARY KEY(stuid)
)

CREATE TABLE tb_college(
colid int auto_increment COMMENT '编号',
colname VARCHAR(31) not null COMMENT '学院名称',
website VARCHAR(1023) COMMENT '学院网址',
PRIMARY KEY(colid))

-- 新增列
ALTER TABLE tb_student ADD COLUMN stuaddr VARCHAR(255)
ALTER TABLE tb_student add COLUMN colid INT

-- 插入数据
INSERT INTO tb_student VALUES(1001,'张三',1,'2002-02-02','湖北'),(1002,'李四',1,'2003-03-03','北京')
INSERT into tb_student(stuid,stuname) VALUES(1003,'王五')
INSERT INTO tb_student VALUES(1004,'赵六'),(1005,'张三丰'),(1006,'谢逊'),(1007,'周芷若')


-- 存在自增列可不提供值，会自动插入
INSERT INTO tb_college (colname) VALUES('计算机学院'),('外国语学院'),('汉语言学院')

-- 删除数据（可以加where条件，可以恢复，但是慢）
DELETE FROM tb_student WHERE stuid = '1003'

-- 截断表(不删除表结构，但会快，无法恢复)
-- TRUNCATE TABLE tb_student

-- drop表（直接删除表结构与数据，无法恢复）
-- drop TABLE tb_student

-- 更新数据操作
UPDATE tb_student set stuaddr='四川成都' where stuid IN(1001,1002)
UPDATE tb_student set stuaddr='湖南长沙',stubirth='1900-01-01' WHERE stuid=1004
UPDATE tb_student set colid=1 WHERE stuid BETWEEN 1001 and 1004
UPDATE tb_student set colid=2 WHERE stuid BETWEEN 1005 and 1006
UPDATE tb_student set colid=3 WHERE stuid=1007


-- 修改学生表添加外键约束（一般加在多对一种的多那张表）
ALTER TABLE tb_student add CONSTRAINT fk_student_colid FOREIGN KEY(colid)
REFERENCES tb_college(colid)

-- 也可以在创建表的时候添加外键约束
/*
CREATE TABLE children (  
    id INT AUTO_INCREMENT,  
    parent_id INT,  
    name VARCHAR(100) NOT NULL,  
    PRIMARY KEY (id),  
    FOREIGN KEY (parent_id) REFERENCES parents(id)  
        ON DELETE SET NULL -- 可选，指定父表记录被删除时的行为  
        ON UPDATE CASCADE -- 可选，指定父表记录被更新时的行为  
);
*/

