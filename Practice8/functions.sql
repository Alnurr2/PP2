CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.name, c.phone FROM contacts c
                 WHERE c.name ILIKE '%' || p || '%'
                    OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(phone_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phone_owner, phone
    FROM phonebook
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;