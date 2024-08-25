CREATE TABLE UserTable (
    userid INT IDENTITY(0001,1) PRIMARY KEY,
    username VARCHAR (255) NOT NULL,
    email VARCHAR (255) UNIQUE NOT NULL,
    password_hash VARCHAR (255) NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

--------------------------------------------
select * from UserTable