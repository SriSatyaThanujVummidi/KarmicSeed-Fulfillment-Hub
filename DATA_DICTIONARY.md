# Data Dictionary

### orders.csv
order_id, order_time, customer_id, sku, quantity, priority, status, courier, pickup_deadline, product_variant_check

### products.csv
sku, product_name, category, variant, unit_price, reorder_level

### inventory.csv
sku, main_stock, secondary_stock, reserved

### couriers.csv
courier_id, courier_name, service_level, base_cost, pickup_cutoff

### issues.csv
issue_id, reference_id, issue_type, item, description, resolution_status, severity
