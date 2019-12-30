USE lab_mysql;

SELECT * FROM Cars;

INSERT INTO Cars VALUES ('3K096I98581DHSNUP','Volkswagen','Tiguan',2019,'Blue');
INSERT INTO Cars VALUES ('ZM8G7BEUQZ97IH46V','Peugeot','Rifter',2019,'Red');
INSERT INTO Cars VALUES ('RKXVNNIHLVVZOUB4M','Ford','Fusion',2018,'White');
INSERT INTO Cars VALUES ('HKNDGS7CU31E9Z7JW','Toyota','RAV4',2018,'Silver');

SELECT * FROM Customers;

INSERT INTO Customers VALUES ('10001','Pablo Picasso','+34 636 17 63 82','','Paseo de la Chopera, 14','Spain');
INSERT INTO Customers VALUES ('20001','Abraham Lincoln','+1 305 907 7086','','120 SW 8th St','United States');
INSERT INTO Customers VALUES ('30001','Napoléon Bonaparte','+33 1 79 75 40 00','','-	40 Rue du Colisée','France');

SalespersonSalespersonSELECT * FROM Salesperson;

INSERT INTO Salesperson VALUES ('0','00001','Petey Cruiser','Madri');
INSERT INTO Salesperson VALUES ('1','00002','Anna Sthesia','Barcelona');
INSERT INTO Salesperson VALUES ('2','00003','Paul Molive','Berlin');
INSERT INTO Salesperson VALUES ('3	','00004','Gail Forcewind','Paris');

SELECT * FROM Invoice;

INSERT INTO Invoice VALUES ('0',852399038,22-08-2018,0,1,3);
INSERT INTO Invoice VALUES ('1',731166526,31-12-2018,3,0,5);
INSERT INTO Invoice VALUES ('2',271135104,22-01-2019,2,2,7);