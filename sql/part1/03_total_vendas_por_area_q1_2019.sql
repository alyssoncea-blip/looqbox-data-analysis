/*
Objetivo:
Apurar o total de vendas em dolar por Area de Negocio no 1o trimestre de 2019.
*/

SELECT
    c.BUSINESS_CODE,
    c.BUSINESS_NAME,
    ROUND(SUM(s.SALES_VALUE), 2) AS TOTAL_SALES_VALUE_USD
FROM `looqbox-challenge`.data_store_sales AS s
INNER JOIN `looqbox-challenge`.data_store_cad AS c
    ON c.STORE_CODE = s.STORE_CODE
WHERE s.DATE >= '2019-01-01'
  AND s.DATE < '2019-04-01'
GROUP BY
    c.BUSINESS_CODE,
    c.BUSINESS_NAME
ORDER BY TOTAL_SALES_VALUE_USD DESC;
