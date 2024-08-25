CREATE TRIGGER trg_UpdateUpdatedAt
ON dbo.UserTable
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE UserTable
    SET updated_at = GETDATE()
    FROM inserted
    WHERE UserTable.userid = inserted.userid;
END;

-------------------------------------------------

SELECT * FROM sys.triggers

