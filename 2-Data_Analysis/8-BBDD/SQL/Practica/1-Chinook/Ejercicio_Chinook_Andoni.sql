-- PARTE 1
--1
SELECT * 
FROM Customers 
WHERE Country = "Brazil";

--2
SELECT *
FROM employees 
WHERE Title = "Sales Support Agent";

--3
SELECT * 
FROM tracks
WHERE composer = "AC/DC";

--4
SELECT FirstName || " " || LastName AS NombreCompleto, CustomerId, Country 
FROM Customers 
WHERE country <> "USA"; 

--5
SELECT FirstName || " " || LastName AS NombreCompleto,
City || " " || State || " " || Country AS Direccion,
Email
FROM employees 
WHERE Title = "Sales Support Agent";

--6
SELECT DISTINCT BillingCountry
FROM invoices;

--7
SELECT DISTINCT count(CustomerId), State
FROM Customers
WHERE Country = "USA" 
GROUP BY State;


--8
SELECT InvoiceId, SUM(quantity) AS Cantidad_Artículos_Factura
FROM invoice_items 
WHERE invoiceid IN (37) 
GROUP BY 1;

--9
SELECT 
artists.Name,
COUNT(tracks.trackid)
FROM tracks
INNER JOIN albums ON tracks.albumid = albums.albumid
INNER JOIN artists ON albums.artistid = artists.artistid
WHERE artists.name = "AC/DC"
GROUP BY 1; 

--10
SELECT InvoiceId, SUM(quantity) AS Cantidad_Articulos
FROM invoice_items
GROUP BY invoiceId
ORDER BY Cantidad_Articulos DESC;

--11
SELECT BillingCountry, COUNT(InvoiceId) AS Cantidad_Facturas
FROM invoices
GROUP BY BillingCountry
ORDER BY Cantidad_Facturas DESC;

--12
SELECT strftime("%Y", invoicedate) AS Año, COUNT(InvoiceID) AS Cantidad_Facturas
FROM invoices
WHERE Año IN ("2009","2011")
GROUP BY 1;

--13
SELECT strftime("%Y", invoicedate) AS Año, COUNT(InvoiceID) AS Cantidad_Facturas
FROM invoices
WHERE Año BETWEEN "2009" AND "2011"
GROUP BY 1;

--14
SELECT Country, COUNT(CustomerId)
FROM Customers
WHERE Country IN ("Spain","Brazil")
GROUP BY 1
ORDER BY 2; -- porque me da la gana, básicamente 

--15 
SELECT name AS Canciones_Empiezan_Por_You
FROM tracks
WHERE Name LIKE "You%";


-- PARTE 2

--1
SELECT
  c.firstname || " " || c.lastname AS Nombre_cliente,
  i.invoiceid AS Id_factura,
  i.invoicedate AS Fecha_factura,
  i.billingcountry AS Pais_factura
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
WHERE c.country = "Brazil";

--2
SELECT
  e.firstname || " " || e.lastname AS Nombre_empleado,
  i.invoiceid,
  i.InvoiceDate,
  i.billingcountry
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid;

--3
SELECT
  c.firstname || " " || c.lastname AS Nombre_cliente,
  c.country AS Pais_cliente,
  e.firstname || " " || e.lastname AS Nombre_empleado,
  SUM(i.total)
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
GROUP BY 1, 2, 3
ORDER BY 4 DESC;

--4
SELECT
  ii.invoiceid,
  ii.trackid,
  t.name AS Nombre_cancion
FROM invoice_items ii
INNER JOIN tracks t ON ii.trackid = t.trackid;

--5
SELECT
  t.Name AS Nombre_cancion,
  mt.Name AS Nombre_formato,
  a.Title AS Nombre_album,
  g.Name AS Nombre_genero
FROM tracks t
INNER JOIN albums a ON t.albumid = a.albumid
INNER JOIN genres g ON t.genreid = g.GenreId
INNER JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId;

--6
SELECT
  pt.playlistid,
  p.name AS Nombre_playlist,
  COUNT(pt.trackid)
FROM playlist_track pt
INNER JOIN playlists p ON p.PlaylistId = pt.playlistid
GROUP BY 1, 2
ORDER BY 3 DESC;

--7
SELECT
  e.firstname || " " || e.lastname AS Nombre_empleado,
  SUM(i.total)
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
GROUP BY 1
ORDER BY 2 DESC;

--8
SELECT
  e.firstname || " " || e.lastname AS Nombre_empleado,
  SUM(i.total)
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
WHERE strftime("%Y", i.invoicedate) = "2009"
GROUP BY 1
ORDER BY 2 DESC;

--9
SELECT
  ar.artistid,
  ar.Name AS Nombre_artista,
  SUM(i.total) AS Ventas_totales
FROM invoices i
INNER JOIN invoice_items ii ON i.invoiceid = ii.invoiceid
INNER JOIN tracks t ON ii.trackid = t.trackid
INNER JOIN albums a ON t.albumid = a.albumid
INNER JOIN artists ar ON a.artistid = ar.ArtistId
GROUP BY 1, 2
ORDER BY 3 DESC;




