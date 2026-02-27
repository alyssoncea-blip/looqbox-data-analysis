/*
Objetivo:
Listar as secoes associadas aos departamentos BEBIDAS e PADARIA.
*/

SELECT DISTINCT
    p.DEP_COD,
    p.DEP_NAME,
    p.SECTION_COD,
    p.SECTION_NAME
FROM `looqbox-challenge`.data_product AS p
WHERE p.DEP_NAME IN ('BEBIDAS', 'PADARIA')
ORDER BY
    p.DEP_NAME ASC,
    p.SECTION_NAME ASC,
    p.SECTION_COD ASC;
