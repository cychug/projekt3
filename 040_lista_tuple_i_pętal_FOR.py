errorCount = 0
logs = [('HTTP_OK', 'GET /index.html'),
        ('HTTP_OK', 'GET /index.html'),
        ('HTTP_NOT_FOUND', 'GET /index.html'),
        ('HTTP_OK', 'GET /index.html'),
        ('HTTP_OK', 'GET /index.html'),
        ('HTTP_NOT_FOUND', 'GET /index.htmll')]
print(logs[1][1])           # wybór konkretnego elementu krotki z listy

# 1 wersja
for status, message in logs:
    if status != 'HTTP_OK':
        errorCount += 1
print("Ilość zgłoszonych błędów: ", errorCount)

# 2 wersja
for log in logs:
    status, message = log
    if status != 'HTTP_OK':
        errorCount += 1
print("Ilość zgłoszonych błędów: ", errorCount)
