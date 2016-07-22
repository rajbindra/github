from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
def main():
	dev = Device(host='172.27.0.159',user='rbindra',password='N0c@nd00')
    # open a connection with the device and start a NETCONF session
	try:
		dev.open()
	except Exception as err:
		print "Cannot connect to device:", err
		return

	dev.bind( cu=Config )

# Lock the configuration, load configuration changes, and commit
	print "Locking the configuration"
	try:
		dev.cu.lock()
	except LockError:
		print "Error: Unable to lock configuration"
		dev.close()
		return

	print "configuring"
	set_cmd = 'set system login message "Hello, Just testing Python!"'
	print "loading config"
	dev.cu.load(set_cmd, format='set')
	print "Committing the configuration"
	# commit the configuration
	try:
		dev.cu.commit()
	except CommitError:
		print "Error: Unable to commit configuration"
		print "Unlocking the configuration"
        try:
            dev.cu.unlock()
        except UnlockError:
            print "Error: Unable to unlock configuration"
        dev.close()
        return
        
	print "Unlocking the configuration"
	try:
		dev.cu.unlock()
	except UnlockError:
		print "Error: Unable to unlock configuration"

	dev.close()

if __name__ == "__main__":
        main()
