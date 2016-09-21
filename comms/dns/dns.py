from core.framework.module import BaseModule
import plistlib


class Module(BaseModule):
    meta = {
        'name': 'Change DNS Settings',
        'author': 'Josh Summitt (@fusesoftllc)',
        'description': 'Update the DNS on the device',
        'options': (
            ('dns',"",  True, 'DNS Setting on the device'),
            ('wifi',"",  False, 'If blank all wifi interfaces will be set to the above DNS Ip.')
        ),
    }

    # ==================================================================================================================
    # UTILS
    # ==================================================================================================================
    def __init__(self, params):
        BaseModule.__init__(self, params)

    # ==================================================================================================================
    # RUN
    # ==================================================================================================================
    def module_run(self):
	prefs="/Library/Preferences/SystemConfiguration/preferences.plist"
	dns1=self.options['dns']
	dns2=self.options['wifi']
        # Setting DNS
        self.printer.info("Converting plist to xml")
	cmd_plutil="plutil -convert xml1 " + prefs
        out = self.device.remote_op.command_blocking(cmd_plutil)
        self.printer.info("Backing up preferences")
	cmd_backup="cp " + prefs + " " + prefs +"-bk"
	out = self.device.remote_op.command_blocking(cmd_backup)
	cmd_catit = "cat " + prefs
	plist_list = self.device.remote_op.command_blocking(cmd_catit)	
	#convert this array to one since string
        plist_str = ""
	i=0
	for str in plist_list:
		## the plistlib messes up on the first two lines so lets just skip them
		if i > 1:
			plist_str=plist_str + str
		i=i+1
	self.printer.info("Updating Preferences")	
	#print plist_str
	plist = plistlib.readPlistFromString(plist_str)
	for elem in plist.NetworkServices:
		networkPref = plist.NetworkServices[elem]
		for data in networkPref:
			if data == "DNS":
				networkPref["DNS"]["ServerAddresses"] = [dns1]
	plist_str = plistlib.writePlistToString(plist)
	self.printer.info("Pushing Preferences back to device")
	self.device.remote_op.command_blocking( "echo '" + plist_str + "' > " + prefs)
	self.device.remote_op.command_blocking( "ifconfig en0 down")
	self.device.remote_op.command_blocking( "ifconfig en0 up")
	self.printer.info("Complete")


