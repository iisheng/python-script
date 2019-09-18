# $language = "python"
# $interface = "1.0"
def main():
	crt.Screen.Synchronous = True
	user = "lisheng"
	host = crt.Arguments.GetArg(0)
	password = crt.Arguments.GetArg(1)
	sendPassCmd = "%s\r" % (password)
	# 先ssh登录到目标服务
	sshCmd = "ssh %s@%s \r" % (user, host)
	crt.Screen.Send(sshCmd)
	crt.Screen.WaitForString("password:", 1)
	crt.Screen.Send(sendPassCmd)

	# 切换为deploy账户
	# deployCmd = "sudo su - deploy\r"
	# crt.Screen.Send(deployCmd)
	# crt.Screen.WaitForString("[sudo] password ",0)
	# crt.Screen.Send(sendPassCmd)
	crt.Screen.Clear()
	crt.Screen.Synchronous = False


main()
