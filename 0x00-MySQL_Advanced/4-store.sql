-- creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER decrease_quantity_after_new_order
BEFORE INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
