
  
    

  create  table "dbt_local_proj"."dbt_test"."customer_sales__dbt_tmp"
  
  
    as
  
  (
    


SELECT count(customer_id) as customer_count, now() as created_date FROM
"dbt_local_proj"."dbt_test"."customer"
  );
  