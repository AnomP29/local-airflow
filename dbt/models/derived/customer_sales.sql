

{{ config(
  materialized='table',
  file_format='delta'
) }}


SELECT count(customerid) as customer_count FROM
{{ source('osdp_sales', 'customer') }};


