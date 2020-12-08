from zipfile import ZipFile

zipObj = ZipFile('DAY-4/sample.zip', 'w')
# Add multiple files to the zip
zipObj.write('DAY-4/file.txt')
zipObj.write('DAY-4/file.html')
# close the Zip File
zipObj.close()