-- Завдання 1. Отримати всю інформацію з усіх інвойсів.
SELECT * FROM Invoice;

-- Завдання 2. Отримати айді інвойсів, білінгову адресу та країну білінгу клієнтів відсортовані по полю Total від більшої ціни до меншої.
SELECT InvoiceId, BillingAddress, BillingCountry, Total FROM Invoice ORDER BY Total DESC;

-- Завдання 3. Отримати список всіх клієнтів під назвою Frank.
SELECT CustomerId FROM Customer WHERE FirstName = 'Frank';

-- Завдання 4. Отримати айдішники клієнтів та айдишники інвойсів ціна, яких менше ніж 10 доларів.
SELECT CustomerId, InvoiceId, Total FROM Invoice WHERE Total < 10;

-- Завдання 5. Вивести список треків, ціна за юніт яких більша ніж 1.
SELECT TrackId, Name, UnitPrice FROM Track WHERE UnitPrice > 1;
