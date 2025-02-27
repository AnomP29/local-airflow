

{{ config(
  materialized='table',
  file_format='delta'
) }}


SELECT count(customer_id) as customer_count, now() as created_date FROM
{{ source('osdp_sales', 'customer') }}


