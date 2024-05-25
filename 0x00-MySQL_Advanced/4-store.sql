--modify the quantity after a new order is made
DELIMITER #
CREATE TRIGGER quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END #
DELIMITER ;


