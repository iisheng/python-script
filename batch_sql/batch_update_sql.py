file1 = open("/Users/lisheng/Desktop/ids.txt", "r")
file2 = open("/Users/lisheng/Desktop/batch_update_sql.txt", "w")

for line in file1.readlines():
    lineStr = line.strip()

    if lineStr != '':
        content = ''
        origin = 'UPDATE `kkb-cloud-vipcourse`.vip_order SET `status` = 7 WHERE id = '
        end = ';\n'
        content += origin
        content += line.strip()
        content += end

        file2.write(content)

file1.close()
file2.close()
