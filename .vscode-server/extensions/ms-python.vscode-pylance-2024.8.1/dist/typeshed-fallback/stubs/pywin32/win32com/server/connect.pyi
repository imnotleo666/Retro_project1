from _typeshed import Incomplete

from win32com import olectl as olectl
from win32com.server.exception import Exception as Exception

IConnectionPointContainer_methods: Incomplete
IConnectionPoint_methods: Incomplete

class ConnectableServer:
    cookieNo: int
    connections: Incomplete
    def EnumConnections(self) -> None: ...
    def GetConnectionInterface(self) -> None: ...
    def GetConnectionPointContainer(self): ...
    def Advise(self, pUnk): ...
    def Unadvise(self, cookie) -> None: ...
    def EnumConnectionPoints(self) -> None: ...
    def FindConnectionPoint(self, iid): ...
