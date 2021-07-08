CREATE DATABASE IF NOT EXISTS BloodBank;
USE BloodBank;

/*Create table commands*/

CREATE TABLE IF NOT EXISTS Donor(
DID varchar(5) not null primary key,
DName varchar(45) not null,
Age integer,
Sex char(1) default null,
phno bigint default null,
email varchar(45) default null,
bg varchar(10) not null, 
LDD date not null);

 CREATE TABLE IF NOT EXISTS Bloodbank(
 CID varchar(5) not null primary key,
 CName varchar(45) not null,
 Cloc varchar(20) default null,
 Cph bigint default null,
 A_pos int(5) default 0,
 A_neg int(5) default 0,
 B_pos int(5) default 0,
 B_neg int(5) default 0,
 AB_pos int(5) default 0,
 AB_neg int(5) default 0,
 O_pos int(5) default 0,
 O_neg int(5) default 0);
 
 CREATE TABLE IF NOT EXISTS Blood(
 BID varchar(5) not null primary key,
 bg varchar(10) not null,
 units int(5) not null,
 DD date not null,
 DID varchar(5) not null,
 Foreign key(DID) references Donor(DID) on update cascade on delete cascade);
 
 CREATE TABLE IF NOT EXISTS Hospital(
 HID varchar(5) not null primary key,
 HName varchar(45) not null,
 HLoc varchar(45) default null,
 Hph bigint default null);
 
CREATE TABLE IF NOT EXISTS Blood_Storage(
BID varchar(5) not null,
CID varchar(5) not null,
Foreign key(BID) references Blood(BID) on update cascade on delete cascade,
Foreign key(CID) references Bloodbank(CID) on update cascade on delete cascade,
Primary key(BID,CID));

CREATE TABLE IF NOT EXISTS Donor_Contact_Info(
DID varchar(5) not null,
CID varchar(5) not null,
Foreign key(DID) references Donor(DID) on update cascade on delete cascade,
Foreign key(CID) references Bloodbank(CID) on update cascade on delete cascade,
Primary key(DID,CID)); 
 
 CREATE TABLE IF NOT EXISTS Log(
 CID varchar(5) not null,
 HID varchar(5) not null,
 bg varchar(10) not null,
 units int(5) not null,
 foreign key(CID) references Bloodbank(CID) on update cascade on delete cascade,
 foreign key(HID) references Hospital(HID) on update cascade on delete cascade,
 primary key(CID,HID));
 
/*TRIGGER*/

CREATE TRIGGER tr_insert
BEFORE INSERT ON Donor
FOR EACH ROW 
SET new.DName = Upper(new.DName);

/*Insertion commands*/

INSERT INTO Donor(DID,DName,Age,Sex,phno,email,bg,LDD) VALUES
('D01','Ashish Chauhan',29,'M',8905182473,'ash@gmail.com','B-','2020-08-08'),
('D02','Divya M',22,'F',8905582973,'divya22@gmail.com','O-','2018-06-02'),
('D03','Maanvi Sen',36,'F',8865182973,'manu@gmail.com','O+','2019-12-22');

INSERT INTO Bloodbank VALUES
('C01','Lions Blood Bank','Chord Road',9901155344,0,0,0,12,0,0,0,3),
('C02','Life Care Blood Bank','Jayanagar',9141364180,3,0,0,5,4,9,0,0),
('C03','Jeeva Blood Bank','Tharagupet',9444107862,0,0,0,9,0,2,6,0);

INSERT INTO Blood VALUES
('B01','O-',3,'2018-03-02','D02'),
('B02','O+',3,'2019-12-22','D03'),
('B03','B-',4,'2020-08-08','D01');

INSERT INTO Hospital VALUES
('H01','Unity Hospital','Rajarajeshwari Nagar',8028611888),
('H02','BGS Hospital','Uttarahalli',8026255555),
('H03','Medsol Hospital','Jnanabharathi Layout',8028602354);

INSERT INTO Blood_Storage VALUES
('B01','C01'),
('B02','C03'),
('B03','C02');

INSERT INTO Donor_Contact_Info VALUES
('D01','C02'),
('D02','C01'),
('D03','C03');

INSERT INTO Log VALUES
('C01','H03','O-',3),
('C02','H01','AB-',9),
('C03','H01','AB-',2);

SELECT * FROM Donor;
SELECT * FROM Bloodbank;
SELECT * FROM Blood;
SELECT * FROM Hospital;
SELECT * FROM Blood_Storage;
SELECT * FROM Donor_Contact_Info;
SELECT * FROM Log;


