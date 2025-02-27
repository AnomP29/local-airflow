
  
    

  create  table "dbt_local_proj"."dbt_test"."customer_sales__dbt_tmp"
  
  
    as
  
  (
    


SELECT count(customerid) as customer_count FROM
"dbt_local_proj"."sales"."customer";
  );
  