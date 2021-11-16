import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQd31Ep4Ih1r_gPM3emNDLz0CnSYq7ITQ3QvUQiCU_ArADvSpl5GUsSqQFQm_glYfUzHnncrhqt4h4Hd"
        self.client_secret = "EDWXjx5ekAH_UWWFczUawFh89pRgUVn6hjsC0G9MXwUrmz_5RE1CQjQkURfKIW0shrv59brrsGb68-OS"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
