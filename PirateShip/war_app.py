from armada import Armada
from ship import Ship

ships1 = [Ship(),Ship(),Ship(),Ship(),Ship(),Ship()]
armada1 = Armada(ships1)
ships2 = [Ship(),Ship(),Ship(),Ship()]
armada2 = Armada(ships2)
war_result = armada1.war(armada2)
print(war_result)
print(armada1)
print(armada2)