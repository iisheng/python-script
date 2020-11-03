import hashlib
import os.path

result_file = open("/Users/lisheng/Desktop/nacos_batch_insert_sql.txt", "w")

base_path = '/Users/lisheng/KkbCode/kkb-cloud-config-repo'
for entry in os.listdir(base_path):
    # 使用os.path.isfile判断该路径是否是文件类型
    if os.path.isfile(os.path.join(base_path, entry)):
        if not entry.startswith('.'):
            print(entry)
            file = open(os.path.join(base_path, entry), "r")
            file_md5 = open(os.path.join(base_path, entry), "rb")

            content = file.read()
            md5 = hashlib.md5(file_md5.read()).hexdigest()
            file_md5.close()
            data_id = entry
            group_id = 'DEFAULT_GROUP'
            tenant_id = 'e203b840-021b-43c0-896d-a2c1f1395f95'
            db_name = 'nacos_test'
            sql = "INSERT INTO `%s`.`config_info` (`data_id`, `group_id`, `content`, `md5`, `gmt_create`, `gmt_modified`, `src_user`, `src_ip`, `app_name`, `tenant_id`, `c_desc`, `c_use`, `effect`, `type`, `c_schema`) VALUES ('%s', '%s', '%s', '%s', '2020-10-26 16:44:33', '2020-10-26 16:59:57', null, '10.20.18.253', '', '%s', null, null, null, 'yaml', null)" % (
                db_name, data_id, group_id, content, md5, tenant_id)
            result_file.write(sql)
            result_file.write(';\n')
            file.close()

result_file.close()
