-- safe divide function to avoid 0 divide errors
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
IF b == 0 THEN
    RETURN 0;
ELSE
    RETURN a/b;
END IF;
DELIMITER ;