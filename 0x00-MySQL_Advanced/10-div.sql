-- creates a function SafeDiv
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE res FLOAT;
    IF b = 0 THEN
        SET res = 0;
    ELSE
        SET res = (a * 1.0) / b;
    END IF;
    RETURN res;
END $$
DELIMITER ;
