create database management_system;

create table books(
	bid varchar(20) primary key,
	title varchar(50),
	author varchar(50),
	status varchar(20)
);

create table books_issued(
	bid varchar(20) primary key,
	issuedto varchar(30)
);

select * from books;
select * from books_issued;