
SELECT
    c.login     AS "courierLogin",
    COUNT(o.id) AS "deliveryCount"
FROM
    "Couriers" AS c
    INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE
    o."inDelivery" = TRUE
GROUP BY
    c.login;
