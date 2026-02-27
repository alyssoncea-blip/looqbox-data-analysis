/*
Objetivo:
Retornar os 10 produtos mais caros do catalogo.
*/

SELECT
    p.PRODUCT_COD,
    p.PRODUCT_NAME,
    p.PRODUCT_VAL,
    p.DEP_NAME,
    p.SECTION_NAME
FROM `looqbox-challenge`.data_product AS p
ORDER BY
    p.PRODUCT_VAL DESC,
    p.PRODUCT_COD ASC
LIMIT 10;
