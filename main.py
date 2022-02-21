import bankomat as b
import bank as ba
import mainscreen as ms
import card as ca
import chosen
import menuoperations as meop

main = ms.MainScreen()
ch = chosen.Chosen()
ch.operations()
card = ca.Card(ch.get_chosen())
#

# если пароль правильный - РАБОТА ИДЕТ
if(main.check_pin(ch.get_chosen(), card)):
    mo = meop.menuOperations()
    mo.print(card)
else:
    exit()
