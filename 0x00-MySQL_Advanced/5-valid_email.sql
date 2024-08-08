-- creates a trigger that resets the attribute valid_email only when the email has been changed
CREATE TRIGGER resets_the_attribute_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
    IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
    END IF;
END;
