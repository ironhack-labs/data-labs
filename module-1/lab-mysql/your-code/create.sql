USE lab_mysql;

CREATE TABLE Cars (
    VIN VARCHAR(255),
    Manufacturer VARCHAR(255),
    Model VARCHAR(255),
    Year INT,
    Color VARCHAR(255),
    PRIMARY KEY (VIN)
);

CREATE TABLE Customers (
    CustomerID VARCHAR(255),
    Name VARCHAR(255),
    PhoneNumber VARCHAR(255),
    Email VARCHAR(255),
    Address VARCHAR(255),
    Country VARCHAR(255),
    PRIMARY KEY (CustomerID)
);

CREATE TABLE Salesperson (
    StaffID VARCHAR(255),
    Name VARCHAR(255),
    Store VARCHAR(255),
    PRIMARY KEY (StaffID)
);

CREATE TABLE Invoice (
    InvoiceNR INT,
    Date DATE,
    PRIMARY KEY (InvoiceNR),
    VIN VARCHAR (255) REFERENCES Cars(VIN),
    CustomerID VARCHAR (255) REFERENCES Customers(CustomerID),
    SalespersonID VARCHAR (255) REFERENCES Salesperson(StaffID)
);
    