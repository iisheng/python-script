# 该脚本 配合 SecureCRT 使用 连接的时候 选择 该脚本为登录脚本 然后 配置 参数 使用空格 分开


# $language = "python"
# $interface = "1.0"
def main():
	crt.Screen.Synchronous = True
	# user = "lisheng"
	# host = crt.Arguments.GetArg(0)
	password = crt.Arguments.GetArg(0)
	sendPassCmd = "%s\r" % (password)
	# 先ssh登录到目标服务
	# sshCmd = "ssh %s@%s \r" % (user, host)
	# crt.Screen.Send(sshCmd)
	# crt.Screen.WaitForString("password:",3)
	# crt.Screen.Send(sendPassCmd)

	# 切换为deploy账户
	deployCmd = "sudo su - deploy\r"
	crt.Screen.Send(deployCmd)
	crt.Screen.WaitForString("[sudo] password ", 0)
	crt.Screen.Send(sendPassCmd)
	crt.Screen.Clear()
	crt.Screen.Synchronous = False


main()
