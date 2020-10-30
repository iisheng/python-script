import os

g = os.walk(r"/Users/lisheng/KkbCode/kkb-cloud")

env = 'test'

namespace = 'e203b840-021b-43c0-896d-a2c1f1395f95'

nacos_server = 'nacos-headless.kkb-base-test.svc.cluster.local:8848'

nacos_config = '''profiles: %s
  cloud:
    nacos:
      config:
        prefix: ${spring.application.name}
        #prefix 对应文件名
        file-extension: yml
        #file-extension 文件格式
        server-addr: %s
        #配置中心地址
        shared-dataids: application.yml
        #shared-dataids 来支持多个共享 Data Id 的配置，多个之间用逗号隔开
        refreshable-dataids: application.yml
        #refreshable-dataids 来支持哪些共享配置的 Data Id 在配置变化时，应用中是否可动态刷新， 感知到最新的配置值，多个 Data Id 之间用逗号隔开
        namespace: %s
        group: DEFAULT_GROUP
''' % (env, nacos_server, namespace)

flag = 'profiles: test'

for path, dir_list, file_list in g:
    for file_name in file_list:
        if file_name == 'bootstrap.yml':
            file = open(os.path.join(path, file_name), "r")
            print(os.path.join(path, file_name))
            origin = file.read()
            file.close()
            start = origin.find(flag)
            end = origin.find('password: OPy#$hIVblv!9', start)

            origin_str = origin[start:end + 23]

            file1 = open(os.path.join(path, file_name), "w")

            origin = origin.replace(origin_str, nacos_config)

            file1.write(origin)
            file1.close()
