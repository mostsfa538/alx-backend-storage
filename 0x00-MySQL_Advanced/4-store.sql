-- creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER decreases_the_quantity
AFTER INSERT ON quantity
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

DELIMITER;
