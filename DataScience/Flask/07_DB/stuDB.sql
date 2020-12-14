-- 12/14 수업
create table students(
students_id int auto_increment primary key,
	name varchar(100),
	city varchar(50),
	addr varchar(200),
	pin varchar(10)
);

insert into students values('김광중', '서울', '동대문구 동작동', '2304');
insert into students (name, city, addr, pin)
values('김광중', '서울', '우주구 달나라군',1234);

select * from students;

